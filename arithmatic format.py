def arithmetic_arranger(problems, show_answers=False):

    if len(problems) >= 6:
        return 'Error: Too many problems.'
    top_line = []
    bottom_line = []
    dash_line = []
    result_line = []


    
    for question in problems:
        pieces = question.split()

        if len(pieces) != 3:
            return 'Error: Invalid problem format.'
            
        n1, opr, n2 = pieces
        if opr not in ['+', '-']:
            return 'Error: Operator must be \'+\' or \'-\'.'
            
        if not n1.isdigit() or not n2.isdigit():
            return 'Error: Numbers must only contain digits.'
            
        if len(n1) > 4 or len(n2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
            
        # After errors, we fix the formatting 

        space = max(len(n1), len(n2)) + 2

        top_line.append(n1.rjust(space))

        bottom_line.append(opr + ' ' + n2.rjust(space - 2))

        dash_line.append('-' * space)

        # Result calculation if asked
        if show_answers==True:
            if opr == '+':
                result = str(int(n1) + int(n2))
            else:
                result = str(int(n1) - int(n2))
            result_line.append(result.rjust(space))

    # Output formatting
    output = '\n'.join(['    '.join(top_line),
                        '    '.join(bottom_line),
                        '    '.join(dash_line)])
    
    if show_answers:
        output += '\n' + '    '.join(result_line)
    return output


print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')
