import qrcode

img = qrcode.make("https://www.youtube.com/watch?v=2Vv-BfVoq4g")
img.save("love.jpg")
