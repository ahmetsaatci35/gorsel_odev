count = 0
for a in range(1,10):
    for b in range(0,10):
        for c in range(0,10):
            if a != b and b !=c and a != c:
               print(str(a)+str(b)+str(c))
               count += 1
print("toplam",count, "tane sayı vardır")