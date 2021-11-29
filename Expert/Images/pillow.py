from PIL import Image

mac = Image.open('example.jpg')
# print(type(mac))
# mac.show()

print(mac.size)
print(mac.filename)
print(mac.format_description)

# Cropping image
mac2 = mac.crop((0, 0, 100, 100))
# mac2.show()

pencils = Image.open('pencils.jpg')
x, y, w, h = 0, 0, 1950/3, 1300/10
pencils2 = pencils.crop((x, y, w, h))
# pencils2.show()

# Pasting image
computer = mac.crop((1993/2-200, 800, 1993/2+200, 1257))
mac.paste(im=computer, box=(0, 0))
# mac.show()

# Resize image
mac_resize = mac.resize((3000,500))
# mac_resize.show()

# Rotate
mac_rotate = mac.rotate(90)
# mac_rotate.show()

# Transparency
red = Image.open('red_color.jpg')
blue = Image.open('blue_color.png')
layered_color = blue
red.putalpha(128)
blue.putalpha(128)
# red.show()
layered_color.paste(im=red, box=(0, 0), mask=red)
# layered_color.show()

# Save
layered_color.save('purple.png')
