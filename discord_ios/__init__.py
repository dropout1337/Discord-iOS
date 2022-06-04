from .identify import identify
from discord.gateway import DiscordWebSocket

DiscordWebSocket.identify = identify
