import sys

def change_keyword(token, num_dict, keyword_dict):
    # If the token is a arabic number it will return english number
    if token[0] in num_dict.keys():
        return ''.join([num_dict[c] for c in token]), True

    # If the token matches any python keywords it returns that keywords
    if token in keyword_dict.keys():
        return keyword_dict[token], True

    # If nothing matches it returns token as it
    return token, False


def change_func(token, func_dict):
    # If the token matches any python in built it returns that function name
    if token in func_dict.keys():
        return func_dict[token], True

    # If nothing matches it returns token as it
    return token, False


def push_token(token, is_symbol=False, stack=[]):
    if token == "":
        return stack

    if len(stack) == 0:
        stack.append(token)
        return stack

    last_token = stack.pop()

    if is_symbol and last_token == " ":
        stack.append(token)
    else:
        stack.append(last_token)
        stack.append(token)

    return stack


def condition_buffer(character, buffer, symbols, operators):
    if not (character in symbols or character in operators):
        buffer += character
    return buffer


def simple_buffer(character, buffer):
    buffer += character
    return buffer


def tokenize(line, line_no, symbols):
    tokens = []
    buffer = ''  # Store buffer
    char_no = 0  # store the characters position
    # effected 1 is single quote string
    # effected 2 is double quote string
    # effected 3 is comment
    effected = 0
    currently_effected = False
    for character in line:
        char_no += 1
        if character in symbols:
            if character == '\'' and not effected:
                effected = 1
                currently_effected = True
            elif character == '\'' and effected is 1:
                effected = 0
            elif character == '\"' and not effected:
                effected = 2
                currently_effected = True
            elif character == '\"' and effected is 2:
                effected = 0
            elif character == '#' and not effected:
                effected = 3
                currently_effected = True
            elif character == '\n' and effected is 3:
                effected = 0
            elif character == '\n' and effected is 2:
                sys.exit("Closing string missing at line no " + str(line_no) + ":" + str(char_no))
            elif character == '\n' and effected is 1:
                sys.exit("Closing string missing at line no " + str(line_no), ":" + str(char_no))

            if effected and not currently_effected:
                buffer += character
            else:
                if buffer != '':
                    tokens = push_token(token=buffer, is_symbol=False, stack=tokens)
                    buffer = ''
                tokens = push_token(token=character, is_symbol=True, stack=tokens)
            currently_effected = False
        else:
            buffer += character  # Attached to the buffer to be processed as token

    return tokens
