#Listing 1_6: ASGI Hello World
import uvicorn


async def app(scope, receive, send):
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/html'],
        ],
    })


    await send({
        'type': 'http.response.body',
        'body': b'<h2>Hello World App on ASGI Server</h2>',
    })


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")
