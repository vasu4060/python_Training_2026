
numbers = [1,2,4,6,7,9,10]

squares = [x **2 for x in numbers]
print(squares)

evens = [x for x in numbers if x%2==0]

print(evens)

odds = [x for x in numbers if x%2 == 1]

print(odds)


words = "hello my nam eis ayyapa i'm a good boy"

split_words = words.split()
capitalized_words = [word.capitalize() for word in split_words]
print(capitalized_words)

Upper_words = [word.upper() for word in split_words]
print(Upper_words)



numbers = [1,1,2,4,4,6,6,8,9,9,9]

unique_numbers = set(numbers)
print(unique_numbers)
