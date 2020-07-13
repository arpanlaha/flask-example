from azure.functions import WsgiMiddleware
from app.wsgi import wsgi

main = WsgiMiddleware(wsgi).main
