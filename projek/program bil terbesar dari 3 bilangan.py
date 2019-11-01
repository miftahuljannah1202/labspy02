#!/user/bin/python3
print("program bilangan terbesar dari 3 buah bilangan yang dinputkan")
a = int(input("masukkan bilangan pertama: "))
b = int(input("masukkan bilangan kedua: "))
c = int(input("masukkan bilangan ketiga: "))

if a > b and a < c:
    print(a,"terbesar dari 3 bilangan yang diinputkan")
elif b > a and b > c:
    print(b,"terbesar dari 3 bilangan yang diinputkan")
else:
    print(c,"terbesar dari bilangan yang diinputkan")
