
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("hello-mcp")


@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers and return the result."""
    return a + b


@mcp.tool()
def modulus(a: float, b: float) -> float:
    """Return the remainder of a divided by b."""
    return a % b


@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract the second number from the first."""
    return a - b


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide the first number by the second."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


@mcp.tool()
def power(a: float, b: float) -> float:
    """Calculate the first number raised to the power of the second."""
    return a ** b


@mcp.tool()
def square(a: float) -> float:
    """Return the square of a number."""
    return a ** 2


@mcp.tool()
def is_even(number: int) -> bool:
    """Check whether a number is even."""
    return number % 2 == 0


if __name__ == "__main__":
    mcp.run()
