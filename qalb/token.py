keywords = {
        'زائف': 'False',
        'لااحد': 'None',
        'صحيح': 'True',
        'و': 'and',
        'مثل': 'as',
        'أكد': 'assert',
        'كسر': 'break',
        'صنف': 'class',
        'استمر': 'continue',
        'حدد': 'def',
        'حذف': 'del',
        'آخرلو': 'elif',
        'آخر': 'else',
        'إلا': 'except',
        'أخيرا': 'finally',
        'لأن': 'for',
        'من': 'from',
        'عالمي': 'global',
        'لو': 'if',
        'استيراد': 'import',
        'في': 'in',
        'يساوي': 'is',
        'امدا': 'lambda',
        'غيرمحلي': 'nonlocal',
        'لا': 'not',
        'أو': 'or',
        'مرر': 'pass',
        'رفع': 'raise',
        'إرجاع': 'return',
        'حاول': 'try',
        'بينما': 'while',
        'مع': 'with',
        'محصول': 'yield'
    }

func_dict = {
        'مطلق': 'abs', '': 'delattr', 'مزيج': 'hash', '': 'memoryview', 'مجموعة': 'set',
        'كل': 'all', 'قاموس': 'dict', 'مساعدة': 'help', 'أدنى': 'min', '': 'setattr',
        '': 'any', '': 'dir', '': 'hex', '': 'next', '': 'slice',
        '': 'ascii', '': 'divmod', '': 'id', '': 'object', '': 'sorted',
        '': 'bin', '': 'enumerate', '': 'input', '': 'oct', '': 'staticmethod',
        '': 'bool', '': 'eval', '': 'int', 'افتح': 'open', '': 'str',
        '': 'breakpoint', '': 'exec', '': 'isinstance', '': 'ord', '': 'sum',
        '': 'bytearray', '': 'filter', '': 'issubclass', '': 'pow', '': 'super',
        '': 'bytes', '': 'float', '': 'iter', 'اكتب': 'print', '': 'tuple',
        '': 'callable', 'شكل': 'format', 'الطول': 'len', '': 'property', 'نوع': 'type',
        '': 'chr', '': 'frozenset', '': 'list', '': 'range', '': 'vars',
        '': 'classmethod', '': 'getattr', '': 'locals', '': 'repr', '': 'zip',
        '': 'compile', '': 'globals', '': 'map', '': 'reversed', '': '__import__',
        '': 'complex', '': 'hasattr', 'أقصى': 'max', '': 'round'
    }


def replace_keyword(word):
    # If the token is a arabic number it will replace with numbers
    if word is not "" and (word[0] == "٠" or word[0] == "١" or word[0] == "٢" or word[0] == "٣" or word[0] == "٤"
                           or word[0] == "٥" or word[0] == "٦" or word[0] == "٧" or word[0] == "٨" or word[0] == "٩"):
        num_dict = {"٠": "0", "١": "1", "٢": "2", "٣": "3", "٤": "4", "٥": "5", "٦": "6", "٧": "7", "٨": "8", "٩": "9"}
        return ''.join([num_dict[c] for c in word])

    # If the token matches any python keywords it replaces it with the keywords
    for key, value in keywords.items():
        if word == key:
            return value
    return False


def replace_function(word):
    # If the token matches any python in built it replaces it with the function name
    for key, value in func_dict.items():
        if word == key:
            return value
    return False


def process_token(token, line, process_func=False):
    if token != '':
        if process_func:
            r_func = replace_function(word=token)
            # If there is a inbuilt function name for this token, it will replace in the line
            if r_func:
                line = line.replace(token, r_func)
        else:
            r_tkn = replace_keyword(word=token)
            # If there is a keyword to replace, it will replace in the line
            if r_tkn:
                line = line.replace(token, r_tkn)
    return line
