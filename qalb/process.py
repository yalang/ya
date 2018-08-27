import sys
from qalb.enum.effected import Effected
from qalb.enum.token_error import TokenError
import qalb.util as util


class Process:

    def __init__(self, file, num_dict: dict, keyword_dict: dict):
        self.file = file
        self.num_dict: dict = num_dict
        self.keyword_dict: dict = keyword_dict
        self.line: str = ''
        self.buffer: str = ''
        self.token: str = ''
        self.las_symbol: str = ''
        self.next_symbol: str = ''
        self.current_symbol: str = ''
        self.effected: Effected = Effected.AS_NONE
        self.line_no: int = 0
        self.char_no: int = 0

        self.operators: str = '=!<>+-%/*^'
        self.symbols: str = '#\"\':;.,@'
        self.brackets: str = '()[]{}'
        self.all_symbols: str = self.operators + self.symbols + self.brackets

    def report_error(self, error: TokenError) -> None:
        error_str = error.value + " " + " في رقم الخط " \
                    + util.replace_en_num(self.line_no) + ":" + util.replace_en_num(self.char_no)
        error_str = self.line + '\n' + error_str
        sys.exit(error_str)

    def change_number(self) -> None:
        if self.token is None or self.token == '':
            return
        new_token = ''
        for c in self.token:
            if c in self.num_dict.keys():
                new_token += self.num_dict[c]
            else:
                self.report_error(TokenError.INVALID_TOKEN)
        self.token = new_token

    def change_keyword(self) -> bool:
        if self.token is None or self.token == '':
            return False

        # If the token is a arabic number it will return english number
        if self.token[0] in self.num_dict.keys():
            self.change_number()
            return True
            # return ''.join([num_dict[c] for c in token]), True

        # If the token matches any python keywords it returns that keywords
        if self.token in self.keyword_dict.keys():
            self.token = self.keyword_dict[self.token]
            return True

        # If nothing matches it returns token as it
        return False

    def process_line(self):

        py_line = ''  # new line to store all characters and processed buffer or buffer

        self.buffer = ''  # Store buffer
        self.char_no = 0  # store the characters position
        self.effected = Effected.AS_NONE

        for character in self.line:
            self.char_no += 1
            if character == " " or character == "\n" or character in self.all_symbols:
                special_character = character  # Since it is special char

                if special_character == '\'' and self.effected is Effected.AS_NONE:
                    self.effected = Effected.AS_SINGLE_QUOTE_STRING
                elif special_character == '\'' and self.effected is Effected.AS_SINGLE_QUOTE_STRING:
                    self.effected = Effected.AS_NONE
                elif special_character == '\"' and self.effected is Effected.AS_NONE:
                    self.effected = Effected.AS_DOUBLE_QUOTE_STRING
                elif special_character == '\"' and self.effected is Effected.AS_DOUBLE_QUOTE_STRING:
                    self.effected = Effected.AS_NONE
                elif special_character == '#' and self.effected is Effected.AS_NONE:
                    self.effected = Effected.AS_COMMENT
                elif special_character == '\n' and self.effected is Effected.AS_COMMENT:
                    self.effected = Effected.AS_NONE
                elif special_character == '\n' and self.effected is Effected.AS_DOUBLE_QUOTE_STRING:
                    self.report_error(TokenError.INCOMPLETE_STRING)
                elif special_character == '\n' and self.effected is Effected.AS_SINGLE_QUOTE_STRING:
                    self.report_error(TokenError.INCOMPLETE_STRING)

                if self.buffer != '':
                    self.token = self.buffer
                    token_processed = self.change_keyword()  # Processed for keyword
                    py_line += self.token
                    self.buffer = ''
                    self.token = ''
                py_line += special_character
            else:
                if self.effected is Effected.AS_NONE:
                    self.buffer += character
                else:
                    py_line += character

        return py_line

    def process(self):

        py_content = ""  # store all the processed line or py_line
        # line_no = 0  # store the characters position
        for line in self.file:
            self.line_no += 1

            # Replace unicode and other arabic character to english.
            line = line.replace("\u202b", "")
            line = line.replace("\u202c", "")
            line = line.replace("،", ",")
            line = line.replace("؛", "")
            line = line.replace("٪", "%")

            self.line = line

            # Finally appending line to the content of the file
            py_content += self.process_line()

        return py_content
