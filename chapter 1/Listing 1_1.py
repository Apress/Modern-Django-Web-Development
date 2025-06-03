#Listing 1_1 : WSGI Hello World
def wsgiapp(environ, start_response):
    """Basic WSGI application object"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ['Hello world!\n']