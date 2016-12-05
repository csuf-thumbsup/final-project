try:
    from datatables import lr_table, cfg_table
except Exception:
    from .datatables import lr_table, cfg_table

def prep_file_list(filename):
    non_terminals = ['program', 'var', 'integer', 'print', 'begin', 'end.', ';', ':', ',']
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

    return new_file_list

def run_parser(parsing_table, cfg_table, input_list):
    str_list = input_list

    stack = ['0'] # init stack to 0

    i = 0 # index for str_list
    read_char = str_list[0] # init read_char to first char

    temp_iter = 1

    while(True):
        print('\n-----Iteration #' + str(temp_iter) + '-----\n')

        # pop the stack on every iteration and store into popped_char
        popped_char = stack.pop()

        # find [popped_char, read_char] in our parsing_table
        temp_parsed_value = parsing_table[popped_char][read_char]

        # our checks and balances
        # if our value is S#
        if temp_parsed_value[0] == 'S':
            # append our 3 values to the stack
            stack.extend([popped_char, read_char, temp_parsed_value[1:]]) # temp_parsed_value[1:] accounts for digits like 14 (use of string slicing)

            # printing our matches for every instance of a read/accepted char
            print('Match!' + '\tpopped_char: ' + popped_char + '\tread_char: ' + read_char + '\tstack: ' + stack.__str__())

            i += 1 # increment our index for str_list
            read_char = str_list[i] # update read_char

        # if our value is R#
        elif temp_parsed_value[0] == 'R':
            # first we append our popped_char
            stack.append(popped_char)

            # get the rule defined by its index (temp_parsed_value[1]) e.g R8 => Rule #8 in CFG
            rule_dict = cfg_table[ int(temp_parsed_value[1:])-1 ] # convert to int and subtract by 1 to account for 0-indexing

            # pop the stack amount of 2*Length of the RHS
            for x in range(0, 2*rule_dict['length']):
                stack.pop()

            print('RVALUE:' + '\tpopped_char: ' + popped_char + '\tread_char: ' + read_char + '\tstack: ' + stack.__str__())

            # update read_char to the LHS of our rule
            read_char = rule_dict['lhs']
            print('CFG Rule #' + str(int(temp_parsed_value[1:])-1) + ' dict: '  + str(rule_dict))


        elif temp_parsed_value == 'undef':
            # printing our failed match
            print('************\nFail!' + '\tpopped_char: ' + popped_char + '\tread_char: ' + read_char + '\tstack: ' + stack.__str__())
            print('************\n\nYour string is NOT valid for the given language!:')#, input_list)
            return
        elif temp_parsed_value == 'ACCEPT':
            print('Your string IS valid for the given language!:', input_list)
            return

        # else our value is a number
        else:
            # append our 3 values to the stack
            stack.extend([popped_char, read_char, temp_parsed_value])

            print('NUMBER:' + '\tpopped_char: ' + popped_char + '\tread_char: ' + read_char + '\tstack: ' + stack.__str__())
            # update read_char to the current char
            read_char = str_list[i]

        temp_iter += 1

if __name__ == '__main__':
    file_str_list = prep_file_list('finalv2.txt')

    print('Parsing File...')
    run_parser(lr_table, cfg_table, file_str_list)

'''
program a 2 0 1 6 ; var a 1 , b 2 a , c , b a 1 2 : integer ; begin a 1 = 3 ; b 2 a = 4 ; c = 5 ; print ( c ) ; b a 1 2 = a 1 * ( b 2 a + 2 * c ) ; print ( b a 1 2 ) ; end.
program a 2 0 1 6 ; var a 1 , b 2 a , c , b a 1 2 : integer ; begin a 1 = 3 ; b 2 a = 4 ; c = 5 ; print ( c ) ; b a 1 2 = a 1 * ( b 2 a + 2 * c ) ; print ( b a 1 2 ) ; end.
'''



