x = 0
while x == 0:
    try:
        x1, y1 = map(int, input('введите координаты первой клетки (x1:y1): ').split(':'))
        x2, y2 = map(int, input('введите координаты второй клетки (x2:y2): ').split(':'))
        while x1 not in range(1, 9) or\
        x2 not in range(1, 9) or\
        y1 not in range(1, 9) or\
        y2 not in range(1, 9):
            print('клеточек не так много')
            x1, y1 = map(int, input('введите координаты первой клетки (x1:y1): ').split(':'))
            x2, y2 = map(int, input('введите координаты второй клетки (x2:y2): ').split(':'))
        x = x + 1
    except:
        print('попробуйте ввести числа от 1 до 8 по образцу')
if (x1 + y1) % 2 == 0:
    cell1 = 'white'
else: 
    cell1 = 'black' 
if (x2 + y2) % 2 == 0:
    cell2 = 'white'
else: 
    cell2 = 'black' 
if cell1 == cell2:
    print('YES')
    print(cell1)
else:
    print('NO')