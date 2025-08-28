# FortunaMCP Lite Server
[![Verified on MseeP](https://mseep.ai/badge.svg)](https://mseep.ai/app/72dda374-2f5b-4be8-9f81-33b9b8e6e0ff)

FortunaMCP is an advanced MCP server dedicated to generating high-quality random values. It leverages the Fortuna C-extension, which is directly powered by Storm—a robust, thread-safe C++ RNG engine optimized for high-speed, hardware-based entropy. FortunaMCP provides dependable randomness for a wide range of AI applications.

Large language models excel at natural language processing but rely on deterministic algorithms that fall short when true unpredictability is required. In contrast, FortunaMCP delivers genuine randomness. This capability makes it indispensable for scenarios where unbiased, unpredictable outcomes are critical, and where LLM approximations (hallucinations) simply won’t suffice.

[FortunaMCP](https://github.com/siliconsociety/FortunaMCP) is perfectly suited for tasks like Monte Carlo simulations, complex system modeling and analysis, and interactive game mechanics. It is not intended for blockchain, security or encryption oriented tasks.

### Credits

- **Developer:** Robert Sharp – creator and maintainer of Fortuna, Storm, and FortunaMCP server.
- **Host:** [Silicon Society](https://siliconsociety.org) – proudly hosting the FortunaMCP server and supporting its mission of delivering world-class random value generation for AI Agents. Silicon Society is building the future of learning, at scale. AI-powered job shadowing that brings learning to where work happens. Follow professionals in action with personalized guidance that adapts to your goals. Sign up for the [waitlist](https://docs.google.com/forms/d/e/1FAIpQLSdMjNkgbOpo-iG53cscOfBqu6CD2G-1J9ukkxYGkVL-7T1tPg/viewform?usp=header).

## Tools Overview

### Dice
- **Description:** Simulates rolling a specified number of dice and returns their summed total. Supports standard RPG-style dice with sides {2, 4, 6, 8, 10, 12, 20, 30, 100}.
- **Use Cases:** Perfect for role-playing games, board games, or simulations where dice mechanics are essential.
- **Trigger:** "Roll three six-sided dice" or "Roll 3d6"
- **Call:** `Fortuna.dice(rolls=3, sides=6)`

### Random Range
- **Description:** Returns a random integer selected from a sequence defined by a custom range. Parameters are bounded by the integer limits (-9223372036854775807 to 9223372036854775807) and the step must be non-zero.
- **Use Cases:** Ideal for simulations and sampling from custom intervals where non-standard steps or intervals are required.
- **Trigger:** "Choose a number from 10 to 100 in steps of 5"
- **Call:** `Fortuna.random_range(start=10, stop=100, step=5)`

### Random Float
- **Description:** Produces a uniformly distributed random float within the half-open interval `[lower_limit, upper_bound)`. Both bounds are within the float limits of -1.7976931348623157e+308 to 1.7976931348623157e+308.
- **Use Cases:** Used in simulations, Monte Carlo methods, or any scenario requiring continuous uniform randomness.
- **Trigger:** "Generate a random float between 0.0 and 1.0"
- **Call:** `Fortuna.random_float(lower_limit=0.0, upper_bound=1.0)`
