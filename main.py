from fastmcp import FastMCP
from app.time.tool import register_time_tools
from app.system.tool import register_system_tools
from app.network.tool import register_network_tools
from app.calculator.tool import register_calculator_tools

mcp = FastMCP(
    "MCP Tools",
    debug=True,
)

register_funcs = [
    register_time_tools,
    register_system_tools,
    register_network_tools,
    register_calculator_tools,
]

# 循环调用
for register in register_funcs:
    register(mcp)

if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=33669)
    # mcp.run(transport="stdio", host="0.0.0.0", port=33669)
    # mcp.run(transport="http", host="127.0.0.1", port=33669)
