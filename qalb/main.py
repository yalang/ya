import qalb.token_util as util
import token
import json
import os
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, 'py/ar/numbers.json')) as f:
    num_dict = json.load(f)
with open(os.path.join(script_dir, 'py/ar/keywords.json')) as f:
    keyword_dict = json.load(f)
with open(os.path.join(script_dir, 'py/ar/functions.json')) as f:
    func_dict = json.load(f)


# def process_keyword(token):
#     # If the token is a arabic number it will return english number
#     if token[0] in num_dict.keys():
#         return ''.join([num_dict[c] for c in token]), True
#
#     # If the token matches any python keywords it returns that keywords
#     if token in keyword_dict.keys():
#         return keyword_dict[token], True
#
#     # If nothing matches it returns token as it
#     return token, False
#
#
# def process_func(token):
#     # If the token matches any python in built it returns that function name
#     if token in func_dict.keys():
#         return func_dict[token], True
#
#     # If nothing matches it returns token as it
#     return token, False
#
#
# def push_token(token, is_symbol=False, stack=[]):
#     last_token = ""
#     if len(stack):
#         last_token = stack.pop()
#
#     if is_symbol and last_token == " ":
#         stack.append(token)
#     else:
#         stack.append(last_token)
#         stack.append(token)
#
#     return stack


def main(file_name):
    tokens = []  # Store all the token. not being used may used in future
    # Flag for string
    is_string = False
    is_string_single = False
    is_string_double = False

    if os.path.isdir(file_name):
        pass
    # Storing as list for matching each symbol by using 'in' identifier
    operators = ['=', '!', '<', '>', '+', '-', '%', '/', '*', '^']
    symbols = ['\n', ' ', '#', '\"', '\'', ':', ';', '.', ',', '@']
    brackets = ['(', ')', '[', ']', '{', '}']

    with open(file_name, 'r') as file:
        py_content = ""  # store all the processed line or py_line
        line_no = 0  # store the characters position
        for line in file:
            line_no += 1
            # Flag for comment
            is_comment = False

            # Replace unicode and other arabic character to english.
            line = line.replace("\u202b", "")
            line = line.replace("\u202c", "")
            line = line.replace("،", ",")
            line = line.replace("‬؛", ";")
            line = line.replace("٪", "%")
            tokens = tokens + util.tokenize(line=line, line_no=line_no)

            buffer = ''  # Store buffer
            token = ''  # token to store buffer for processing
            token_processed = False  # to store if the token was process or not
            py_line = ""  # new line to store all characters and processed buffer or buffer
            char_no = 0  # store the characters position
            for character in line:
                char_no += 1
                # All condition were separate initially.
                # It is merged in order to code maintenance for now.
                # It is important as each symbols were supposed to be handled separately.
                # It will be separated based on the need now.
                #
                # When iterating over characters, two case happens
                # Either character goes back to the line or goes to the buffer
                # Buffer gets process and than attached to the line and get emptied.
                # If the buffer didn't get processed since it was in a string or comment
                # then it get attached to the line anyway and get emptied.
                # Buffer needs to be emptied either it get processed or not before getting attached to the line.
                #
                # If a character does not match any symbol then it goes to the buffer.
                # Buffer than become a token when a character is symbol or space or new line to be processed.
                # After the token is processed it get back attached to the line.
                #
                # CONCLUSION: A character either get attached back to line or goes to the buffer
                # to become a token which get processed and than attached to the line and buffer get empty.
                # If the buffer is not empty it means it is not processed due to string or comment.
                # But its need to be clear and appended to the line.
                if character == '\"' or character == '\'':
                    if not is_comment:
                        is_string = not is_string
                    # If buffer is not empty it means it not been processed. Append it to the line and empty it
                    if buffer != '':
                        py_line += buffer
                        buffer = ''
                    py_line += character  # Attached back to the new line
                elif character == '#':
                    if not is_string:
                        # Do not process if it string. If it is string comment will not work
                        is_comment = True

                    # Process even if it is string
                    # If buffer is not empty it means it not been processed. Append it to the line and empty it
                    if buffer != '':
                        py_line += buffer
                        buffer = ''
                    py_line += character  # Attached back to the new line
                elif character == '(':
                    if not (is_string or is_comment):
                        # Do not process if it string or comment
                        if buffer != '':
                            token = buffer
                            token, token_processed = util.change_keyword(token=token, num_dict=num_dict, keyword_dict=keyword_dict)  # Processed for keyword
                            token, token_processed = util.change_func(token=token, func_dict=func_dict)  # And then for function
                            py_line += token  # And then attached to the line
                            #  since the tokenizer symbol is ( which means the token might be an inbuilt function
                            buffer = ''
                        else:
                            # If the buffer is empty than chances are that the token has been
                            # tokenized and processed by the space and got attached to the line.
                            # But we need that token to be processed as function,
                            # because that might be an inbuilt function.
                            # So we take last processed token and see if its not been processed then
                            # process it for function. If it is processed then replace the token with processed token
                            # We don't append it here since we can not append, as it is already appended
                            # so we replaced it.
                            if token != "" and not token_processed:
                                r_token, r_token_processed = util.change_func(token=token, func_dict=func_dict)
                                if r_token_processed:
                                    py_line = py_line.replace(token, r_token)

                    # Process even if it string or comment.
                    # If buffer is not empty it means it not been processed. Append it to the line and empty it
                    if buffer != '':
                        py_line += buffer
                        buffer = ''
                    py_line += character  # Attached back to the new line
                # If it is comment or string do not process as tokens
                elif character in symbols + operators + brackets:
                    if not (is_string or is_comment):
                        # Do not process if it string or comment
                        if buffer != '':
                            token = buffer
                            token, token_processed = util.change_keyword(token=token, num_dict=num_dict, keyword_dict=keyword_dict)  # Processed for keyword
                            py_line += token  # And than attached to the line
                            buffer = ''

                    # Process even if it string or comment.
                    # If buffer is not empty it means it not been processed. Append it to the line and empty it
                    if buffer != '':
                        py_line += buffer
                        buffer = ''

                    py_line += character  # Attached back to the new line
                else:
                    buffer += character  # Attached to the buffer to be processed as token
            # Finally appending line to the content of the file
            py_content += py_line

    # Splitting file name to remove existing extension in order to add python extension
    file_split = file_name.split(".")
    # Name of the python file to be created
    py_file = file_split[0] + ".py"
    # Creating the python file
    f = open(py_file, "w")
    # And then writing content to the python file
    f.write(py_content)

    print(tokens)
