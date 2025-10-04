from fastmcp import FastMCP
from typing import List, Dict, Any
import json

mcp = FastMCP(name="My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    """Greet a user by name."""
    return f"Hello, {name}!"

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

@mcp.tool
def get_system_info() -> Dict[str, Any]:
    """Get system information."""
    import platform
    return {
        "platform": platform.platform(),
        "python_version": platform.python_version(),
        "architecture": platform.architecture()[0],
        "processor": platform.processor()
    }

@mcp.tool
def create_todo_list(items: List[str]) -> Dict[str, Any]:
    """Create a todo list from items."""
    return {
        "todo_list": items,
        "total_items": len(items),
        "status": "created"
    }

@mcp.tool
def calculate_area(length: float, width: float) -> Dict[str, float]:
    """Calculate area of a rectangle."""
    area = length * width
    return {
        "length": length,
        "width": width,
        "area": area,
        "perimeter": 2 * (length + width)
    }

if __name__ == "__main__":
    mcp.run()  # This starts the MCP server with stdio transport by default
