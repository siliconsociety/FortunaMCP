import os
from pathlib import Path

from typing import Annotated, Literal, TypeAlias

import Fortuna
import markdown
from pydantic import Field
from mcp.server.fastmcp import FastMCP
from starlette.responses import HTMLResponse, FileResponse
from starlette.routing import Route


version = "0.1.3"
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


async def root(request):
    """Serve the README as HTML at the root path"""
    readme = Path("README.md").read_text()
    html_content = markdown.markdown(readme, extensions=['tables', 'fenced_code'])
    html_response = f"""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FortunaMCP Lite Server</title>
    <style>
        body {{
            font-family: 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        main {{
            background: white;
            padding: 20px 30px 40px 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .version {{
            font-size: 0.8em;
            float: right;
        }}
        h1 {{ margin-top: 0; }}
        h1, h2, h3 {{ color: #2c3e50; }}
        h3 {{ margin-bottom: 0; }}
        ul {{ margin-top: 0; }}
        code {{
            background: #f8f9fa;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: 'Monaco', 'Consolas', monospace;
            color: #666;
        }}
        pre {{
            background: #f8f9fa;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }}
        a {{ color: #3498db; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        .badge {{
            display: inline-block;
            margin-bottom: 20px;
        }}
    </style>
</head>
<body>
    <main>
        <span class="version">v{version}</span>
        {html_content}
    </main>
</body>
</html>
""".strip()
    return HTMLResponse(content=html_response)


async def favicon(request):
    favicon_path = Path("static/favicon.ico")
    return FileResponse(str(favicon_path))


if __name__ == "__main__":
    print(f"Starting Fortuna MCP Lite Server {version}")
    _sse_app = mcp.sse_app


    def sse_app(request):
        app = _sse_app()
        root_route = Route("/", root, methods=["GET"])
        favicon_route = Route("/favicon.ico", favicon, methods=["GET"])
        app.router.routes.insert(0, root_route)
        app.router.routes.insert(1, favicon_route)
        return app


    mcp.sse_app = sse_app
    mcp.run(transport="sse")
