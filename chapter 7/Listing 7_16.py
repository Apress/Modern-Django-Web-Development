#Listing 7_16: NinjaAPI object
from ninja import NinjaAPI

api = NinjaAPI()

@api.get("/hello")
def test(request):
    return {'message': 'Hello World!'}
