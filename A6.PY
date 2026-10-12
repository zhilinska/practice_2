sek = int(input("введите кол-во секунд: "))
while sek > 86399: #если введено больше суток
    sek = sek - 86400
h = sek // 3600
k = h * 3600
sek = sek - k
m = sek // 60
l = m * 60
s = sek - l
print("{:02}:{:02}:{:02}".format(h, m, s))