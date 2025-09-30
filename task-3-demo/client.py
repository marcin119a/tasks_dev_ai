from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent
from langchain_mcp_adapters.tools import load_mcp_tools

load_dotenv()

server_params = StdioServerParameters(
    command="python3",
    # Full absolute path to the server.py file
    args=["server.py"],
)

import asyncio

async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await load_mcp_tools(session)

            agent = create_react_agent('openai:gpt-4o-mini', tools)
            agent_response = await agent.ainvoke({"messages": "Show me the best offers for flats for 300.000-400.000 in Warsaw."})
            print(agent_response["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())