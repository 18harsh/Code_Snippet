import re, pyperclip

phoneregex = re.compile(r'''
(((\d{3}) | (\(\d\d\d\)))?
(\s|-)
\d\d\d
-
\d\d\d\d
(((ext(\.)?\s) |x) 	
(\d{2,5}))?)

''',re.VERBOSE)

emailregex = re.compile(r'''
[a-zA-Z0-9_.+]+
@
[a-zA-Z0-9_.+]+
''',re.VERBOSE)

text = pyperclip.paste()

extractedphone = phoneregex.findall(text)
extractedemail = emailregex.findall(text)

phone=[]
for i in extractedphone:
	phone.append(i[0])

results =    "\n".join(phone)+ '\n'+	"\n".join(extractedemail)

print(results)

# print(phone)
# print(extractedemail)
