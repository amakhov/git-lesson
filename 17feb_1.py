from datetime import datetime
datetime.now().minute
a=datetime.now().minute
print(a)
if (a%10<=3) or (5<=a%10<=8):
    print("Green")
else:
    print("Red")
    

