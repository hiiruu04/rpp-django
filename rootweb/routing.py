from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from ULB.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    'websocket': 
    AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})

channel_routing = {}