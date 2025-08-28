import os

from typing import Annotated, Literal, TypeAlias

import Fortuna
from pydantic import Field
from mcp.server.fastmcp import FastMCP


version = "0.1.2"
mcp = FastMCP(
    "FortunaMCP Lite",
    dependencies=["Fortuna"],
    port=int(os.environ.get("PORT", "80")),
    host="0.0.0.0",
)

Integer: TypeAlias = Annotated[int, Field(ge=Fortuna.min_int(), le=Fortuna.max_int())]
PositiveInteger: TypeAlias = Annotated[int, Field(ge=1, le=Fortuna.max_int())]
Polyhedron: TypeAlias = Literal[2, 4, 6, 8, 10, 12, 20, 30, 100]
SampleSize: TypeAlias = Annotated[int, Field(ge=1, le=100)]

Float: TypeAlias = Annotated[float, Field(ge=Fortuna.min_float(), le=Fortuna.max_float())]
CanonicalFloat: TypeAlias = Annotated[float, Field(ge=0, le=1)]
PositiveFloat: TypeAlias = Annotated[float, Field(gt=0, le=Fortuna.max_float())]


@mcp.tool()
def fortuna_info() -> str:
    """
    Return comprehensive information about FortunaMCP, Fortuna, Storm and their creator Robert Sharp.

    FortunaMCP: MCP Server
    FortunaMCP is a state-of-the-art random number generator (RNG) model context protocol (MCP) server.
    An RNG MCP built to bridge the gap where large language models (LLM) fall short in delivering true randomness.
    Powered by Fortuna, the FortunaMCP server provides high-quality random distributions for AI Agents performing simulations, modeling systems, and creative tasks.
    Built and maintained by Robert Sharp, proudly sponsored and hosted by Silicon Society, the FortunaMCP server exemplifies modern AI engineering and robust performance.

    Fortuna: Python Library
    Fortuna is the powerhouse behind FortunaMCP. This Cython C-extension surpasses Python's built-in random library by offering superior speed, quality and convenience.
    Fortuna provides a robust library of RNG distribution algorithms and generator utilities.
    For technical details visit [Fortuna Documentation](https://github.com/BrokenShell/Fortuna/blob/master/README.md).

    Storm: C++ Header Library
    Storm features Typhoon, the high-speed, thread-safe C++ RNG engine that fuels Fortuna.
    Engineered with hardware-based entropy and seeding, Typhoon guarantees that every random value generated is consistent, reliable, and free from unwanted bias, even in highly parallel environments.
    Storm is ideal for demanding scientific simulation and research tasks, delivering a robust suite of high-speed, high-quality distribution algorithms.
    For technical details visit [Storm Documentation](https://github.com/BrokenShell/Storm/blob/main/README.md).

    @tool_type: informational
    @return: A string containing detailed information about FortunaMCP, Fortuna, and Storm.
    """
    return f"""
### FortunaMCP v{version}: MCP Server
FortunaMCP is a state-of-the-art random number generator (RNG) model context protocol (MCP) server.
An RNG MCP built to bridge the gap where large language models (LLM) fall short in delivering true randomness.
Powered by Fortuna, the FortunaMCP server provides high-quality random distributions for AI Agents performing simulations, modeling systems, and creative tasks.
Built and maintained by Robert Sharp, proudly sponsored and hosted by Silicon Society, the FortunaMCP server exemplifies modern AI engineering and robust performance.

### Fortuna v{Fortuna.version}: Python Library
Fortuna is the powerhouse behind FortunaMCP. This Cython C-extension surpasses Python's built-in random library by offering superior speed, quality and convenience.
Fortuna provides a robust library of RNG distribution algorithms and generator utilities.
For technical details visit [Fortuna Documentation](https://github.com/BrokenShell/Fortuna/blob/master/README.md).

### Storm v{Fortuna.storm_version()}: C++ Header Library
Storm features Typhoon, the high-speed, thread-safe C++ RNG engine that fuels Fortuna.
Engineered with hardware-based entropy and seeding, Typhoon guarantees that every random value generated is consistent, reliable, and free from unwanted bias, even in highly parallel environments.
Storm is ideal for demanding scientific simulation and research tasks, delivering a robust suite of high-speed, high-quality distribution algorithms.
For technical details visit [Storm Documentation](https://github.com/BrokenShell/Storm/blob/main/README.md).
""".strip()


@mcp.tool()
def dice(rolls: SampleSize, sides: Polyhedron) -> int:
    """
    Roll a specified number of dice and return their summed total.

    Simulates rolling 'rolls' dice, each with a fixed number of sides provided by 'sides'.
    The number of dice must be between 1 and 100, and 'sides' must be one of the standard
    values: 2, 4, 6, 8, 10, 12, 20, 30, or 100.

    @param rolls: Number of dice to roll (1 <= rolls <= 100).
    @param sides: Number of sides per die; allowed values are 2, 4, 6, 8, 10, 12, 20, 30, or 100.
    @return: The total sum of the dice rolls.
    """
    return Fortuna.dice(rolls, sides)


@mcp.tool()
def random_range(start: Integer, stop: Integer, step: Integer) -> int:
    """
    Return a random integer selected from a sequence defined by a range.

    Constructs a sequence analogous to Python's range(start, stop, step) and selects a random
    element uniformly from that sequence. The parameters 'start', 'stop', and 'step' must be within
    the integer bounds of -9223372036854775807 to 9223372036854775807. 'step' must be non-zero to
    ensure the range contains at least one element.

    @param start: Starting value of the range (inclusive; -9223372036854775807 <= start <= 9223372036854775807).
    @param stop: Ending value of the range (exclusive; -9223372036854775807 <= stop <= 9223372036854775807).
    @param step: Increment between values; must be non-zero (-9223372036854775807 <= step <= 9223372036854775807).
    @return: A random integer from the defined range.
    """
    return Fortuna.random_range(start, stop, step)


@mcp.tool()
def random_float(lower_limit: Float, upper_bound: Float) -> float:
    """
    Produce a random float uniformly distributed within a specified interval.

    Generates a random float in the half-open interval [lower_limit, upper_bound).
    Both 'lower_limit' and 'upper_bound' must lie within the float bounds of
    -1.7976931348623157e+308 to 1.7976931348623157e+308, and lower_limit must be strictly less than upper_bound.

    @param lower_limit: Inclusive lower bound (-1.7976931348623157e+308 <= lower_limit < upper_bound).
    @param upper_bound: Exclusive upper bound (lower_limit < upper_bound <= 1.7976931348623157e+308).
    @return: A random float from the specified interval.
    """
    return Fortuna.random_float(lower_limit, upper_bound)


if __name__ == "__main__":
    print(f"Starting FortunaMCP Lite Server {version}")
    mcp.run(transport="sse")
