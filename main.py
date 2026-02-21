from fastmcp import FastMCP
from src import AppContext
from src.graph import graph

mcp = FastMCP("MyAgent")

context_instance = AppContext(name="My first langgraph setup")


@mcp.tool()
async def entrypoint(query: str) -> str:
    result = await graph.ainvoke(
        {'input': query, 'results': ''},
        context=context_instance,
    )
    return result['demo_result']


if __name__ == "__main__":
    mcp.run(transport="http")
