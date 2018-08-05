import sys
from qalb.enum.effected import Effected
from qalb.enum.identified import Identified
from qalb.enum.bracket import Bracket


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


# def condition_buffer(character, buffer, symbols, operators):
#     if not (character in symbols or character in operators):
#         buffer += character
#     return buffer
#
#
# def simple_buffer(character, buffer):
#     buffer += character
#     return buffer


# def process_tokens(tokens, line_no, symbols):
#     # tokens = []
#     # buffer = ''  # Store buffer
#     # char_no = 0  # store the characters position
#     # effected 1 is single quote string
#     # effected 2 is double quote string
#     # effected 3 is comment
#     # effected
#     effected = 0
#     currently_effected = False
#     for token in tokens:
#         # char_no += 1
#         if token in symbols:
#             if token == '\'' and not effected:
#                 effected = Effected.AS_SINGLE_QUOTE_STRING
#                 currently_effected = True
#             elif token == '\'' and effected is 1:
#                 effected = 0
#             elif token == '\"' and not effected:
#                 effected = 2
#                 currently_effected = True
#             elif token == '\"' and effected is 2:
#                 effected = 0
#             elif token == '#' and not effected:
#                 effected = 3
#                 currently_effected = True
#             elif token == '\n' and effected is 3:
#                 effected = 0
#             elif token == '\n' and effected is 2:
#                 sys.exit("Closing string missing at line no " + str(line_no) + ":" + str(char_no))
#             elif token == '\n' and effected is 1:
#                 sys.exit("Closing string missing at line no " + str(line_no), ":" + str(char_no))
#
#             if effected and not currently_effected:
#                 buffer += token
#             else:
#                 if buffer != '':
#                     tokens = push_token(token=buffer, is_symbol=False, stack=tokens)
#                     buffer = ''
#                 tokens = push_token(token=token, is_symbol=True, stack=tokens)
#             currently_effected = False
#         else:
#             buffer += token  # Attached to the buffer to be processed as token
#
#     return tokens


# def simply_tokenize(line, line_no, symbols):
#     tokens = []
#     buffer = ''  # Store buffer
#     char_no = 0  # store the characters position
#
#     for character in line:
#         char_no += 1
#         if character in symbols:
#             if buffer != '':
#                 tokens.append(buffer)
#                 buffer = ''
#             tokens.append(character)
#         else:
#             buffer += character  # Attached to the buffer to be processed as token
#
#     return tokens


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
    effected = 0
    currently_effected = False
    for character in line:
        char_no += 1
        if character == " " or character == "\n" or character in (symbols + operators + brackets):
            if character == '\'' and not effected:
                effected = Effected.AS_SINGLE_QUOTE_STRING
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
