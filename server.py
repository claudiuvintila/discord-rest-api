from asyncio import gather, get_event_loop
from logging import basicConfig, INFO
from discord.ext.commands import Bot
from aiohttp.web import AppRunner, Application, TCPSite

from api import routes
import config

basicConfig(level=INFO)


async def run_bot():

    app = Application()
    app.add_routes(routes)

    runner = AppRunner(app)
    await runner.setup()
    site = TCPSite(runner, config.HOST, config.PORT)
    await site.start()

    bot = Bot(command_prefix="$")
    app['bot'] = bot

    try:
        await bot.start(config.DISCORD_TOKEN)

    except:
        bot.close(),
        raise

    finally:
        await runner.cleanup()

if __name__ == '__main__':
    loop = get_event_loop()
    loop.run_until_complete(run_bot())
