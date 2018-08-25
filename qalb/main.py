import qalb.util as util
import json
import os


script_dir = os.path.dirname(__file__)
# with open(os.path.join(script_dir, 'py/ar/numbers.json')) as f:
#     num_dict = json.load(f)
# with open(os.path.join(script_dir, 'py/ar/keywords.json')) as f:
#     keyword_dict = json.load(f)
# with open(os.path.join(script_dir, 'py/ar/functions.json')) as f:
#     func_dict = json.load(f)


def main(file_name):

    num_dict = {
      "٠": "0",
      "١": "1",
      "٢": "2",
      "٣": "3",
      "٤": "4",
      "٥": "5",
      "٦": "6",
      "٧": "7",
      "٨": "8",
      "٩": "9"
    }

    keyword_dict = {
      "زائف":    "False",
      "لااحد":    "None",
      "صحيح":    "True",
      "و":       "and",
      "مثل":     "as",
      "أكد":     "assert",
      "اكسر":    "break",
      "صنف":     "class",
      "استمر":   "continue",
      "وظيفة":   "def",
      "حذف":     "del",
      "ولو":     "elif",
      "آخر":     "else",
      "إلا":      "except",
      "أخيرا":   "finally",
      "لأن":      "for",
      "من":      "from",
      "عالمي":   "global",
      "لو":      "if",
      "استيراد": "import",
      "في":      "in",
      "يساوي":   "is",
      "امدا":    "lambda",
      "غيرمحلي": "nonlocal",
      "لا":       "not",
      "أو":      "or",
      "مرر":     "pass",
      "رفع":     "raise",
      "إرجاع":   "return",
      "حاول":    "try",
      "بينما":   "while",
      "مع":      "with",
      "محصول":   "yield",
      "منطقية":  "bool",
      "عدد":     "int",
      "عشري":    "float",
      "خيط":     "string"
    }

    if os.path.isdir(file_name):
        # TODO: If the file name is directory then it will search all the file with *.قلب and process all file
        pass

    py_content = ''
    # Appending print function code to the file
    with open(os.path.join(script_dir, 'include.py'), 'r') as file:
        py_content += file.read()
    # Reading file to process the text
    with open(file_name, 'r') as file:
        py_content += util.process(file, num_dict, keyword_dict)  # process store all the processed line or py_line

    # Splitting file name to remove existing extension in order to add python extension
    file_split = file_name.split(".")
    # Name of the python file to be created
    py_file = file_split[0] + ".py"
    # Creating the python file
    f = open(py_file, "w")
    # And then writing content to the python file
    f.write(py_content)
