x1, y1 = map(int, input('введите координаты первой клетки (x1:y1): ').split(':'))
x2, y2 = map(int, input('введите координаты второй клетки (x2:y2): ').split(':'))
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