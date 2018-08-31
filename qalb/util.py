

def replace_en_num(number: any) -> str:
    """
    Replace en number with ar number
    :param number: any
    :return: text: str
    """
    text = str(number)
    num_dict = {"0": "٠", "1": "١", "2": "٢", "3": "٣", "4": "٤", "5": "٥", "6": "٦", "7": "٧", "8": "٨", "9": "٩"}
    for num in num_dict.keys():
        if num in text:
            text = text.replace(num, num_dict[num])
    return text
