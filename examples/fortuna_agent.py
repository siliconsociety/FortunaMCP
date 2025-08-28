import asyncio

from agents import Agent, Runner
from agents.mcp import MCPServerSse
from agents.model_settings import ModelSettings
from dotenv import load_dotenv


class FortunaAgent:
    load_dotenv()
    # mcp_url = "https://fortuna-mcp.siliconsociety.org/sse"
    mcp_url = "http://localhost/sse"
    model = "gpt-4.1-nano"

    def __init__(self):
        self.mcp_server = MCPServerSse(
            name="FortunaMCP",
            params={"url": self.mcp_url}
        )
        self.agent = None

    async def initialize(self):
        await self.mcp_server.__aenter__()
        self.agent = Agent(
            name="FortunaAgent",
            instructions=(
                "You specialize in random value generation. "
                "When randomness is needed, use the tools provided by FortunaMCP. "
                "When information about FortunaMCP, Fortuna, Storm, Robert Sharp or "
                "Silicon Society is requested use the fortuna_info tool provided by FortunaMCP. "
            ),
            mcp_servers=[self.mcp_server],
            model=self.model,
            model_settings=ModelSettings(tool_choice="auto"),
        )

    async def close(self):
        await self.mcp_server.__aexit__(None, None, None)

    async def run(self, request: str) -> str:
        result = await Runner.run(starting_agent=self.agent, input=request)
        return result.final_output


async def main():
    bot = FortunaAgent()
    await bot.initialize()
    try:
        while True:
            user_input = await asyncio.to_thread(input, "\n>>> ")
            if user_input.lower() in ("", "q", "quit", "exit"):
                break
            bot_reply = await bot.run(request=user_input)
            print(f"\n{bot_reply}")
    finally:
        await bot.close()


if __name__ == "__main__":
    asyncio.run(main())
