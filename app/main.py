import os
from pathlib import Path

from typing import Annotated, Literal, TypeAlias

import Fortuna
import markdown
from pydantic import Field
from mcp.server.fastmcp import FastMCP
from starlette.responses import HTMLResponse, FileResponse
from starlette.routing import Route


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


@mcp.tool()
def triangular(lower_limit: Float, upper_limit: Float, mode: Float) -> float:
    """
    Generate a random float from a triangular distribution.

    The distribution is defined by a lower limit, an upper limit, and a mode.
    All parameters must lie within the float bounds of -1.7976931348623157e+308 to 1.7976931348623157e+308,
    and must satisfy lower_limit <= mode <= upper_limit.

    @param lower_limit: Minimum possible value (-1.7976931348623157e+308 <= lower_limit).
    @param upper_limit: Maximum possible value (upper_limit <= 1.7976931348623157e+308).
    @param mode: Most likely value; must satisfy lower_limit <= mode <= upper_limit.
    @return: A random float sampled from the triangular distribution.
    """
    return Fortuna.triangular(lower_limit, upper_limit, mode)


@mcp.tool()
def bernoulli_variate(ratio_of_truth: CanonicalFloat) -> bool:
    """
    Perform a Bernoulli trial returning a boolean outcome.

    Executes a single trial where the chance of success is given by 'ratio_of_truth',
    which must be between 0 and 1 (inclusive).

    @param ratio_of_truth: Success probability (0 <= ratio_of_truth <= 1).
    @return: True with probability equal to ratio_of_truth, otherwise False.
    """
    return Fortuna.bernoulli_variate(ratio_of_truth) == 1


@mcp.tool()
def binomial_variate(number_of_trials: PositiveInteger, probability: CanonicalFloat) -> int:
    """
    Generate a random count of successes in a fixed number of Bernoulli trials.

    Models a binomial distribution where each trial has a success probability given by 'probability'.
    'number_of_trials' must be between 1 and 9223372036854775807, and 'probability' must be in [0, 1].

    @param number_of_trials: Total number of trials (1 <= number_of_trials <= 9223372036854775807).
    @param probability: Success probability per trial (0 <= probability <= 1).
    @return: Number of successes achieved.
    """
    return Fortuna.binomial_variate(number_of_trials, probability)


@mcp.tool()
def negative_binomial_variate(number_of_trials: PositiveInteger,
                              probability: CanonicalFloat) -> int:
    """
    Calculate the number of failures before achieving a target number of successes.

    Uses a negative binomial model where 'number_of_trials' is the target number of successes
    (minimum 1, maximum 9223372036854775807) and 'probability' is the chance of success per trial (0 <= probability <= 1).

    @param number_of_trials: Target successes (1 <= number_of_trials <= 9223372036854775807).
    @param probability: Success probability per trial (0 <= probability <= 1).
    @return: Count of failures before reaching the target successes.
    """
    return Fortuna.negative_binomial_variate(number_of_trials, probability)


@mcp.tool()
def geometric_variate(probability: Annotated[float, Field(gt=0, le=1)]) -> int:
    """
    Determine the number of failures before the first success in a sequence of trials.

    Implements a geometric distribution where 'probability' is the chance of success on each trial.
    The probability must be greater than 0 and no more than 1.

    @param probability: Success probability (0 < probability <= 1).
    @return: Number of failures before the first success.
    """
    return Fortuna.geometric_variate(probability)


@mcp.tool()
def poisson_variate(mean: PositiveFloat) -> int:
    """
    Generate a random integer from a Poisson distribution.

    The Poisson distribution is characterized by the expected number of occurrences (λ).
    'mean' must be greater than 0 and no more than 1.7976931348623157e+308.

    @param mean: Expected occurrences (λ > 0 and ≤ 1.7976931348623157e+308).
    @return: A random integer from the Poisson distribution.
    """
    return Fortuna.poisson_variate(mean)


@mcp.tool()
def beta_variate(alpha: PositiveFloat, beta: PositiveFloat) -> float:
    """
    Generate a random float from a beta distribution on the interval [0, 1].

    The beta distribution is parameterized by two positive shape parameters.
    Both 'alpha' and 'beta' must be greater than 0 and no more than 1.7976931348623157e+308.

    @param alpha: First shape parameter (alpha > 0 and ≤ 1.7976931348623157e+308).
    @param beta: Second shape parameter (beta > 0 and ≤ 1.7976931348623157e+308).
    @return: A random float between 0 and 1 from the beta distribution.
    """
    return Fortuna.beta_variate(alpha, beta)


