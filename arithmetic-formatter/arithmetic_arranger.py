TOO_MANY_PROBLEMS = 'Error: Too many problems.'
INCORRECT_OPERATOR = "Error: Operator must be '+' or '-'."
DIGITS_ONLY = 'Error: Numbers must only contain digits.'
TOO_MANY_DIGITS = 'Error: Numbers cannot be more than four digits.'

def arithmetic_arranger(problems, expected_output=False, fail_message=None):
    """ Given a list of arithmetic problem strings, arrange the problems vertically and side by side."""

    arranged_problems = 'PASS'
    problem_components = []

    if len(problems) > 5:
        return TOO_MANY_PROBLEMS

    for problem in problems:
        parts = problem.split()

        first_operand = parts[0]
        operator = parts[1]
        second_operand = parts[2]

        # check for invalid input
        if operator != '+' and operator != '-':
            return INCORRECT_OPERATOR
        if not first_operand.isnumeric() or not second_operand.isnumeric():
            return DIGITS_ONLY
        if len(first_operand) > 4 or len(second_operand) > 4:
            return TOO_MANY_DIGITS


        # transform strings to numbers and calulate solution
        first_operand_num = int(first_operand)
        second_operand_num = int(second_operand)

        if operator == '+':
            solution_num = first_operand_num + second_operand_num
        elif operator == '-':
            solution_num = first_operand_num - second_operand_num

        solution = str(solution_num)


        # create strings with correct spacing from problem and solution
        if len(first_operand) > len (second_operand):
            first_line = '  ' + first_operand
            spaces = ' ' * (len(first_operand) - len(second_operand))
            second_line = operator + ' ' + spaces + second_operand            
        else:
            spaces = (' ' * (len(second_operand) - len(first_operand)))
            first_line = '  ' + spaces + first_operand
            second_line = operator + ' ' + second_operand

        problem_components.append((first_line, second_line, solution))


    # create output strings
    first_operands = ''
    second_operands = ''
    dashes = ''
    solutions = ''

    for x in range(len(problem_components)):
        if x < (len(problem_components) - 1):
            first_operands += (problem_components[x][0] + '    ')
            second_operands += (problem_components[x][1] + '    ')
            dashes += ('-' * len(problem_components[x][1]) + '    ')
            solutions += ((' ' * (len(problem_components[x][1]) - len(problem_components[x][2]))) + problem_components[x][2] + '    ')
        elif x == (len(problem_components) - 1):
            first_operands += (problem_components[x][0] + '\n')
            second_operands += (problem_components[x][1] + '\n')
            if expected_output:
                dashes += ('-' * len(problem_components[x][1]) + '\n')
            else:
                dashes += ('-' * len(problem_components[x][1]))
            solutions += ((' ' * (len(problem_components[x][1]) - len(problem_components[x][2]))) + problem_components[x][2])


    # construct output and return values based on input parameters
    if expected_output:
        arranged_problems = first_operands + second_operands + dashes + solutions
    else:
        arranged_problems = first_operands + second_operands + dashes

    if fail_message:
        return arranged_problems, fail_message
    else:
        return arranged_problems