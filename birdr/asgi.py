import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from .consumers import QuizConsumer  # Adjust the import as necessary

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "birdr.settings.production")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("mpg/<str:game_token>", QuizConsumer.as_asgi()),
        ])
    ),
})