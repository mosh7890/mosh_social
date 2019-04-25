from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import OriginValidator
from decouple import config, Csv

application = ProtocolTypeRouter({
    "websocket": OriginValidator(
        URLRouter([]),
        [config('CHANNELS_HOSTS', cast=Csv(), default=['*'])],
    ),
})
