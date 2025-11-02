#Challenge : Smart Grader App
# Input: name , marks 
# Output: Grade + Feedback

name = input("Enter your name:")
marks = int(input("Enter your marks :"))

if marks >= 90:
    grade = 'A+'
    feedback = 'Excellent work!'
elif marks >= 75:
    grade = 'B'
    feedback= 'Good job!'
elif marks >= 50:
    grade = 'C'
    feedback = 'You passed.'
else:
    grade = 'F'
    feedback = 'Better luck next time.'

print(f'Hello {name}, your grade is {grade}.{feedback}')

# if they want to retake the test 


retry = (input("Do you want to retake the test? (yes/no): ")).lower()

if retry == 'yes':
    print("let's start again soon!")
else:
    print("Goodbye, keep leaning!")