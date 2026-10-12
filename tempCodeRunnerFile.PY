    try:
        fnum = int(input("введиде число A от 1 до 1000: "))
        snum = int(input("введиде число B от 1 до 1000: "))
        while fnum not in range(1, 1001) or snum not in range(1, 1001):
            print('данные не подходят')
            fnum = int(input("введиде число A от 1 до 1000: "))
            snum = int(input("введиде число B от 1 до 1000: "))
        x = x = 1
    except:
        print('это ж не число')