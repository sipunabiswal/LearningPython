student_heights=input("Input a list of student height followed by space. ").split()
for n in range(0,len(student_heights)):
    student_heights[n]=int(student_heights[n])
print(student_heights)

sum_height=0
count=0
for height in student_heights:
    sum_height+=height
    count+=1

avg_height = sum_height/count

print(f"Average height rounded to nearest whole number is {round(avg_height)}.")