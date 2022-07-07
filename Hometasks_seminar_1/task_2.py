# 2.Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

check = [0, 1]
for x in check:
    for y in check:
        for z in check:
            if not(x or y or z) == (not x and not y and not z):
                print(f"{x}, {y}, {z} true")
            else:
                print(f"{x}, {y}, {z} false")