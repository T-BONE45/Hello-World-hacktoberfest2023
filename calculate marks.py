def calculate_average(marks):
    total_marks = sum(marks)
    average = total_marks / len(marks)
    return average

def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
    num_students = int(input("Enter the number of students: "))
    student_data = []

    for i in range(num_students):
        student_name = input(f"Enter the name of student {i + 1}: ")
        student_marks = []
        for j in range(3):  # Assuming 3 subjects, you can change this
            mark = float(input(f"Enter the mark for subject {j + 1}: "))
            student_marks.append(mark)
        student_data.append((student_name, student_marks))

    print("\nStudent Report:")
    for student_name, student_marks in student_data:
        average = calculate_average(student_marks)
        grade = calculate_grade(average)
        print(f"{student_name}: Average = {average:.2f}, Grade = {grade}")

if __name__ == "__main__":
    main()
