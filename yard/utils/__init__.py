import base64
import requests


def get_image_data(url):
    return bytes.decode(base64.b64encode(requests.get(url).content))