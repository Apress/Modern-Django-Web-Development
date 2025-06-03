#Listing 1_3: Hello World WSGI
from wsgiref.simple_server import make_server

def wsgiapp(environ, start_response):
    host=environ.get('HTTP_HOST')
    start_response("200 OK", [("Content-type", "text/html")])
    ret = [("<h2>Hello World App on WSGI Server Running at :{}</h2>".format((host)).encode("utf-8"))]
    return ret

server = make_server('localhost', 8000, wsgiapp)
server.serve_forever()