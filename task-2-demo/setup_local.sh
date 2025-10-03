#!/bin/bash

echo "🚀 Setting up Offers API for local development..."

# Create data directory
mkdir -p data

# Create a sample CSV file for testing (since the original data file is missing)
echo "📊 Creating sample data file..."
cat > data/adresowo_warszawa_wroclaw.csv << 'EOF'
rooms,area_m2,photos,locality,street,property_type,city,price_total_zl
3,65.5,5,Krzyki,ul. Krzycka,apartment,Wrocław,450000
2,45.2,3,Śródmieście,ul. Świdnicka,apartment,Wrocław,380000
4,85.0,8,Psie Pole,ul. Psie Pole,apartment,Wrocław,520000
1,32.1,2,Stare Miasto,ul. Oławska,apartment,Wrocław,280000
3,70.8,6,Krzyki,ul. Legnicka,apartment,Wrocław,470000
2,48.5,4,Śródmieście,ul. Kazimierza Wielkiego,apartment,Wrocław,410000
EOF

echo "✅ Sample data file created!"

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Create database and tables
echo "🗄️ Creating database..."
python create_db.py

# Train the initial model
echo "🤖 Training initial model..."
python train.py

echo "✅ Setup complete!"
echo ""
echo "To run the application locally:"
echo "1. Run: uvicorn main:app --reload --host 0.0.0.0 --port 8000"
echo "2. Open: http://localhost:8000"
echo "3. API docs: http://localhost:8000/docs"
echo ""
echo "To build Docker image:"
echo "docker build -t offers-api:latest ."
