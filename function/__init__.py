import logging

from azure.functions import HttpRequest, Context, HttpResponse, WsgiMiddleware
from app.wsgi import wsgi


main = WsgiMiddleware(wsgi).main
