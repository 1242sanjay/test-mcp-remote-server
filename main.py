from fastmcp import FastMCP
import random
import json

#Create the FastMCP server instance
mcp = FastMCP("Simple Calculator Server")

# Tool: Add two numbers
@mcp.tool("add", description="Add two numbers")
def add(a: float, b: float) -> float:
    """Add two numbers and return the result.
    
    Args:
        a (float): The first number.
        b (float): The second number.
    Returns:
        float: The sum of a and b.
    """
    return a + b

# Tool: Generate a random number
@mcp.tool("random_number", description="Generate a random number within a specified range")
def random_number(min_val: int, max_val: int) -> int:
    """Generate a random number within a specified range.
    
    Args:
        min_val (int): The minimum value.
        max_val (int): The maximum value.
    
    Returns:
        int: A random number between min_val and max_val.
    """
    return random.randint(min_val, max_val)


# Resource: Server information
@mcp.resource("info://server", description="Get information about the server")
def server_info() -> str:
    """Get information about the server.
    
    Returns:
        str: A JSON string containing server information.
    """
    info = {
        "name": mcp.name,
        "version": "1.0",
        "description": "A simple calculator server with random number generation.",
        "tools": ["add", "random_number"],
        "authors": ["Sanjay Kumar"]
    }
    return json.dumps(info)



if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)