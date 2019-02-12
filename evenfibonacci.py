# EVEN FIBONACCI NUMBERS - 5%
# finds sum of even Fibonacci numbers
fibs = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
while fibs[-1] < 4000000:
    fibs.append(fibs[-1] + fibs[-2])
total = 0
for num in fibs:
    if num %2 == 0:
        total += num
print(total)