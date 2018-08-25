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


def replace_num(text):
    num_dict = {"0": "٠", "1": "١", "2": "٢", "3": "٣", "4": "٤", "5": "٥", "6": "٦", "7": "٧", "8": "٨", "9": "٩"}
    for num in num_dict.keys():
        if num in text:
            text = text.replace(num, num_dict[num])
    return text


def process(file, num_dict, keyword_dict):

    py_content = ""  # store all the processed line or py_line
    line_no = 0  # store the characters position
    for line in file:
        line_no += 1

        # Replace unicode and other arabic character to english.
        line = line.replace("\u202b", "")
        line = line.replace("\u202c", "")
        line = line.replace("،", ",")
        line = line.replace("؛", "")
        line = line.replace("٪", "%")

        # Finally appending line to the content of the file
        py_content += process_line(line, line_no, num_dict, keyword_dict)

    return py_content


def process_line(line, line_no, num_dict, keyword_dict):

    operators = '=!<>+-%/*^'
    symbols = '#\"\':;.,@'
    brackets = '()[]{}'

    buffer = ''  # Store buffer
    py_line = ''  # new line to store all characters and processed buffer or buffer

    char_no = 0  # store the characters position
    effected = Effected.AS_NONE
    currently_effected = False  # If is effected and is effected in current loop then true

    for character in line:
        char_no += 1
        if character == " " or character == "\n" or character in (symbols + operators + brackets):
            special_character = character  # Since it is special char

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
            elif special_character == '\n' and effected is Effected.AS_DOUBLE_QUOTE_STRING:
                sys.exit(replace_num("هناك مشكلة في رقم الخط " + str(line_no) + ":" + str(char_no)))
            elif special_character == '\n' and effected is Effected.AS_SINGLE_QUOTE_STRING:
                sys.exit(replace_num("هناك مشكلة في رقم الخط " + str(line_no), ":" + str(char_no)))

            if effected is not Effected.AS_NONE and not currently_effected:
                buffer += special_character
            else:
                if buffer != '':
                    buffer, token_processed = change_keyword(token=buffer, num_dict=num_dict, keyword_dict=keyword_dict)  # Processed for keyword
                    py_line += buffer
                    buffer = ''
                py_line += special_character
            currently_effected = False
        else:
            buffer += character

    return py_line
