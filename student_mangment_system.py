#the program works it just needs input validation so the program doesn't crash


students = {
    "John": [30, 20, 10],
    "Sarah": [95, 92, 88],
    "Mike": [60, 55, 70]
}

running = True

while running:
    print("=" * 45)
    print('===== STUDENT MANAGEMENT SYSTEM =====\n\n' \
    '1. Add student\n' \
    '2. View all students\n' \
    '3. Calculate student average\n' \
    '4. Check pass or fail\n' \
    '5. Show top student\n' \
    '6. Exit\n\n')
    option = int(input('Choose an option (type 1 - 6): '))
    print("=" * 45)

    if option == 6:
        running = False
    
    #add student
    if option == 1:
        student_name = input('input student name: ')
        student_grades = input('input student grades: ')
        student_grades = student_grades.split(',')
        edited_student_grades = [] #new student grade after being converted from a string to int
        for grade in student_grades:
            grade = int(grade) #converts each grade string in the list student grades to an int
            edited_student_grades.append(grade) #adds the int grade to a new list

        students[student_name] = edited_student_grades

    #view all grades
    if option == 2:
        print("=" * 45) #prints decrative text prints the = 45 times
        print(f"{'STUDENT':<15} {'GRADES'}") #:<15 left aligns STUDENT and adds 15 spaces
        print("=" * 45)

        for key, value in students.items():
            grades = ", ".join(map(str, value)) # ", " ads a coma bettween each value
            print(f"{key:<15} {grades}") #prints the key left aligned with 15 spaces

        print("=" * 45)

    #caculate student average
    if option == 3:
        print("=" * 45)
        print('STUDENTS:')
        print("=" * 45)
        for key in students.keys():
            print(key)
        print("=" * 45)
        student_name = input('choose a student: ')
        grades = students[student_name] #grades = dictionary students at a key of student_name
        average = sum(grades) / len(grades)
        print(f"{student_name}'s grade average is: {average:.2f}" )

    #Display PASS if average >= 60, otherwise FAIL.
    if option == 4:
        print("=" * 45)
        print('STUDENTS:')
        print("=" * 45)
        for key in students.keys():
            print(key)
        print("=" * 45)
        student_name = input('choose a student: ')
        grades = students[student_name] #grades = the dictionary students at a key of the students name
        average = sum(grades) / len(grades) #caculates average
        if average >= 60: 
            print('PASS')
        else:
            print("FAIL")
    
    #Find the student with the highest average.
    if option == 5:
        averages = {}
        averages_sorted = {}

        for key, value in students.items(): 
            average = sum(value) / len(value)
            averages[key] = average

        averages_sorted = dict(sorted(averages.items(), key=lambda item: item[1], reverse=True))

        first_key = list(averages_sorted.keys())[0] #extracts the first key in the dictionary, we acess all the keys in the dicionary with .keys() then list() converts the dicionary into a list, then [0] acesses the element at index 0
        first_value = averages_sorted[first_key] #extracts the value at first_key

        print(f"{first_key} has the highest grade average at: {first_value:.2f}")