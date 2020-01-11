import requests
from io import BytesIO
from PIL import Image

r = requests.get("https://images6.alphacoders.com/101/1012987.jpg")
print("Status:", r.status_code)

image = Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)
path = "./PythonMisc/image." + image.format

try:
    image.save(path, image.format)
except IOError:
    print("Cannot save image.")
