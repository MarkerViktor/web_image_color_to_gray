import io

from aiohttp import web
from PIL import Image


async def index(_) -> web.StreamResponse:
    return web.FileResponse('index.html')


async def convert(request: web.Request) -> web.Response:
    post = await request.post()
    input_image_file = post['image'].file
    image = Image.open(input_image_file).convert('L')

    output_image_file = io.BytesIO()
    image.save(output_image_file, 'jpeg')

    return web.Response(body=output_image_file.getvalue(), content_type='image/jpeg')


def main():
    app = web.Application()
    app.add_routes([
        web.get('/', index),
        web.post('/convert', convert)
    ])
    web.run_app(app, port=80)


if __name__ == '__main__':
    main()
