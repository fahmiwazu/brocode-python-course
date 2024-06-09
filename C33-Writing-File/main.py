############ writing file in python
text = "YOOOOOOOOO \nThis is some text\nhave a good day\n"
# text = "this text was overwritten"

with open('test.txt','w') as file:
    file.write(text)

text = "have a nice day"
with open('test.txt','a') as file:
    file.write(text)