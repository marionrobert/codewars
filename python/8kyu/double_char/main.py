# my solution
def double_char(string):
    output = ""
    for n in range(len(string)):
        output += (string[n] * 2)
    return output

# better solution
def double_char(string):
    return ''.join(char * 2 for char in string)
