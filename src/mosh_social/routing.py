from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from decouple import config, Csv

application = ProtocolTypeRouter({
    "websocket": AllowedHostsOriginValidator(
        URLRouter([]),
    ),
})
