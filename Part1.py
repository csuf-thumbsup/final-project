import re

def remove_comments(input_list):
    pattern = re.compile('\/\*' + '(.*?)' + '\*\/')  # pattern: /* (anything in between) */

    new_list = []
    # removing comments from list
    multi_line_comment_flag = False
    for line in input_list:
        # immediate check if its a one-liner comment
        if line[0:2] == '/*' and line[-2:] == '*/':
            continue
        elif line[0:2] == '/*':
            multi_line_comment_flag = True
        elif multi_line_comment_flag:
            # check if we are at the end of the comment
            if line[-2:] == '*/':
                multi_line_comment_flag = False
            else:
                continue
        else:
            # append our line and remove any embedded comments in the line
            if line:
                # we skip empty elements and strip excess whitespace again just in case
                new_list.append(re.sub(pattern, '' ,line).strip())

    return new_list

def format_item(item):
    item_list = re.split('(,|\+|\*|:|;|=|print\(|\(|\))', item) # break item into list by [, :, =, print(, (, )]keywords/delimeters

    item_list = [item.strip() for item in item_list] # strip excess whitespace from each item

    item_list = [item for item in item_list if item] # remove empty items from list

    return item_list

def beautify(filename):
    filelines = [line.strip() for line in open(filename).readlines()] # split into lines and strip excess whitespace

    filelines = remove_comments(filelines)

    beautify_list = []

    for line in filelines:
        formatted_line = ' '.join(format_item(line)).strip()
        beautify_list.append(formatted_line)

    beautify_str = '\n'.join(beautify_list) # joining list together to a string

    return beautify_str

if __name__ == '__main__':

    print('\n--------------Executing Part 1-----------------\n')

    beautify_str = beautify('finalv1.txt')
    print('**********Beautified String**********\n' + beautify_str)

    print('\nSaving Beautified String to file: finalv2.txt')
    with open('finalv2.txt', 'w+') as file:
        file.write(beautify_str)

'''
Example Output:

**********Beautified String**********
program a2016 ;
var
a1 , b2a , c , bal2 : integer ;
begin
a1 = 3 ;
b2a = 4 ;
c = 5 ;
print( c ) ;
bal2 = al * ( b2a+2*c ) ;
print( bal2 ) ;
end.

Saving Beautified String to file: finalv2.txt

'''