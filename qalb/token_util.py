import sys
from qalb.enum.effected import Effected


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

    if token == " ":
        return stack

    if token == "\n":
        return stack

    if len(stack) == 0:
        stack.append(token)
        return stack

    stack.append(token)

    # last_token = stack.pop()
    #
    # if is_symbol and last_token == " ":
    #     stack.append(token)
    # else:
    #     stack.append(last_token)
    #     stack.append(token)

    return stack


def tokenize(line, line_no):

    operators = '=!<>+-%/*^'
    symbols = '#\"\':;.,@'
    brackets = '()[]{}'

    tokens = []
    buffer = ''  # Store buffer
    char_no = 0  # store the characters position
    # effected 1 is single quote string
    # effected 2 is double quote string
    # effected 3 is comment
    # effected
    effected = Effected.AS_NONE
    currently_effected = False
    last_symbol = ""
    for character in line:
        char_no += 1
        if character == " " or character == "\n" or character in (symbols + operators + brackets):
            special_character = character # Since it is special char
            if special_character == '\'' and effected is Effected.AS_NONE:
                effected = Effected.AS_SINGLE_QUOTE_STRING
                currently_effected = True
            elif special_character == '\'' and effected is Effected.AS_SINGLE_QUOTE_STRING:
                effected = Effected.AS_NONE
            elif special_character == '\"' and effected is Effected.AS_NONE:
                effected = Effected.AS_DOUBLE_QUOTE_STRING
                currently_effected = True
            elif special_character == '\"' and effected is Effected.AS_DOUBLE_QUOTE_STRING:
                effected = Effected.AS_NONE
            elif special_character == '#' and effected is Effected.AS_NONE:
                effected = Effected.AS_COMMENT
                currently_effected = True
            elif special_character == '\n' and effected is Effected.AS_COMMENT:
                effected = Effected.AS_NONE
                # Replacing # with ; since we are ignoring new line character.
                # But in order to detect the end of statement we have replaced it with ;
                special_character = ';'
            elif special_character == '\n' and effected is Effected.AS_DOUBLE_QUOTE_STRING:
                sys.exit("Closing string missing at line no " + str(line_no) + ":" + str(char_no))
            elif special_character == '\n' and effected is Effected.AS_SINGLE_QUOTE_STRING:
                sys.exit("Closing string missing at line no " + str(line_no), ":" + str(char_no))

            if effected is not Effected.AS_NONE and not currently_effected:
                buffer += special_character
            else:
                if buffer != '':
                    tokens = push_token(token=buffer, is_symbol=False, stack=tokens)
                    buffer = ''
                tokens = push_token(token=special_character, is_symbol=True, stack=tokens)
                last_symbol = special_character
            currently_effected = False
        else:
            buffer += character

    return tokens


def untokenize(file_tokens):
    line_no = 0
    src_content = ""
    for line_tokens in file_tokens:
        line_no += 1
        src_line = ""
        for token in line_tokens:
            if token == ";":
                src_line += "\n"
            else:
                src_line += token
        src_content += src_line

    return src_content