@mcp.tool()
def pareto_variate(alpha: PositiveFloat) -> float:
    """
    Generate a random float from a Pareto distribution.

    Models heavy-tailed distributions. The 'alpha' parameter is the shape factor,
    must be greater than 0 and no more than 1.7976931348623157e+308.
    The output is a float greater than or equal to 1.

    @param alpha: Shape parameter (alpha > 0 and ≤ 1.7976931348623157e+308).
    @return: A float (>= 1) sampled from the Pareto distribution.
    """
    return Fortuna.pareto_variate(alpha)


@mcp.tool()
def vonmises_variate(
    mu: Float,
    kappa: Annotated[float, Field(ge=0, le=Fortuna.max_float())],
) -> float:
    """
    Produce a random angle based on the Von Mises distribution.

    Useful for modeling circular data such as angles, this distribution wraps around at 2π.
    'mu' must be within the float bounds of -1.7976931348623157e+308 to 1.7976931348623157e+308,
    and 'kappa' must be between 0 and 1.7976931348623157e+308.

    @param mu: Mean angle in radians (-1.7976931348623157e+308 <= mu <= 1.7976931348623157e+308).
    @param kappa: Concentration parameter (kappa >= 0 and ≤ 1.7976931348623157e+308).
    @return: A random angle in radians from the Von Mises distribution.
    """
    return Fortuna.vonmises_variate(mu, kappa)


@mcp.tool()
def exponential_variate(lambda_rate: PositiveFloat) -> float:
    """
    Generate a random float from an exponential distribution.

    The exponential distribution is defined by its rate parameter 'lambda_rate',
    which must be greater than 0 and no more than 1.7976931348623157e+308.

    @param lambda_rate: Rate parameter (λ > 0 and ≤ 1.7976931348623157e+308).
    @return: A float representing time until the next event.
    """
    return Fortuna.exponential_variate(lambda_rate)


@mcp.tool()
def gamma_variate(shape: PositiveFloat, scale: PositiveFloat) -> float:
    """
    Generate a random float from a gamma distribution.

    The gamma distribution is characterized by a shape parameter and a scale parameter.
    Both must be greater than 0 and no more than 1.7976931348623157e+308.

    @param shape: Shape parameter (k > 0 and ≤ 1.7976931348623157e+308).
    @param scale: Scale parameter (θ > 0 and ≤ 1.7976931348623157e+308).
    @return: A random float from the gamma distribution.
    """
    return Fortuna.gamma_variate(shape, scale)


@mcp.tool()
def weibull_variate(shape: PositiveFloat, scale: PositiveFloat) -> float:
    """
    Generate a random float from a Weibull distribution.

    The Weibull distribution uses a shape and a scale parameter.
    Both must be greater than 0 and no more than 1.7976931348623157e+308,
    modeling the time until a failure or event.

    @param shape: Shape parameter (k > 0 and ≤ 1.7976931348623157e+308).
    @param scale: Scale parameter (λ > 0 and ≤ 1.7976931348623157e+308).
    @return: A random float representing time until a failure or event.
    """
    return Fortuna.weibull_variate(shape, scale)


@mcp.tool()
def normal_variate(mean: Float, std_dev: PositiveFloat) -> float:
    """
    Generate a random float from a normal (Gaussian) distribution.

    The normal distribution is defined by a mean and a standard deviation.
    'mean' must lie within -1.7976931348623157e+308 to 1.7976931348623157e+308,
    and 'std_dev' must be greater than 0 and no more than 1.7976931348623157e+308.

    @param mean: Mean value (μ) within [-1.7976931348623157e+308, 1.7976931348623157e+308].
    @param std_dev: Standard deviation (σ > 0 and ≤ 1.7976931348623157e+308).
    @return: A random float from the normal distribution.
    """
    return Fortuna.normal_variate(mean, std_dev)


