# import pygame
# import requests

# pygame.init()
# pygame.mixer.init()

# url = "http://localhost:5000/play-music"

# response = requests.get(url)
# # file = response.content

# # with open("temp.mp3", "wb") as f:
# #     f.write(file)

# # pygame.mixer.music.load("temp.mp3")
# # pygame.mixer.music.play()

# while pygame.mixer.music.get_busy():
#     continue

# pygame.mixer.music.stop()
# pygame.quit()

# import threading
# import tkinter as tk
# from urllib.request import urlopen
# from PIL import ImageTk


# def getImageFromURL(url, controller):
#     print('hai')
#     try:
#         controller.image = ImageTk.PhotoImage(file=urlopen(url))
#         # notify controller that image has been downloaded
#         controller.event_generate("<<ImageLoaded>>")
#     except Exception as e:
#         print(e)


# import pygame
# import requests
# from mutagen.mp3 import MP3

# pygame.init()
# pygame.mixer.init()

# url = "http://localhost:5000/play-music"

# response = requests.get(url)
# file = response.content

# with open("temp.mp3", "wb") as f:
#     f.write(file)

# pygame.mixer.music.load("temp.mp3")
# pygame.mixer.music.play()

# audio = MP3("temp.mp3")
# length = audio.info.length
# print("Length:", length)

# while pygame.mixer.music.get_busy():
#     continue

# pygame.mixer.music.stop()
# pygame.quit()


from PIL import Image, ImageOps
from PIL import Image, ImageDraw

input_path = r"D:\\SGU\\Opensource_Software\\radio-client\\assets\\zing-mp3.png"

# Đọc ảnh vào đối tượng Image
img = Image.open(input_path)

# Lấy kích thước của ảnh
width, height = img.size

# Tính đường kính của hình tròn cần cắt ra
diameter = min(width, height)

# Tạo ảnh mới kích thước bằng đường kính của hình tròn
new_img = Image.new("RGBA", (diameter, diameter), (0, 0, 0, 0))

# Chèn ảnh gốc vào ảnh mới
new_img.paste(img, ((diameter - width) // 2, (diameter - height) // 2))

# Bo tròn ảnh mới
mask = Image.new("L", (diameter, diameter), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, diameter, diameter), fill=500)
new_img.putalpha(mask)

# Lưu ảnh mới
output_path = "output.png"
new_img.save(output_path)
