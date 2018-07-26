import مفيد.الكلمات as الكلمات
import os

keywords = الكلمات.قاموس_الكلمات()
# file_ext = "قلب"
# file_name = 'احلاـوـسحلا'
# # file_path = file_name + "." + file_ext
# file_path = file_name


def replace_keyword(word):
    if word is not "" and (word[0] == "٠" or word[0] == "١" or word[0] == "٢" or word[0] == "٣" or word[0] == "٤" or word[0] == "٥" or word[0] == "٦" or word[0] == "٧" or word[0] == "٨" or word[0] == "٩"):
        عدد = {"٠": "0", "١": "1", "٢": "2", "٣": "3", "٤": "4", "٥": "5", "٦": "6", "٧": "7", "٨": "8",
                              "٩": "9"}
        return ''.join([عدد[c] for c in word])

    for key, value in keywords.items():
        if word == key:
            return value
    return False


def do_replace_token(buffer, line):
    global replace_token
    replace_token = replace_keyword(buffer)
    if replace_token:
        line = line.replace(buffer, replace_token)
    return line


def main(file_name):
    with open(file_name, 'r') as file:
        content = ""
        for line in file:
            line = line.replace("\u202b", "")
            line = line.replace("\u202c", "")
            line = line.replace("،", ",")
            token = ''
            buffer = ''
            blackout = False
            for char in line:
                if not blackout and char == '\n':
                    line = do_replace_token(buffer, line)
                    buffer = ''
                elif not blackout and char == ' ':
                    line = do_replace_token(buffer, line)
                    buffer = ''
                elif char == '#':
                    blackout = True
                elif not blackout and char == ':':
                    line = do_replace_token(buffer, line)
                    buffer = ''
                elif not blackout and char == '(':
                    line = do_replace_token(buffer, line)
                    buffer = ''
                elif not blackout and char == ')':
                    line = do_replace_token(buffer, line)
                    buffer = ''
                elif not blackout and char == '[':
                    line = do_replace_token(buffer, line)
                    buffer = ''
                elif not blackout and char == ']':
                    line = do_replace_token(buffer, line)
                    buffer = ''
                elif not blackout and char == '{':
                    line = do_replace_token(buffer, line)
                    buffer = ''
                elif not blackout and char == '}':
                    line = do_replace_token(buffer, line)
                    buffer = ''
                elif not blackout and char == '.':
                    line = do_replace_token(buffer, line)
                    buffer = ''
                elif not blackout and char == ',':
                    line = do_replace_token(buffer, line)
                    buffer = ''
                elif char == '\"':
                    blackout = not blackout
                elif char == '\'':
                    blackout = not blackout
                elif not blackout and char == '=':
                    line = do_replace_token(buffer, line)
                    buffer = ''
                elif not blackout and char == '!':
                    line = do_replace_token(buffer, line)
                    buffer = ''
                elif not blackout and char == '<':
                    line = do_replace_token(buffer, line)
                    buffer = ''
                elif not blackout and char == '>':
                    line = do_replace_token(buffer, line)
                    buffer = ''
                elif not blackout and char == '+':
                    line = do_replace_token(buffer, line)
                    buffer = ''
                elif not blackout and char == '-':
                    line = do_replace_token(buffer, line)
                    buffer = ''
                elif not blackout and char == '%':
                    line = do_replace_token(buffer, line)
                    buffer = ''
                elif not blackout and char == '/':
                    line = do_replace_token(buffer, line)
                    buffer = ''
                elif not blackout and char == '*':
                    line = do_replace_token(buffer, line)
                    buffer = ''
                elif not blackout and char == '^':
                    line = do_replace_token(buffer, line)
                    buffer = ''
                elif not blackout and char == '==':
                    line = do_replace_token(buffer, line)
                    buffer = ''
                elif not blackout and char == '!=':
                    line = do_replace_token(buffer, line)
                    buffer = ''
                elif not blackout and char == '<=':
                    line = do_replace_token(buffer, line)
                    buffer = ''
                elif not blackout and char == '>=':
                    line = do_replace_token(buffer, line)
                    buffer = ''
                elif not blackout and char == '+=':
                    line = do_replace_token(buffer, line)
                    buffer = ''
                elif not blackout and char == '-=':
                    line = do_replace_token(buffer, line)
                    buffer = ''
                elif not blackout and char == '%=':
                    line = do_replace_token(buffer, line)
                    buffer = ''
                elif not blackout and char == '/=':
                    line = do_replace_token(buffer, line)
                    buffer = ''
                elif not blackout and char == '*=':
                    line = do_replace_token(buffer, line)
                    buffer = ''
                elif not blackout and char == '^=':
                    line = do_replace_token(buffer, line)
                    buffer = ''
                else:
                    buffer += char

            content += line

    py_file = file_name + ".py"
    f = open(py_file, "w")
    f.write(content)

    os.system("python3 " + py_file)


if __name__ == '__main__':
    main(*args[0])
