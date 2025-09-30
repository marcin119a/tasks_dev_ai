from fastapi import FastAPI
import models
import asyncio
from utils import predict_price
from database import SessionLocal
from sqlalchemy.orm import Session
from fastapi import Depends
from functools import lru_cache

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def read_root():
    return {"message": "API do mieszkań we Wrocławiu"}

@app.post("/predict/")
async def predict(offer: models.PricePrediction):
   predicted_price = await asyncio.get_event_loop().run_in_executor(
       None, predict_price, offer.rooms, offer.area_m2, offer.photos, offer.locality, offer.street, offer.property_type, offer.city
   )
   return {"predicted_price": predicted_price}

@app.post("/offers/")
async def create_offer(offer: models.OfferCreate, db: Session = Depends(get_db)):
    predict_price_value = predict_price(offer.rooms, offer.area_m2, offer.photos, offer.locality, offer.street, offer.property_type, offer.city)
    df_offer = models.OfferDB(
        area_m2=offer.area_m2,
        photos=offer.photos,
        locality=offer.locality,
        street=offer.street,
        property_type=offer.property_type,
        city=offer.city,
        price=predict_price_value
    )
    db.add(df_offer)
    db.commit()
    db.refresh(df_offer)
    return df_offer

@app.get("/offers/")
@lru_cache(maxsize=32)
def read_offers(db: Session = Depends(get_db)):
    return db.query(models.OfferDB).all()