
nums = [4,1,2,1,2]
single=[]

for i in nums:
          if nums.count(i) == 1:
                    single.append(i)

print(single)