# FortunaMCP Use Cases

## Role-Playing Games
Imagine a player interacting with an Agent in an online RPG. The player types "Roll 3d6" into the chat interface. The Agent recognizes the dice notation and immediately forwards the request to FortunaMCP's dice tool. The tool simulates rolling three standard six-sided dice, generating a random sum between 3 and 18. The Agent then returns this sum, which the player uses to determine the outcome of an in-game action—be it an attack, a skill check, or a critical event—adding a layer of genuine unpredictability and fairness to the gameplay.

## Financial Risk Simulation
A financial analyst asks the Agent, "I need to model how many trading days this month will be profitable. Historically, 60% of our trading days are profitable." The Agent recognizes this as a binomial problem—a fixed number of trials with a known success probability. Without the analyst needing to specify the statistical method, the Agent selects FortunaMCP's binomial variate tool, using 20 trials (trading days) and 0.6 probability. The result shows realistic clustering of profitable days, helping the analyst understand cash flow patterns and risk exposure that simple averages would miss.

## Scientific Simulation
A researcher studying radioactive decay tells the Agent, "I need to simulate when the next particle will decay. The half-life is 1.4 hours." The Agent understands that radioactive decay follows an exponential distribution and automatically calculates the appropriate rate parameter from the half-life. Without the researcher needing to know the mathematical relationship, the Agent calls FortunaMCP's exponential variate tool with the correct rate. The generated waiting time reflects the memoryless property of radioactive decay, providing realistic simulation data for the researcher's model.

## Monte Carlo Portfolio Analysis
A portfolio manager asks the Agent, "I need to stress-test our portfolio. Based on historical data, our average monthly return is 8% with typical volatility around 15%. Show me 1000 possible scenarios for next year's performance." The Agent recognizes this requires modeling returns as normally distributed and automatically selects FortunaMCP's normal variate tool with the appropriate parameters. The manager receives realistic return scenarios that capture both the expected performance and the fat-tail risks that could impact the portfolio, enabling sophisticated risk management without requiring statistical expertise.

## A/B Testing Simulation
A product manager tells the Agent, "We're planning to test a new checkout flow. Our current conversion rate is 12%. If we test with 500 users, what kind of results should we expect to see?" The Agent understands this involves independent user decisions and selects FortunaMCP's Bernoulli variate tool to simulate 500 individual conversion outcomes. The realistic simulation shows natural clustering—maybe 15 conversions in the first 100 users, then 8 in the next 100—helping the manager understand that early results might be misleading and plan appropriate test durations.

## Quality Control Modeling
A manufacturing engineer explains to the Agent, "We typically see about 2-3 defects per production batch, but it varies randomly. I need to plan quality control resources for the next 100 batches." The Agent recognizes this as a classic Poisson process—rare events occurring independently over fixed intervals. It automatically selects FortunaMCP's Poisson distribution with the appropriate rate parameter. The simulation reveals realistic patterns: some batches with zero defects, others with 5 or 6, helping the engineer staff inspection teams and plan rework capacity appropriately.

## Clinical Trial Power Analysis
A biostatistician explains, "I'm designing a trial with 30 patients per group. I need to understand what treatment effect sizes we might observe given normal biological variation." The Agent recognizes this involves small-sample statistics where the normal distribution isn't appropriate, and automatically selects FortunaMCP's Student's t distribution with 28 degrees of freedom (30-2 for two-sample comparison). The generated effect sizes account for the additional uncertainty inherent in small samples, helping design a trial with appropriate power while avoiding costly over-enrollment.
