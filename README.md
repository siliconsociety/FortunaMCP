# FortunaMCP Server

FortunaMCP is an advanced MCP server dedicated to generating high-quality random values. It leverages the Fortuna C-extension, which is directly powered by Storm—a robust, thread-safe C++ RNG engine optimized for high-speed, hardware-based entropy. FortunaMCP provides dependable randomness for a wide range of AI applications.

Large language models excel at natural language processing but rely on deterministic algorithms that fall short when true unpredictability is required. In contrast, FortunaMCP delivers genuine randomness. This capability makes it indispensable for scenarios where unbiased, unpredictable outcomes are critical, and where LLM approximations (hallucinations) simply won’t suffice.

FortunaMCP is perfectly suited for tasks like Monte Carlo simulations, complex system modeling and analysis, and interactive game mechanics. It is not intended for blockchain, security or encryption oriented tasks.

### Credits

- **Developer:** Robert Sharp – creator and maintainer of Fortuna, Storm, and FortunaMCP server.
- **Host:** [Silicon Society](https://siliconsociety.org) – proudly hosting the FortunaMCP server and supporting its mission of delivering world-class random value generation for AI Agents. Silicon Society is building the future of learning, at scale. AI-powered job shadowing that brings learning to where work happens. Follow professionals in action with personalized guidance that adapts to your goals. Sign up for the [waitlist](https://docs.google.com/forms/d/e/1FAIpQLSdMjNkgbOpo-iG53cscOfBqu6CD2G-1J9ukkxYGkVL-7T1tPg/viewform?usp=header).

### Reference Deployment
- FortunaMCP Lite https://fortuna-mcp.siliconsociety.org/sse
- Tools
  - Dice
  - Random Range
  - Random Float

## Tools Overview

### Dice
- **Description:** Simulates rolling a specified number of dice and returns their summed total. Supports standard RPG-style dice with sides {2, 4, 6, 8, 10, 12, 20, 30, 100}.
- **Use Cases:** Perfect for role-playing games, board games, or simulations where dice mechanics are essential.
- **Example:**
  - **Trigger:** "Roll three six-sided dice" or "Roll 3d6"
  - **Call:** `Fortuna.dice(rolls=3, sides=6)`

### Random Range
- **Description:** Returns a random integer selected from a sequence defined by a custom range. Parameters are bounded by the integer limits (-9223372036854775807 to 9223372036854775807) and the step must be non-zero.
- **Use Cases:** Ideal for simulations and sampling from custom intervals where non-standard steps or intervals are required.
- **Example:**
  - **Trigger:** "Choose a number from 10 to 100 in steps of 5"
  - **Call:** `Fortuna.random_range(start=10, stop=100, step=5)`

### Random Float
- **Description:** Produces a uniformly distributed random float within the half-open interval `[lower_limit, upper_bound)`. Both bounds are within the float limits of -1.7976931348623157e+308 to 1.7976931348623157e+308.
- **Use Cases:** Used in simulations, Monte Carlo methods, or any scenario requiring continuous uniform randomness.
- **Example:**
  - **Trigger:** "Generate a random float between 0.0 and 1.0"
  - **Call:** `Fortuna.random_float(lower_limit=0.0, upper_bound=1.0)`

### Triangular Variate
- **Description:** Samples a random float from a triangular distribution defined by a lower limit, an upper limit, and a mode.
- **Use Cases:** Excellent for project management estimates, risk analysis, or any scenario where outcomes are most likely around a central value.
- **Example:**
  - **Trigger:** "Simulate an outcome with a most likely value of 50, ranging from 10 to 100"
  - **Call:** `Fortuna.triangular(lower_limit=10.0, upper_limit=100.0, mode=50.0)`

### Bernoulli Variate
- **Description:** Executes a Bernoulli trial returning a boolean outcome based on the provided success probability.
- **Use Cases:** Useful for binary decision-making, such as simulating coin tosses, on/off events, or success/failure outcomes.
- **Example:**
  - **Trigger:** "Simulate a coin toss with a 70% chance of heads"
  - **Call:** `Fortuna.bernoulli_variate(ratio_of_truth=0.7)`

### Binomial Variate
- **Description:** Returns the number of successes in a fixed number of Bernoulli trials, modeling a binomial distribution.
- **Use Cases:** Valuable for statistical simulations, quality control processes, and experiments where you need to determine success rates.
- **Example:**
  - **Trigger:** "Determine the number of heads in 20 coin flips with a 50% chance each"
  - **Call:** `Fortuna.binomial_variate(number_of_trials=20, probability=0.5)`

### Negative Binomial Variate
- **Description:** Calculates the number of failures before achieving a target number of successes in a series of Bernoulli trials.
- **Use Cases:** Applied in reliability engineering, risk assessment, and scenarios where tracking failures before a success is crucial.
- **Example:**
  - **Trigger:** "Calculate failures before 5 successes with a 40% success rate per trial"
  - **Call:** `Fortuna.negative_binomial_variate(number_of_trials=5, probability=0.4)`

### Geometric Variate
- **Description:** Determines the number of failures before the first success, following a geometric distribution.
- **Use Cases:** Ideal for modeling waiting times and first-occurrence events in processes such as customer acquisition or quality testing.
- **Example:**
  - **Trigger:** "How many failures before the first success with a 25% success rate?"
  - **Call:** `Fortuna.geometric_variate(probability=0.25)`

### Poisson Variate
- **Description:** Generates a random integer from a Poisson distribution, characterized by the expected number of occurrences (λ).
- **Use Cases:** Essential for modeling rare events over time, such as system failures, network traffic, or customer arrivals.
- **Example:**
  - **Trigger:** "Simulate the number of events in an interval with an average of 4 events"
  - **Call:** `Fortuna.poisson_variate(mean=4.0)`

### Beta Variate
- **Description:** Draws a random float from a beta distribution on the interval [0, 1] using two positive shape parameters.
- **Use Cases:** Widely used in Bayesian statistics, modeling proportions, and any scenario where probabilities need to be simulated.
- **Example:**
  - **Trigger:** "Generate a random probability with shape parameters 2 and 5"
  - **Call:** `Fortuna.beta_variate(alpha=2.0, beta=5.0)`

### Pareto Variate
- **Description:** Returns a random float from a Pareto distribution, ideal for modeling heavy-tailed phenomena. The output is always greater than or equal to 1.
- **Use Cases:** Useful in economics, insurance, and risk management where power-law behaviors are observed.
- **Example:**
  - **Trigger:** "Generate a Pareto-distributed value with shape parameter 1.5"
  - **Call:** `Fortuna.pareto_variate(alpha=1.5)`

### Von Mises Variate
- **Description:** Produces a random angle from a Von Mises distribution, tailored for circular or directional data.
- **Use Cases:** Common in meteorology, navigation, and any application involving angles or periodic phenomena.
- **Example:**
  - **Trigger:** "Generate a random angle with a mean of 0 radians and concentration 1.0"
  - **Call:** `Fortuna.vonmises_variate(mu=0.0, kappa=1.0)`

### Exponential Variate
- **Description:** Generates a random float from an exponential distribution defined by a rate parameter, modeling the time between independent events.
- **Use Cases:** Critical for simulating lifetimes, system failures, and inter-arrival times in queuing models.
- **Example:**
  - **Trigger:** "Simulate time until the next event with a rate of 0.5"
  - **Call:** `Fortuna.exponential_variate(lambda_rate=0.5)`

### Gamma Variate
- **Description:** Returns a random float from a gamma distribution, determined by shape and scale parameters.
- **Use Cases:** Used for modeling waiting times, reliability analysis, and in various continuous processes.
- **Example:**
  - **Trigger:** "Generate a gamma variate with shape 2.0 and scale 3.0"
  - **Call:** `Fortuna.gamma_variate(shape=2.0, scale=3.0)`

### Weibull Variate
- **Description:** Samples a random float from a Weibull distribution, which models the time until a failure or event.
- **Use Cases:** Widely used in survival analysis, reliability engineering, and failure rate estimation.
- **Example:**
  - **Trigger:** "Simulate time until failure with Weibull parameters shape 1.5 and scale 100.0"
  - **Call:** `Fortuna.weibull_variate(shape=1.5, scale=100.0)`

### Normal Variate
- **Description:** Generates a random float from a normal (Gaussian) distribution defined by a mean and a standard deviation.
- **Use Cases:** Fundamental for statistical modeling, quality control, and simulations requiring bell-curve behavior.
- **Example:**
  - **Trigger:** "Generate a normally distributed value with mean 0 and standard deviation 1"
  - **Call:** `Fortuna.normal_variate(mean=0.0, std_dev=1.0)`

### Log-Normal Variate
- **Description:** Draws a random float from a log-normal distribution derived from an underlying normal distribution.
- **Use Cases:** Used in financial modeling, stock price simulations, and scenarios where outcomes are multiplicative.
- **Example:**
  - **Trigger:** "Generate a log-normal variate with log-mean 0 and log-deviation 1"
  - **Call:** `Fortuna.log_normal_variate(log_mean=0.0, log_deviation=1.0)`

### Extreme Value Variate
- **Description:** Samples a random float from an extreme value (Gumbel) distribution, used for modeling maxima or minima.
- **Use Cases:** Suitable for risk assessment, extreme weather predictions, and stress testing in engineering.
- **Example:**
  - **Trigger:** "Simulate an extreme event with location 0 and scale 1.0"
  - **Call:** `Fortuna.extreme_value_variate(location=0.0, scale=1.0)`

### Chi-Squared Variate
- **Description:** Generates a random float from a chi-squared distribution based on the degrees of freedom.
- **Use Cases:** Essential for hypothesis testing, variance estimation, and goodness-of-fit tests.
- **Example:**
  - **Trigger:** "Generate a chi-squared variate with 5 degrees of freedom"
  - **Call:** `Fortuna.chi_squared_variate(degrees_of_freedom=5.0)`

### Cauchy Variate
- **Description:** Returns a random float from a Cauchy distribution, characterized by heavy tails.
- **Use Cases:** Useful in robust statistical analysis, signal processing, and scenarios where outliers are expected.
- **Example:**
  - **Trigger:** "Generate a Cauchy variate with location 0 and scale 1.0"
  - **Call:** `Fortuna.cauchy_variate(location=0.0, scale=1.0)`

### Fisher F Variate
- **Description:** Draws a random float from a Fisher F distribution defined by two sets of degrees of freedom.
- **Use Cases:** Applied in ANOVA testing, variance analysis, and comparing statistical models.
- **Example:**
  - **Trigger:** "Generate a Fisher F variate with degrees of freedom 5 and 10"
  - **Call:** `Fortuna.fisher_f_variate(degrees_of_freedom_1=5.0, degrees_of_freedom_2=10.0)`

### Student’s t Variate
- **Description:** Produces a random float from a Student’s t-distribution based on the specified degrees of freedom.
- **Use Cases:** Integral to small-sample statistical analysis, confidence interval estimation, and hypothesis testing.
- **Example:**
  - **Trigger:** "Generate a Student’s t variate with 10 degrees of freedom"
  - **Call:** `Fortuna.student_t_variate(degrees_of_freedom=10.0)`
