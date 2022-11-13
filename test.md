grade1 and 
grade2
grade2represent two grades (
float
floats) between 0.0 and 100.0, inclusive. A passing grade is greater than or equal to 50.   Select the code fragment(s) that prints the average of all passing grade(s). The printed value should be 0.0 if neither grade is a passing grade, the passing grade if exactly one grade is a passing grade, and the average of the two grades if both are passing grades.

Watch your ifs and elifs!

```
  total = 0
grade_count = 0

if grade1 >= 50:
    total = total + grade1
    grade_count = grade_count + 1
elif grade2 >= 50:
    total = total + grade2
    grade_count = grade_count + 1

if grade_count > 0:
    print(total / grade_count)
else:
    print(0.0)
  ```
  
  ```
  total = 0
grade_count = 0

if grade1 >= 50:
    total = total + grade1
    grade_count = grade_count + 1
else:
    total = total + grade2
    grade_count = grade_count + 1

if grade_count > 0:
    print(total / grade_count)
else:
    print(0.0)
    ```
    
    ```
    total = 0
grade_count = 0

if grade1 >= 50 and grade2 >= 50:
    total = grade1 + grade2
    grade_count = 2

if grade_count > 0:
    print(total / grade_count)
else:
    print(0.0)
    ```
    ```
    total = 0
grade_count = 0

if grade1 >= 50:
    total = total + grade1
    grade_count = grade_count + 1
if grade2 >= 50:
    total = total + grade2
    grade_count = grade_count + 1

if grade_count > 0:
    print(total / grade_count)
else:
    print(0.0)
    ```
