from src.process import Process
from src.enum.file_error import FileError
import os
import sys
script_dir = os.path.dirname(__file__)

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
    "٩": "9",
}

keyword_dict = {
    "صحيح": "True",
    "كاذب": "False",
    "لااحد": "None",
    "مثل": "as",
    "اكد": "assert",
    "غيرمتزامن": "async",
    "و": "and",
    "ترقب": "await",
    "اكسر": "break",
    "صنف": "class",
    "استمر": "continue",
    "وظيفة": "def",
    "حذف": "del",
    "ولو": "elif",
    "اخر": "else",
    "الا": "except",
    "اخيرا": "finally",
    "لكل": "for",
    "من": "from",
    "عالمي": "global",
    "لو": "if",
    "استيراد": "import",
    "في": "in",
    "يساوي": "is",
    "امدا": "lambda",
    "لا": "not",
    "غيرمحلي": "nonlocal",
    "او": "or",
    "مرر": "pass",
    "رفع": "raise",
    "ارجع": "return",
    "حاول": "try",
    "بينما": "while",
    "مع": "with",
    "محصول": "yield",
    "منطقية": "bool",
    "عدد": "int",
    "عشري": "float",
    "خيط": "string",
}

function_dict = {
    "مطلق": "abs",
    "": "delattr",
    "مزيج": "hash",
    "": "memoryview",
    "مجموعة": "set",
    "كل": "all",
    "قاموس": "dict",
    "مساعدة": "help",
    "أدنى": "min",
    "": "setattr",
    "أي": "any",
    "دليل": "dir",
    "": "hex",
    "بعد": "next",
    "شريحة": "slice",
    "أسكي": "ascii",
    "": "divmod",
    "": "id",
    "": "object",
    "رتب": "sorted",
    "": "bin",
    "": "enumerate",
    "إدخال": "input",
    "": "oct",
    "": "staticmethod",
    "منطقية": "bool",
    "": "eval",
    "عدد": "int",
    "افتح": "open",
    "": "str",
    "نقطةكسر": "breakpoint",
    "": "exec",
    "": "isinstance",
    "": "ord",
    "": "sum",
    "": "bytearray",
    "": "filter",
    "": "issubclass",
    "": "pow",
    "ممتاز": "super",
    "بايت": "bytes",
    "عشري": "float",
    "": "iter",
    "": "tuple",
    "للاستدعاء": "callable",
    "شكل": "format",
    "الطول": "len",
    "": "property",
    "نوع": "type",
    "": "chr",
    "": "frozenset",
    "": "list",
    "نطاق": "range",
    "": "vars",
    "": "classmethod",
    "": "getattr",
    "": "locals",
    "": "repr",
    "": "zip",
    "": "compile",
    "عالمي": "globals",
    "خريطة": "map",
    "عكس": "reversed",
    "__استيراد__": "__import__",
    "": "complex",
    "": "hasattr",
    "أقصى": "max",
    "": "round",
}


def main(file_name):

    if os.path.isdir(file_name):
        # TODO: If the file name is directory then it will search all the file with *.ي and process all file
        pass
    elif os.path.isfile(file_name):
        py_content = ''
        # Appending print function code to the file
        with open(os.path.join(script_dir, 'include.py'), 'r') as file:
            py_content += file.read()

        # Reading file to process the text
        with open(file_name, 'r') as file:
            # Process all content of the file
            py_content += Process(file, num_dict, keyword_dict, function_dict).process()

        # Splitting file name to remove existing extension in order to add python extension
        file_split = file_name.split(".")
        # Name of the python file to be created
        py_file = file_split[0] + ".py"
        # Creating the python file
        f = open(py_file, "w")
        # And then writing content to the python file
        f.write(py_content)
    else:
        sys.exit("'" + file_name + "'" + " " + FileError.INVALID_FILE.value)