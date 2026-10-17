from PIL import Image


img = Image.open("car.gif")


img_resized = img.resize((50,25))


img_resized.save("car_chinh_size.gif")