student = {
    "name":"John",
    "age":24,
    "major":"Data Science"
}

print(student)
print(student["name"])
print(student.get("age"))

student['gpa'] = 3.8

print(student)

for key,value in student.items():
          print(key,value)




text = "machine learning machine ai ai ai"

words = text.split()

freq = {}

for word in words:
          if word in freq:
                    freq[word] += 1
          else:
                    freq[word] = 1

print(freq)