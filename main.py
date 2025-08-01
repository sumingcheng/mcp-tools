from app.common.mcp import mcp


if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=33669)
    # mcp.run(transport="stdio", host="0.0.0.0", port=33669)
    # mcp.run(transport="http", host="127.0.0.1", port=33669)
