from qalb import ar_token as tkn


def main(file_name):

    # Variables for future use may.
    # If not used will be removed.
    is_import = False
    is_from = False
    is_as = False
    is_curly_bracket = False
    is_square_bracket = False
    is_bracket = False
    is_function = False
    is_class = False
    is_if = False
    is_else = False
    is_elseif = False
    is_while = False
    is_for = False
    is_try = False
    is_except = False
    is_finally = False
    is_pass = False
    is_global = False
    is_return = False
    # Flag for "Not processing tokens for string"
    is_string = False
    operators = ['=', '!', '<', '>', '+', '-', '%', '/', '*', '^',
                 '==', '!=', '<=', '>=', '+=', '-=', '%=', '/=', '*=', '^=']
    symbols = ['\n', ' ', ':', ';', '.', ',', ')', '[', ']', '{', '}']

    with open(file_name, 'r') as file:
        py_content = ""
        line_no = 0
        for line in file:
            # Flag for "Not processing tokens for comment"
            is_comment = False

            line_no += 1
            line = line.replace("\u202b", "")
            line = line.replace("\u202c", "")
            line = line.replace("،", ",")
            line = line.replace("‬؛", ";")
            line = line.replace("٪", "%")
            buffer = ''
            token = ''
            tokens = []
            py_line = ""
            char_no = 0
            for character in line:
                char_no += 1
                # All condition were separate initially.
                # It is merged in order to code maintenance for now.
                # It is important as each symbols were supposed to be handled separately.
                # It will be separated based on the need now.

                # When iterating over character, two case happens
                # FIRST: Character does not match any symbol or it is not in the string or comment
                # then it goes to the buffer. Buffer than become a token when a character
                # is symbol or space or new line to be processed.
                # After the token is processed it get back attached to the line.
                # SECOND: In rest of the cases character attached back to the line.
                # CONCLUSION: A character either get attached back to line or goes to the buffer
                # to become a token which get processed and than attached to the line.
                if character == '\"' or character == '\'':
                    is_string = not is_string
                    buffer = ''
                    py_line += character  # Attached back to the new line
                # If it is string comment will not work
                elif not is_string and character == '#':
                    is_comment = True
                    py_line += character  # Attached back to the new line
                # If it is comment or string do not process as tokens
                elif not (is_string or is_comment) and (character in symbols or character in operators):
                    if buffer != '':
                        token = buffer
                        tokens = tkn.push(token=token, symbol=character, stack=tokens)
                        py_line += tkn.process_keyword(token=token)  # Processed and than attached to the line
                        buffer = ''
                    py_line += character  # Attached back to the new line
                elif not (is_string or is_comment) and character == '(':
                    if buffer != '':
                        token = buffer
                        tokens = tkn.push(token=token, symbol=character, stack=tokens)
                        token = tkn.process_keyword(token=token)  # Processed for keyword
                        py_line += tkn.process_func(token=token)  # Than for function and than attached to the line
                        #  since the tokenizer symbol is ( which means the token might be an inbuilt function
                        buffer = ''
                    else:
                        pass
                        # TODO
                        # If the buffer is empty than chances are that the token has been
                        # tokenized and processed by the space and got attached to the line.
                        # But we need that token to be processed as function, because that might be an inbuilt function.
                    py_line += character  # Attached back to the new line
                else:
                    buffer += character  # Attached to the buffer to be processed as token

            py_content += line

            # print("tokens", tokens)

    file_split = file_name.split(".")
    py_file = file_split[0] + ".py"
    f = open(py_file, "w")
    f.write(py_content)
