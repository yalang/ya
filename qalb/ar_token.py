# keyword_dict = {
#         'زائف': 'False',
#         'لااحد': 'None',
#         'صحيح': 'True',
#         'و': 'and',
#         'مثل': 'as',
#         'أكد': 'assert',
#         'كسر': 'break',
#         'صنف': 'class',
#         'استمر': 'continue',
#         'حدد': 'def',
#         'حذف': 'del',
#         'آخرلو': 'elif',
#         'آخر': 'else',
#         'إلا': 'except',
#         'أخيرا': 'finally',
#         'لأن': 'for',
#         'من': 'from',
#         'عالمي': 'global',
#         'لو': 'if',
#         'استيراد': 'import',
#         'في': 'in',
#         'يساوي': 'is',
#         'امدا': 'lambda',
#         'غيرمحلي': 'nonlocal',
#         'لا': 'not',
#         'أو': 'or',
#         'مرر': 'pass',
#         'رفع': 'raise',
#         'إرجاع': 'return',
#         'حاول': 'try',
#         'بينما': 'while',
#         'مع': 'with',
#         'محصول': 'yield'
#     }
#
# type_dict = {
#         'منطقية': 'bool',
#         'عدد': 'int',
#         'عشري': 'float',
#         'خيط': 'string'
#     }
#
# num_dict = {"٠": "0", "١": "1", "٢": "2", "٣": "3", "٤": "4", "٥": "5", "٦": "6", "٧": "7", "٨": "8", "٩": "9"}
#
# func_dict = {
#         'مطلق': 'abs', '': 'delattr', 'مزيج': 'hash', '': 'memoryview', 'مجموعة': 'set',
#         'كل': 'all', 'قاموس': 'dict', 'مساعدة': 'help', 'أدنى': 'min', '': 'setattr',
#         'أي': 'any', 'دليل': 'dir', '': 'hex', 'بعد': 'next', '': 'slice',
#         '': 'ascii', '': 'divmod', '': 'id', '': 'object', '': 'sorted',
#         '': 'bin', '': 'enumerate', 'إدخال': 'input', '': 'oct', '': 'staticmethod',
#         '': 'bool', '': 'eval', '': 'int', 'افتح': 'open', '': 'str',
#         '': 'breakpoint', '': 'exec', '': 'isinstance', '': 'ord', '': 'sum',
#         '': 'bytearray', '': 'filter', '': 'issubclass', '': 'pow', '': 'super',
#         '': 'bytes', '': 'float', '': 'iter', 'اكتب': 'print', '': 'tuple',
#         '': 'callable', 'شكل': 'format', 'الطول': 'len', '': 'property', 'نوع': 'type',
#         '': 'chr', '': 'frozenset', '': 'list', 'نطاق': 'range', '': 'vars',
#         '': 'classmethod', '': 'getattr', '': 'locals', '': 'repr', '': 'zip',
#         '': 'compile', '': 'globals', '': 'map', '': 'reversed', '': '__import__',
#         '': 'complex', '': 'hasattr', 'أقصى': 'max', '': 'round'
#     }
#
#
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
# def push_token(token, symbol, stack):
#     if token == '':
#         token = stack.pop()
#
#     if symbol != " " and token == " ":
#         stack.append(symbol)
#     else:
#         stack.append(token)
#         stack.append(symbol)
#
#     return stack
