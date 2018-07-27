import مفيد.الكلمات as الكلمات

keywords = الكلمات.قاموس_الكلمات()
def replace_keyword(word):
    if word is not "" and (word[0] == "٠" or word[0] == "١" or word[0] == "٢" or word[0] == "٣" or word[0] == "٤" or word[0] == "٥" or word[0] == "٦" or word[0] == "٧" or word[0] == "٨" or word[0] == "٩"):
        عدد = {"٠": "0", "١": "1", "٢": "2", "٣": "3", "٤": "4", "٥": "5", "٦": "6", "٧": "7", "٨": "8",
                              "٩": "9"}
        return ''.join([عدد[c] for c in word])

    for key, value in keywords.items():
        if word == key:
            return value
    return False


def process_token(buffer, line):
    global replace_token
    replace_token = replace_keyword(buffer)
    if replace_token:
        line = line.replace(buffer, replace_token)
    return line