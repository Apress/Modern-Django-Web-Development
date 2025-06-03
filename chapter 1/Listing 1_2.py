#Listing 1_2: WSGI demo_app
from wsgiref.simple_server import make_server, demo_app
server = make_server('', 8000, demo_app)
server.serve_forever()