
subject = ["Math", "Science", "History", "Art", "Physical Education"]

print(subject[-2:-1])

for list in subject:
    print(list[0].capitalize())



nums = [1,8,2,5,4,6]

squares = [num**2 for num in nums]
cubes = [num**3 for num in nums]
print(squares)
print(cubes)


max = 0;
for num in nums:
    if num > max:
        max = num
print(max)



second_max = 0;
max =0
for num in nums:
    if num > max:
        max = num
        second_max = max
    elif num > second_max and num!= max:
          second_max = num
print(max)
print(second_max)
