from qalb import token as tkn


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

    with open(file_name, 'r') as file:
        # Flag for "Not processing tokens for comment"
        is_comment = False
        # Flag for "Not processing tokens for string"
        is_string = False
        py_content = ""
        line_no = 0
        for py_line in file:
            line_no += 1
            py_line = py_line.replace("\u202b", "")
            py_line = py_line.replace("\u202c", "")
            py_line = py_line.replace("،", ",")
            py_line = py_line.replace("‬؛", ";")
            buffer = ''
            token = ''
            # blackout = False
            char_no = 0
            for char in py_line:
                char_no += 1
                # All condition were separate initially.
                # It is merged in order to code maintenance for now.
                # It is important as each symbols were supposed to be handled separately.
                # It will be separated based on the need now.
                if char == '\n' or char == ' ' or char == ':' or char == ';' or char == '.' or char == ',':
                    if buffer != '' and (not is_string or not is_comment):
                        token = buffer
                        py_line = tkn.process_token(token, py_line)
                        buffer = ''
                elif char == '#':
                    is_comment = True
                elif char == '(':
                    is_bracket = True
                    if buffer != '' and (not is_string or not is_comment):
                        token = buffer
                        py_line = tkn.process_token(token, py_line)
                        py_line = tkn.process_token(token, py_line, process_func=True)
                        buffer = ''
                    elif token != '' and (not is_string or not is_comment):
                        py_line = tkn.process_token(token, py_line, process_func=True)
                        buffer = ''
                elif char == ')':
                    is_bracket = False
                    if buffer != '' and (not is_string or not is_comment):
                        token = buffer
                        py_line = tkn.process_token(token, py_line)
                        buffer = ''
                elif char == '[':
                    is_square_bracket = True
                    if buffer != '' and (not is_string or not is_comment):
                        token = buffer
                        py_line = tkn.process_token(token, py_line)
                        buffer = ''
                elif char == ']':
                    is_square_bracket = False
                    if buffer != '' and (not is_string or not is_comment):
                        token = buffer
                        py_line = tkn.process_token(token, py_line)
                        buffer = ''
                elif char == '{':
                    is_curly_bracket = True
                    if buffer != '' and (not is_string or not is_comment):
                        token = buffer
                        py_line = tkn.process_token(token, py_line)
                        buffer = ''
                elif char == '}':
                    is_curly_bracket = True
                    if buffer != '' and (not is_string or not is_comment):
                        token = buffer
                        py_line = tkn.process_token(token, py_line)
                        buffer = ''
                elif char == '\"' or char == '\'':
                    is_string = not is_string
                elif (char == '=' or char == '!' or char == '<' or char == '>' or char == '+' or char == '-'
                        or char == '%' or char == '/' or char == '*' or char == '^' or char == '==' or char == '!='
                        or char == '<=' or char == '>=' or char == '+=' or char == '-=' or char == '%='
                        or char == '/=' or char == '*=' or char == '^='):
                    if buffer != '' and (not is_string or not is_comment):
                        token = buffer
                        py_line = tkn.process_token(token, py_line)
                        buffer = ''
                else:
                    buffer += char

            py_content += py_line

    file_split = file_name.split(".")
    py_file = file_split[0] + ".py"
    f = open(py_file, "w")
    f.write(py_content)
