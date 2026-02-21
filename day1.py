"""
Student Grade Analyzer
Uses: List comprehensions, dictionaries, zip, enumerate
"""

students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
maths_marks = [85, 92, 78, 65, 88]
science_marks = [90, 88, 72, 70, 85]
english_marks = [78, 85, 80, 60, 90]

student_data = [
    {'name':name ,'scores': scores , 'avg': round(sum(scores)/len(scores),2)} for name,scores in zip(students,zip(maths_marks,science_marks,english_marks))]
average = [ round(sum(score['scores'])/len(score['scores']),2) for score in student_data ]

def get_grade(avg):
    if avg >= 90 :
        return'A'
    elif avg>=80:
        return 'B'
    elif avg>=70:
        return 'C'
    elif avg>=60:
        return 'D'
    else :
        return 'F'
    pass

for student in student_data:
    student['grades'] = get_grade(student['avg'])
top = max(student_data,key=lambda x:x['avg'])['name']
bottom = min(student_data,key=lambda x:x['avg'])['name']
math_avg = round((sum(maths_marks)/len(maths_marks)),2)
science_avg = round((sum(science_marks)/len(science_marks)),2)
english_avg = round((sum(english_marks)/len(english_marks)),2)
passed_student = [ dic['name'] for dic in student_data if dic['avg'] >= 60 ]
failed_student = [ dic['name'] for dic in student_data if dic['avg'] < 60 ] 

def print_report():
    """Print a nicely formatted report"""
    print("="*50)
    print("STUDENT GRADE REPORT")
    print("="*50)
    for i,student in enumerate(student_data,start=1) :
        print("#"*50)
        print(f"{i}.{student['name']}\n")
        print("-"*50)
        print(f"maths_marks = {student['scores'][0]} | science_marks = {student['scores'][1]} | english_marks = {student['scores'][2]}\ngrade = {student['grades']} with average of {student['avg']}\n")
        print("-"*50)
    print("CLASS STASTICS\n")
    print("-"*50)
    print(f"maths average marks = {math_avg}\n")
    print(f"science average marks = {science_avg}\n")
    print(f"english average marks = {english_avg}\n")
    print("-"*50)
    print(f"topper student in the class = {top}({max(average)})\n")
    print(f"needs improvement = {bottom}({min(average)})\n")
    print("-"*50)
    print(f"no of students passed = {len(passed_student)}")
    print(f"needs improvement = {len(failed_student)}")
    print("-"*50)
    pass
print_report()