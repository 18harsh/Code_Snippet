import os
print(os.path.join('folder1','folder2','folder3','sample.png'))#folder1\folder2\folder3\sample.png

print(os.sep) #\

print(os.getcwd())#C:\Users\harsh\Desktop\code\python\OS_file  (current file location)

os.chdir("C:\\Users\\harsh\\Desktop\\code\\python") #(change root directory)
print(os.getcwd())

print(os.path.abspath('delete.txt'))#C:\Users\harsh\Desktop\code\python\delete.txt

print(os.path.abspath('..\\..\\delete.txt'))#C:\Users\harsh\Desktop\delete.txt

print(os.path.isabs('..\\..\\delete.txt'))

print(os.path.relpath("C:\\Users\\harsh\\Desktop\\code\\python"))

print(os.path.dirname("c:\\user\\harsh\\code")) #c:\user\harsh

print(os.path.basename("C:\\Users\\harsh\\Desktop\\code\\python\\delete.txt")) #delete.txt

print(os.path.exists("C:\\Users\\harsh\\Desktop\\code\\python\\delete.txt")) #True

print(os.path.isfile("c:\\user\\harsh\\code")) #False

print(os.path.getsize('C:\\Users\\harsh\\Desktop\\code\\python\\delete.txt'))

print(os.listdir('c:\\'))

totalsize=0
for filename in os.listdir('C:\\Users\\harsh\\Desktop\\code\\python\\'):
	if not os.path.isfile(os.path.join("C:\\Users\\harsh\\Desktop\\code\\python\\",filename)):
		continue
	totalsize = totalsize+os.path.getsize(os.path.join("C:\\Users\\harsh\\Desktop\\code\\python\\",filename))		
print(totalsize)	

# print(os.makedirs('C:\\Users\\harsh\\Desktop\\create\\dell'))


# os.unlink('C:\\Users\\harsh\\Desktop\\code\\python\\delete.txt')

os.walk()

#os.rmdir()


#import shutil  #(copy,move,rename files)
#
#shutil.rmtree('C:\\Users\\harsh\\Desktop\\create')
#
#import sen2trash  #(send files to trash)
#send2trash.send2trash('C:\\Users\\harsh\\Desktop\\code\\python\\delete.txt')
