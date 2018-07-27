import os
import sys
import token as tkn


def main(file_name):

    is_import = False
    is_from = False
    is_as = False
    is_comment = False
    is_string = False
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
        py_content = ""
        py_line = ""
        line_no = 0
        for line in file:
            line_no += 1
            line = line.replace("\u202b", "")
            line = line.replace("\u202c", "")
            line = line.replace("،", ",")
            line = line.replace("‬؛", ";")
            buffer = ''
            # blackout = False
            char_no = 0
            for char in line:
                char_no += 1
                # All condition were separate initially.
                # It is merged in order to code maintenance for now.
                # It is important as each symbols were supposed to be handled separately.
                # It will be separated based on the need now.
                if char == '\n' or char == ';' or char == ' ' or char == '.' or char == ',':
                    line = tkn.process_token(buffer, line)
                    buffer = ''
                elif char == '#':
                    is_comment = not is_comment
                elif char == ':':
                    line = tkn.process_token(buffer, line)
                    buffer = ''
                elif char == '(':
                    is_bracket = True
                    line = tkn.process_token(buffer, line)
                    buffer = ''
                elif char == ')':
                    is_bracket = False
                    line = tkn.process_token(buffer, line)
                    buffer = ''
                elif char == '[':
                    is_square_bracket = True
                    line = tkn.process_token(buffer, line)
                    buffer = ''
                elif char == ']':
                    is_square_bracket = False
                    line = tkn.process_token(buffer, line)
                    buffer = ''
                elif char == '{':
                    is_curly_bracket = True
                    line = tkn.process_token(buffer, line)
                    buffer = ''
                elif char == '}':
                    is_curly_bracket = True
                    line = tkn.process_token(buffer, line)
                    buffer = ''
                elif :
                    line = tkn.process_token(buffer, line)
                    buffer = ''
                elif :
                    line = tkn.process_token(buffer, line)
                    buffer = ''
                elif char == '\"' or char == '\'':
                    is_string = not is_string
                elif char == '=' or char == '!' or char == '<' or char == '>' or char == '+' or char == '-' \
                        or char == '%' or char == '/' or char == '*' or char == '^' or char == '==' or char == '!=' \
                        or char == '<=' or char == '>=' or char == '+=' or char == '-=' or char == '%=' \
                        or char == '/=' or char == '*=' or char == '^=':
                    line = tkn.process_token(buffer, line)
                    buffer = ''
                else:
                    buffer += char

            py_content += line

    file_split = file_name.split(".")
    py_file = file_split[0] + ".py"
    f = open(py_file, "w")
    f.write(py_content)

    os.system("python3 " + py_file)


if __name__ == '__main__':
    main("مرحبا.قلب")
    # main(sys.argv[1])
