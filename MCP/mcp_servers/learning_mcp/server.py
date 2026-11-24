
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

def multiplication_table(number: int):

    table = []

    for i in range(1, 11):

        result = number * i

        table.append(f"{number} x {i} = {result}")

    return "\n".join(table)

@mcp.tool()
def number_factors(number: int):

    factors = []

    for i in range(1, number + 1):

        if number % i == 0:

            factors.append(i)

    return factorse

# RESOURCE 1: Mathematical Formulas

@mcp.resource("math://formulas")
def mathematical_formulas() -> str:
    """Provide commonly used mathematical formulas."""

    return """
    MATHEMATICAL FORMULAS

    1. Addition: a + b
    2. Subtraction: a - b
    3. Multiplication: a * b
    4. Division: a / b
    5. Modulus: a % b
    6. Power: a ** b
    7. Square: a ** 2
    8. Even Number: number % 2 == 0
    """


# RESOURCE 2: Mathematical Rules

@mcp.resource("math://rules")
def mathematical_rules() -> str:
    """Provide basic mathematical rules."""

    return """
    MATHEMATICAL RULES

    1. Division by zero is not allowed.
    2. A number is even if divisible by 2.
    3. A number is odd if not divisible by 2.
    4. Factors divide a number without a remainder.
    5. Square means multiplying a number by itself.
    6. Modulus returns the remainder after division.
    """

@mcp.prompt()
def math_teacher(topic: str) -> str:
    """Teach a mathematical topic."""

    return f"""
    Act as a mathematics teacher.
    Explain {topic} with examples.
    """


@mcp.prompt()
def calculation_explainer(expression: str) -> str:
    """Explain a mathematical calculation."""

    return f"""
    Explain this expression step by step: {expression}
    """


@mcp.prompt()
def math_quiz(difficulty: str = "easy") -> str:
    """Generate a mathematics quiz."""

    return f"""
    Generate five mathematics questions.
    Difficulty: {difficulty}
    """


if __name__ == "__main__":
    mcp.run()
