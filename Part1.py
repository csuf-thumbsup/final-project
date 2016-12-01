import re

def remove_comments(input_str):
    pattern = re.compile('\/\*' + '(.*?)' + '\*\/') # pattern: /* (anything in between) */

    # replace all comment matches with nothing
    no_comments_str = re.sub(pattern, '' ,input_str)

    return no_comments_str

def format_item(item):
    item_list = re.split('(,|:|=|print\(|\(|\))', item)

    item_list = [item.strip() for item in item_list] # strip excess whitespace from each item

    item_list = [item for item in item_list if item] # remove empty items from list

    formatted_item = ' '.join(item_list)

    return formatted_item

def beautify(filename):
    filestr =  ''.join(open(filename).readlines()).replace('\n', '') # join file list items together to form 1 string

    filestr = remove_comments(filestr)

    filelist = re.split('(;|var|begin|end\.)', filestr) # split filestr into a list by [var, begin, end, ;] keywords/delimeters

    filelist = [item.strip() for item in filelist] # strip excess whitespace from each item

    filelist = [item for item in filelist if item] # remove empty items from list

    beautify_list = []

    for item in filelist:
        if item.startswith('program') or item.startswith('begin') or item.startswith('var') or item.startswith('end.'):
            beautify_list.append( (' '.join(subitem.strip() for subitem in re.split('\s+', item))) ) # split token then rejoin by 1 space and append to beautify_list
        elif item.startswith(';'):
            beautify_list.append(' ;') # special case for semi-colons
        else:
            beautify_list.append(format_item(item)) # format then append to beautify_list

    beautify_list = [re.sub('(;|var|begin|end\.)', r'\1\n', item) for item in beautify_list] # add a newline to [var, begin, end, ;] keywords/delimeters

    beautify_str = ''.join(beautify_list) # joining list together to a string

    return beautify_str

if __name__ == '__main__':
    beautify_str = beautify('finalv1.txt')
    print('**********Beautified String**********\n' + beautify_str)

    print('Saving Beautified String to file: finalv2.txt')
    with open('finalv2.txt', 'w') as file:
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