def checkForPrintMisspelling(input_list):
    for word in input_list:
        # the way input_list is formatted then a misspelled "print" will still have left parantheses next to it
        # e.g. pabct(
        if len(word) == 6 and word[0] == 'p' and word[-2] == 't' and word[-1] == '(':
            # we definitely know this word is misspelled from the input_list
            print('print is misspelled.')
            exit(1)

def checkForPeriod(input_list):
    last_word = input_list[-1]
    if last_word == 'end':
        # check last elem which should be end
        print('. is missing from end')
        exit(1)

def checkForKeywords(input_list, keywords_list):
    for keyword in keywords_list:
        if keyword not in input_list:
            print(keyword + ' is expected.\n')
            exit(1)

def checkForUndefinedVariables(input_list, terminals_list):

    variable_list = [] # first get variables
    var_index = input_list.index('var')
    integer_index = input_list.index('integer')
    for word in input_list[var_index+1:integer_index]:
        if word in [',', ':']:
            # skip over terminals
            continue
        else:
            variable_list.append(word) # add our declared variables


    begin_index = input_list.index('begin')
    word_list = input_list[begin_index+1:] # get our words to examine from 'begin' and onwards

    valid_list = terminals_list + variable_list # joining the lists together

    for word in word_list:
        if word not in valid_list:
            print(word + ' is an Unkown Identifier.\n')
            exit(1)

def checkForMissingSemiColons():
    filelines = open('finalv2.txt').readlines()
    filelines = [line.strip() for line in filelines] # strip excess whitespace just in case

    for line in filelines:
        if line.startswith('var') or line.startswith('begin') or line.startswith('end.'):
            continue
        else:
            # we need to check this line for an ending semi-colon
            last_letter = line[-1]
            if last_letter != ';':
                print('; is missing from the following code of line:\t' + line)
                exit(1)

def checkForMissingCommas(input_list):

    var_index = input_list.index('var')
    integer_index = input_list.index('integer')
    variable_list = input_list[var_index + 1:integer_index]

    i=0
    while(i < len(variable_list)):
        word = variable_list[i]
        peak_word = variable_list[i+1]
        if word not in [',', ':']:
            # word is a some var, we need to check if the next word is a , or :
            if peak_word not in [',', ':']:
                print(', is missing from var line.')
                exit(1)
            else:
                i += 2

def checkForParentheses(input_list):
    begin_index = input_list.index('begin')
    end_index = input_list.index('end.')
    word_list = input_list[begin_index + 1:end_index]  # get our words to examine from 'begin' and onwards

    triggered_parentheses = False
    for word in word_list:
        # once we see a (, then we need to look for a )
        if word == '(':
            if triggered_parentheses:
                # we found another left parantheses without finding a right one first
                print('Right parantheses is missing.')
                exit(1)
            else:
                triggered_parentheses = True
        elif word == ')':
            # only if it was set
            if triggered_parentheses:
                # we found a closing right parentheses, so reset the flag
                triggered_parentheses = False
            else:
                # we found another right parantheses without finding a left one first
                print('Left Parentheses is missing.')
                exit(1)