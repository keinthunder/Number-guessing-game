import random
a=random.randint(1,100)
Tries=0
while True:
    Tries+=1
    Hum=int(input('enter your number between 1-100'))
    if Hum==a:
        print('congrats u won🎉\nYour tries are',Tries)
        break
    elif Hum>a:
        print("sry wrong guess go a little lower😅🔻")
    else:
        print("sry wrong guess go a little above😅🔺")