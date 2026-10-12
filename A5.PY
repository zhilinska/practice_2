x = 0
while x == 0:
    try:
        fnum = int(input("введиде число A: "))
        snum = int(input("введиде число B: "))
        while snum == 0:
            print('на ноль не делят')
            fnum = int(input("введиде число A: "))
            snum = int(input("введиде число B: "))
        x = x + 1
    except:
        print('сюда бы число')
if fnum % snum == 0:
    print("YES")
else:
    print("NO")