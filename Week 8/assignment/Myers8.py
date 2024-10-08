from operator import index
from typing import Literal


def main():
    students: list[str] = []
    subject_names: list[str] = ["Math", "Science", "English"]
    grades: list[list[float]] = [[], [], []]


    def calculate_student_average(student_index: int) -> float:
        total = 0
        for grade in grades:
            total += float(grade[student_index])
        return total / len(grades)

    def find_subject_average(subject_index: int) -> float:
        return sum(grades[subject_index]) / len(grades[subject_index])

    def get_valid_float(user_prompt: str) -> float:
        while True:
            try:
                a = float(input(user_prompt))
                return a
            except ValueError:
                print("That is not a float...")

    def get_valid_int(user_prompt: str) -> int:
        while True:
            try:
                a = int(input(user_prompt))
                return a
            except ValueError:
                print("That is not an integer...")

    def user_add_student():
        student_name = input("Enter student name: ")
        students.append(student_name)

        for grade_index in range(len(grades)):
            while True:
                ui = get_valid_float(f"Enter grade for {student_name} in {subject_names[grade_index]}: ")
                if 0 <= ui <= 100:
                    grades[grade_index].append(ui)
                    break
                else:
                    print("Grade must be between 0 and 100.")
        print("Student added!")

    def user_students_and_grades():
        print(f"{'Student':19}|", end="")
        for subject_index in range(len(subject_names)):
            print(f"{subject_names[subject_index]:^10}|", end="")
        print("")

        for student_index in range(len(students)):
            print(f"{students[student_index]:19}|", end="")
            for grade_index in range(len(grades)):
                print(f"{grades[grade_index][student_index]:^10}|", end="")
            print("")

    def user_student_average_grade():
        student_name = input("Enter student name: ")
        found_students = 0
        for s_index in range(len(students)):
            student = students[s_index]
            if student.lower() == student_name.lower():
                found_students += 1
                print(f"{student}'s average grade: {calculate_student_average(s_index)}")
        if found_students == 0:
            print("Invalid student name...")

    def user_find_top_student():
        highest_gpa = 0
        highest_student_name: list[str] = []
        for s_index in range(len(students)):
            student = students[s_index]
            student_average = calculate_student_average(s_index)
            if student_average > highest_gpa:
                highest_gpa = student_average
                highest_student_name = [student]
            elif student_average == highest_gpa:
                highest_student_name.append(student)

        if len(highest_student_name) > 1:
            print(f"Top students (tie): ")
        else:
            print(f"Top student:")
        for name in highest_student_name:
            print(f"{name}'s average grade: {highest_gpa}")

    def user_get_subject_average():
        subject_name = input("Enter subject name: ").title()
        try:
            subject_index = subject_names.index(subject_name)
            print(f"Average for {subject_name}: {find_subject_average(subject_index)}")
        except ValueError:
            print("That is not a valid subject name...")

    def user_remove_student():
        student_name = input("Enter student name: ")
        for s_index in range(len(students) - 1, -1 , -1):
            student = students[s_index]
            if student.lower() == student_name.lower():
                students.pop(s_index)
                print(f"Student removed: {student}")

    def user_best_subject():
        best_subject_gpa = 0
        best_subject_indexes = []
        for subject_index in range(len(subject_names)):
            this_subject_gpa = sum(grades[subject_index]) / len(grades[subject_index])
            if this_subject_gpa > best_subject_gpa:
                best_subject_gpa = this_subject_gpa
                best_subject_indexes = [subject_index]
            elif this_subject_gpa == best_subject_gpa:
                best_subject_indexes.append(subject_index)
        print("Best Subject(s):")
        for subject_index in best_subject_indexes:
            print(f"{subject_names[subject_index]} - Average grade of {best_subject_gpa}")

    def user_specific_grade_change():
        student_name = input("Enter student name: ")
        for s_index in range(len(students)):
            student = students[s_index]
            if student.lower() == student_name.lower():
                subject_name = input("Enter subject name: ")
                subject_index = subject_names.index(subject_name.title())
                if subject_index == -1:
                    print("Invalid subject name...")
                    return
                else:
                    new_grade = get_valid_float(f"Enter grade for {student_name} in {subject_name}: ")
                    grades[subject_index][s_index] = new_grade
                    print("Grade updated!")

    def user_exit():
        exit(0)

    program_functions = [
        ["Add a new student", user_add_student],
        ["View students and grades", user_students_and_grades],
        ["View students average grade", user_student_average_grade],
        ["Find top student", user_find_top_student],
        ["Find subject average", user_get_subject_average],
        ["Remove student", user_remove_student],
        ["Find best subject", user_best_subject],
        ["Update student grade in subject", user_specific_grade_change],
        ["Quit", user_exit]
    ]

    while True:
        input("Grade Manager, press enter to continue!")
        for program_function_index in range(len(program_functions)):
            print(f"{program_function_index + 1}) {program_functions[program_function_index][0]}")

        trying_input = True
        while trying_input:
            selected_option = get_valid_int("Enter option number: ")
            if 0 < selected_option <= len(program_functions):
                trying_input = False
                print("")
                program_functions[selected_option - 1][1]()
                print("")
            else:
                print("That is not a valid option...")


if __name__ == '__main__':
    main()