from datatables_1 import parsing_table

def prep_file_list(filename):
    non_terminals = ['program', ';', 'var', 'begin', 'end.', ':', ',', 'integer', 'print', '+', '-', '*', '/', '(', ')', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c']
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
            new_file_list.extend(list(word))

    print('File List: ' + new_file_list.__str__() + '\n')
    return new_file_list

def run_parser(parsing_table_1, input_str, terminals, starting_non_terminal):
    str_list = input_str
    stack = ['$', starting_non_terminal] # initialize stack to $ and the starting non-terminal

    i = 0
    read_char = str_list[i] # init read_char to first char

    temp_index = 1

    while(True):

        print('*******Iteration #' + str(temp_index) + '*******\n')
        print('Stack: \t' + stack.__str__())

        # pop the stack on every iteration and store into popped_char
        popped_char = stack.pop()

        # immediate check if the popped_char is a terminal
        if popped_char in terminals:
            # we found a match
            print('match: ' + popped_char + '\tstack: '+ stack.__str__())
            i = i + 1
            read_char = str_list[i]
            continue
        elif popped_char == '$':
            # check for end of string. If we got here then you're good to go!
            print('match: ' + popped_char + '\tstack: ' + stack.__str__())
            print('Your string IS valid:', input_str)
            return;

        print('----Values----')
        print('popped_char: ' + popped_char + '\tread_char: ' + read_char)
        # find [popped_char, read_char] in our parsing_table_1
        temp_parsed_value = parsing_table_1[popped_char][read_char]

        print('----Grabbing val from parsing_table----')
        print('parsing_table_1[' + popped_char + '][' + read_char +']' + ' = ' + temp_parsed_value)

        # our checks and balances
        if temp_parsed_value == 'undef':
            print('Your string is NOT valid for the given language!:', input_str)
            return;
        elif temp_parsed_value == 'lambda':
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

if __name__ == '__main__':

    terminals = ['program', ';', 'var', 'begin', 'end.', ':', ',', 'integer', 'print', '+', '-', '*', '/', '(', ')', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c']
    input = prep_file_list('finalv2.txt')
    starting_non_terminal = 'A'

    print('Attempting to Parse...')

    run_parser(parsing_table, input, terminals, starting_non_terminal)
