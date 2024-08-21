def arithmetic_arranger(problems, show_answers=False):

    if len(problems) > 5:
        return 'Error: Too many problems.'


    first_line = ""
    second_line = ""
    dashes = ""
    results = ""

    for problem in problems:
        num1, operator, num2 = problem.split()


        width = max(len(num1), len(num2)) + 2

        if width > 6:
            return 'Error: Numbers cannot be more than four digits.'

        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."
        
        first_line += str(num1).rjust(width) + "    "
        second_line += operator + str(num2).rjust(width - 1) + "    "
        dashes += "-" * width + "    "

        if operator == "+":
            result = str(int(num1) + int(num2))
        elif operator == "-":
            result = str(int(num1) - int(num2))
        else:
            return "Error: Operator must be '+' or '-'."
        results += result.rjust(width) + "    "
        

    first_line = first_line.rstrip()
    second_line = second_line.rstrip()
    dashes = dashes.rstrip()
    results = results.rstrip()

    if show_answers == True:
        problems = f"{first_line}\n{second_line}\n{dashes}\n{results}"
    else:
        problems = f"{first_line}\n{second_line}\n{dashes}"

    return problems
        

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')