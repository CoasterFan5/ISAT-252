from random import randint

problem_count = 1
problem_number = 1
global_test_cases = ""

def make_test_cases():
    global global_test_cases
    test_cases_file = open("./problemBank/problem_" + str(problem_number) + "/test.py")
    global_test_cases = test_cases_file.read()
    test_cases_file.close()

def new_problem():
    global problem_number
    problem_number = randint(1, problem_count)
    print("Now solving: Problem", problem_number)
    code_editor = open("./code_editor.txt", "w")
    problem_file = open("./problemBank/problem_" + str(problem_number) + "/problem.py", "r")
    make_test_cases()
    code_editor.write(problem_file.read())
    code_editor.close()
    problem_file.close()

def compile_problem():
    global global_test_cases
    code_editor = open("./code_editor.txt", "r")
    code_parser = open("./code_parser", "w")
    code_parser.write("")

    code_parser = open("./code_parser", "a")
    code_editor_content = code_editor.read()
    code_parser.write(code_editor_content)
    code_parser.write("\n")
    code_parser.write(global_test_cases)
    code_parser.write("\ntest(main)")
    code_parser.close()


def test(func):
    print(func)
    passing = func()
    for test_case in global_test_cases:
        try:
            result = func(test_case)
            print(result, test_case)
            if result != test_case[1]:
                passing = False
                raise Exception("Test Failed Test Case. Expected: ", test_case[1], "got:", result)
            else:
                print("Test Passed")
        except Exception as e:
            passing = False
            print("Test failed with error: ", e)
    if passing:
        print("All Tests Passed")
        print("Fetching new problem...")
        new_problem()


if __name__ == '__main__':
    new_problem()
    while True:
        input("Enter anything to test function")
        compile_problem()
        code_editor = open("./code_editor.txt", "r")
        code_parser_read = open("./code_parser", "r")
        try:
            exec(code_parser_read.read(), {"do_test": test})
        except Exception as e:
            print("Error executing program")
            print(e)
        code_parser_read.close()
        code_editor.close()




