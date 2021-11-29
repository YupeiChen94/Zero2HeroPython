from PIL import Image

# word_matrix = Image.open('word_matrix.png')
# new_word_matrix = word_matrix.convert('RGB')
# new_word_matrix.save('new_word_matrix.jpg')
#
# mask = Image.open('mask.png')
# new_mask = mask.convert('RGB')
# new_mask.save('new_mask.jpg')

word_matrix = Image.open('new_word_matrix.jpg')
mask = Image.open('new_mask.jpg')
mask.putalpha(128)

# print(word_matrix.size)
mask = mask.resize((1015, 559))
# print(mask.size)

answer = word_matrix
answer.paste(im=mask, box=(0, 0), mask=mask)
answer.show()

# GREAT WORK WITH IMAGES YOU ARE THE BEST
