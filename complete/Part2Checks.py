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

def checkForMissingCommas():
    filelines = open('finalv2.txt').readlines()
    filelines = [line.strip() for line in filelines]  # strip excess whitespace just in case

    for