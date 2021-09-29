from PIL import Image, ImageFilter

before = Image.open("DkIT_corporate_logo_mockup.jpg")
after = before.filter(ImageFilter.BLUR)
after.save("DkiT_blurred.jpg")