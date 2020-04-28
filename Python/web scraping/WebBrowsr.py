import webbrowser,sys,pyperclip
# webbrowser.open('https://automatetheboringstuff.com/chapter11/')
print(sys.argv) 
if len(sys.argv)>1:
	address = ''.join(sys.argv[1:])
else:
	address = pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/"+address)