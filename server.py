from fastmcp import FastMCP

mcp = FastMCP("My-Nutri-MCP")

@mcp.tool()
def get_vitamin_c_info() -> str:
    """비타민 C의 권장 섭취량 및 효능 정보를 반환합니다."""
    return "비타민C 권장 섭취량은 하루 100mg이며, 항산화 작용과 면역력 증진에 도움을 줍니다."

if __name__ == "__main__":
    mcp.run()
    