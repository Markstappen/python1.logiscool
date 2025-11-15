"""
while True:
    print("2")
"""
i = 0
while i<10:
    print(i)
    i += 2

for i in range (10):
    print(i)

sum = 0
for j in range (10):
    sum += j 
    print(sum)

num = 6845
count = 0
while num != 0:
    num = num//10
    count +=1 
print(count)


counting = 8
num1 = 0
num2 = 1 
print(num1)
print(num2)
for i in range (8):
    temp = num1 + num2
    num1 = num2
    num2 = temp 
    print(num2)