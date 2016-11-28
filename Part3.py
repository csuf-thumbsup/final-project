def generate_code_str():
    fileline_list = open('finalv2.txt').readlines() # get list of all file lines

    code_list = []
    trigger = False

    for line in fileline_list:
        # we literally dont care about anything until the "begin" keyword

        # begin keyword was flagged
        # begin adding to code_list until end.
        if trigger:
            if line.startswith('end.') == False:
                code_line = line.replace(' ;', '') # replace ' ;' with nothing -- get rid of the end of the string
                code_list.append(code_line)

        # check if line is a keyword we care about
        if line.startswith('begin'):
            trigger = True

    # end - we've parsed and added all necessary code_lines
    code_str = '\n'.join(code_list)
    return code_str

if __name__ == '__main__':
    code_str = generate_code_str()
    print('Generated Python code:\n---------\n' + code_str + '---------')
    print('\nExecuting generated code...\n')
    exec(code_str)