@mcp.tool()
def log_normal_variate(log_mean: Float, log_deviation: PositiveFloat) -> float:
    """
    Generate a random float from a log-normal distribution.

    Derived from a normally distributed variable, the log-normal distribution uses 'log_mean'
    as the mean and 'log_deviation' as the standard deviation of the underlying normal distribution.
    'log_mean' must be within [-1.7976931348623157e+308, 1.7976931348623157e+308] and
    'log_deviation' must be greater than 0 and no more than 1.7976931348623157e+308.

    @param log_mean: Mean of the underlying normal distribution.
    @param log_deviation: Standard deviation of the underlying normal (log_deviation > 0 and ≤ 1.7976931348623157e+308).
    @return: A positive float sampled from the log-normal distribution.
    """
    return Fortuna.log_normal_variate(log_mean, log_deviation)


@mcp.tool()
def extreme_value_variate(location: Float, scale: PositiveFloat) -> float:
    """
    Generate a random float from an extreme value (Gumbel) distribution.

    Defined by a location and a scale parameter, the Gumbel distribution models the distribution
    of the maximum (or minimum) of a set of samples. 'location' must lie within
    [-1.7976931348623157e+308, 1.7976931348623157e+308] and 'scale' must be greater than 0 and
    no more than 1.7976931348623157e+308.

    @param location: Location parameter (μ) within [-1.7976931348623157e+308, 1.7976931348623157e+308].
    @param scale: Scale parameter (β > 0 and ≤ 1.7976931348623157e+308).
    @return: A random float from the Gumbel distribution.
    """
    return Fortuna.extreme_value_variate(location, scale)


@mcp.tool()
def chi_squared_variate(degrees_of_freedom: PositiveFloat) -> float:
    """
    Generate a random float from a chi-squared distribution.

    The chi-squared distribution is determined by its degrees of freedom, which must be
    greater than 0 and no more than 1.7976931348623157e+308.

    @param degrees_of_freedom: Degrees of freedom (df > 0 and ≤ 1.7976931348623157e+308).
    @return: A random float sampled from the chi-squared distribution.
    """
    return Fortuna.chi_squared_variate(degrees_of_freedom)


@mcp.tool()
def cauchy_variate(location: Float, scale: PositiveFloat) -> float:
    """
    Generate a random float from a Cauchy distribution.

    Defined by a central location and a scale parameter, the Cauchy distribution is known
    for its heavy tails. 'location' must lie within [-1.7976931348623157e+308, 1.7976931348623157e+308],
    and 'scale' must be greater than 0 and no more than 1.7976931348623157e+308.

    @param location: Central location parameter (x₀) within [-1.7976931348623157e+308, 1.7976931348623157e+308].
    @param scale: Scale parameter (γ > 0 and ≤ 1.7976931348623157e+308).
    @return: A random float from the Cauchy distribution.
    """
    return Fortuna.cauchy_variate(location, scale)


@mcp.tool()
def fisher_f_variate(degrees_of_freedom_1: PositiveFloat,
                     degrees_of_freedom_2: PositiveFloat) -> float:
    """
    Generate a random float from a Fisher F distribution.

    The Fisher F distribution is parameterized by two sets of degrees of freedom,
    both of which must be greater than 0 and no more than 1.7976931348623157e+308.

    @param degrees_of_freedom_1: Numerator degrees of freedom (df₁ > 0 and ≤ 1.7976931348623157e+308).
    @param degrees_of_freedom_2: Denominator degrees of freedom (df₂ > 0 and ≤ 1.7976931348623157e+308).
    @return: A random float sampled from the Fisher F distribution.
    """
    return Fortuna.fisher_f_variate(degrees_of_freedom_1, degrees_of_freedom_2)


@mcp.tool()
def student_t_variate(degrees_of_freedom: PositiveFloat) -> float:
    """
    Generate a random float from a Student’s t-distribution.

    The Student’s t-distribution is determined by its degrees of freedom, which must be
    greater than 0 and no more than 1.7976931348623157e+308.

    @param degrees_of_freedom: Degrees of freedom (df > 0 and ≤ 1.7976931348623157e+308).
    @return: A random float sampled from the Student’s t-distribution.
    """
    return Fortuna.student_t_variate(degrees_of_freedom)


async def root(request):
    """Serve the README as HTML at the root path"""
    readme = Path("README.md").read_text()
    html_content = markdown.markdown(readme, extensions=['tables', 'fenced_code'])
    #  🎲
    html_response = f"""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FortunaMCP Server</title>
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
    print(f"Starting Fortuna MCP Server {version}")
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
