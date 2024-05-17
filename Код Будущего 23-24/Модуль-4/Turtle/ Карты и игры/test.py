#!/usr/bin/env python3
# coding:utf-8
from io import BytesIO
import requests
from PIL import Image
from turtle import Screen, bgpic, done

lonlat = "14.204317,68.149046"
z = 15
url = f'https://static-maps.yandex.ru/v1?ll={lonlat}&z={z}&apikey=f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'
response = requests.get(url)
im = Image.open(BytesIO(response.content))
im.save("football.png")
Screen().setup(width=640, height=480)
bgpic("football.png")
done()
