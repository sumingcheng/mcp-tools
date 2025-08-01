from app.common.mcp import mcp
from app.tool_loader import load_tools

# 自动加载所有工具
load_tools()

if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=33669)
    # mcp.run(transport="stdio", host="0.0.0.0", port=33669)
    # mcp.run(transport="http", host="127.0.0.1", port=33669)
