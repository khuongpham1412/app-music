from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk, Image, ImageDraw, ImageOps
from io import BytesIO


class Radius():

    def __init__(self, url):
        root = Tk()
        # url = "https://scontent.fsgn8-3.fna.fbcdn.net/v/t1.6435-9/110317078_108873884247194_8632694263271216467_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=CYkmKjjJ3K8AX8Z-gb1&_nc_ht=scontent.fsgn8-3.fna&oh=00_AfD_bZk2d07vAhFPpfwLsst7J0AXCpZnB8e56o2Qe_QHIA&oe=6476F918"
        image_bytes = urlopen(url).read()

        image = Image.open(BytesIO(image_bytes))
        img_width, img_height = image.size

        # Tính đường kính của hình tròn
        diameter = min(img_width, img_height)

        # Tạo mask hình tròn
        mask = Image.new('L', (diameter, diameter), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, diameter, diameter), fill=255)

        # Crop hình ảnh bằng mask hình tròn
        img = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
        img.putalpha(mask)

        # Resize hình ảnh
        img = img.resize((300, 300), Image.ANTIALIAS)

        photo = ImageTk.PhotoImage(img)

        # label = Label(root, image=photo)
        # label.pack()

        # root.mainloop()
