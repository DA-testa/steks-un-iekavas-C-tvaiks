# python3
# Mareks Siņica-Siņavskis 221RDB430

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(char=next, position=i))

        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                return i+1
            if not are_matching(opening_brackets_stack.pop().char, next):
                return i+1
    if len(opening_brackets_stack) == 0:
        return 'Success'
    else:
        return 1


def main():
    input_type = input() # before 'Please input F for file or I for input: '
    #if input_type == 'F':
        #file_name = input()
        #try:
            #with open(file_name) as text_file:
                text = text_file.read()
        #except IOError:
            #print('Invalid file name')
            #return
    #elif input_type == 'I':
        #text = input('Please input brackets: ')
    #else:
        #print('Invalid input!')
        #return
    text = input_type[5:]
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
