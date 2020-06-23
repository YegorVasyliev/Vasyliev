a=input()
b=a.upper()
c=b.replace(" ","")
if c[:]==c[::-1]:
    print('palindrom')
else:
    print("no")
