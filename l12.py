#tache1 - recuperer data d une list
lenght_of_list = 10
numbers = []
while lenght_of_list > 0:
    new_number = int(input("Enter a number\n"))
    numbers.append(new_number)
    lenght_of_list -=1
odd = 0
even = 0
negative = 0
zero = 0
for i in numbers: 
    if i > 0:
        positif += 1
    elif i < 0:
        negative += 1
    else:
        zero += 1
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"""
"Evens: {even}
Odds:  {odd}
Positive:  {positif}
Negative:  {negative} 
Zero :  {zero}   
""")

# tache2 - supprimer duplication

nums = [1,2,3,4,5,6,6,7,8,8,9]
print(str(nums))
new_nums = []
skipped_nums = 0
for i in nums:
    if i not in new_nums:
        new_nums.append(i)
    else:
        skipped_nums += 1
print(str(nums))
print(str(new_nums))
print("Skipped numbers: " + str(skipped_nums))

#tache3 = extend command
list = [1,2,3,4]
print(list)
list.extend([9, "Hello There"])
print(list)
list.append([1,2])
print(list)

# tache4 - trouver integer dans list

list_bazzare = ["pomme poire",1,76,True,"null"]
integer_list = []
for i in list_bazzare:
    if type(i) == int:
        integer_list.append(i)
print(integer_list)