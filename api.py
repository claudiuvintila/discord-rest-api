# from aiohttp.typedefs import Handler
from aiohttp.web_response import json_response
from aiohttp.web_routedef import RouteTableDef

import config

routes = RouteTableDef()


@routes.get('/invite/create')
async def get_guilds(request):
    client = request.app['bot']
    guild = client.get_guild(config.DISCORD_GUILD)
    link = await guild.text_channels[0].create_invite(max_age=300, max_users=1)
    response = {
        'invite_link': str(link)
    }
    return json_response(response, status=200, content_type='application/json')
