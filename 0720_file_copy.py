file = open('minecraft.jpg','rb')
img = file.read()
file.close()

#print(img)

#圖片檔案複製
file = open('copy.jpg','wb')
file.write(img)
file.close()