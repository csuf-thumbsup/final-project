from datatables_1 import parsing_table
import Part2Checks as ck

def prep_file_list(filename, for_parser=False):
    non_terminals = ['$', 'program', ';', 'var', 'begin', 'end.', ':', ',', 'integer', 'print', '+', '-', '*', '/', '(', ')', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c']
    filelines = open(filename).readlines()
    file_str = ' '.join(line.strip() for line in filelines)

    file_list = file_str.split()
    new_file_list = []
    for word in file_list:
        if word in non_terminals:
            new_file_list.append(word)
        elif word == 'print(':
            # special case for print(
            new_file_list.extend(['print', '('])
        else:
            if for_parser:
                new_file_list.extend(list(word))
            else:
                new_file_list.append(word)
    if for_parser:
        new_file_list.append('$') # append $
    return new_file_list

def run_parser(parsing_table, input_list, terminals, starting_non_terminal):
    str_list = input_list
    stack = ['$', starting_non_terminal] # initialize stack to $ and the starting non-terminal

    i = 0
    read_char = str_list[i] # init read_char to first char

    temp_index = 2
    accepted_input = read_char

    while(True):

        print('\n*******Iteration #' + str(temp_index) + '*******\n')
        print('Stack: \t' + stack.__str__())

        # pop the stack on every iteration and store into popped_char
        popped_char = stack.pop()

        # immediate check if the popped_char is a terminal
        if popped_char in terminals:
            # we found a match
            print('MATCH: ' + popped_char)
            i = i + 1
            read_char = str_list[i]
            accepted_input += read_char
            temp_index += 1
            continue

        elif popped_char == '$':
            # check for end of string. If we got here then you're good to go!
            print('MATCH: ' + popped_char)
            print('Your string IS valid: ' + input_list.__str__())
            exit(0)

        print('popped_char: ' + popped_char + '\tread_char: ' + read_char)
        # find [popped_char, read_char] in our parsing_table_1
        try:
            temp_parsed_value = parsing_table[popped_char][read_char]
        except KeyError:
            print('\n\n*****ERROR Accessing Parsing Table*****')
            exit(1)

        print('parsing_table[ ' + popped_char + ' ][ ' + read_char +' ] ' + ' = ' + temp_parsed_value)

        # our checks and balances
        if temp_parsed_value == 'undef':
            print('\nYour string is NOT valid for the given language!:', input_list.__str__())
            return
        elif temp_parsed_value == 'lambda':
            temp_index += 1
            # skip and loop back to top
            continue
        else:
            # we found a valid value
            # just put back on the stack even if its a terminal

            value_list = temp_parsed_value.split()
            print('Value_list: \t' + str(value_list))

            reversed_list = value_list[::-1]
            stack.extend(reversed_list)

            '''
            reversed_value = temp_parsed_value[::-1]
            for x in reversed_value:
                # push the values in reverse order
                stack.append(x)
            '''

        temp_index += 1
        print('Accepted Input:  ' +  accepted_input)

if __name__ == '__main__':

    print('\n--------------Executing Part 2-----------------\n')

    terminals = ['program', ';', 'var', 'begin', ':', ',', 'integer', 'end.', 'print', '=', '+', '-', '*', '/', '(',
                 ')', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c']
    keywords = ['program', 'var', 'integer', 'begin', 'end.']

    #------ PRE-CHECKS ---------------------------
    preCheckInput = prep_file_list('finalv2.txt', False)

    ck.checkForPrintMisspelling(preCheckInput)

    ck.checkForPeriod(preCheckInput)

    ck.checkForKeywords(preCheckInput, keywords)

    ck.checkForUndefinedVariables(preCheckInput, terminals)

    ck.checkForMissingSemiColons()

    ck.checkForMissingCommas(preCheckInput)

    ck.checkForParentheses(preCheckInput)

    #------ PARSING ------------------------------
    print('Attempting to Parse...')
    parser_input = prep_file_list('finalv2.txt', True)
    starting_non_terminal = 'A'
    run_parser(parsing_table, parser_input, terminals, starting_non_terminal)
