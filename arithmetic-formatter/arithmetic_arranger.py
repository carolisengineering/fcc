TOO_MANY_PROBLEMS = 'Error: Too many problems.'
INCORRECT_OPERATOR = "Error: Operator must be '+' or '-'."
DIGITS_ONLY = 'Error: Numbers must only contain digits.'
TOO_MANY_DIGITS = 'Error: Numbers cannot be more than four digits.'

def arithmetic_arranger(problems):

    arranged_problems = 'PASS'

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

    return arranged_problems