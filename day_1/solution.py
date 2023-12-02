import regex as re
from utilities import input_to_list, clean_text


NUMBERS = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}


def search_number_first_approach(text: str, is_reverse=False) -> str:
    if is_reverse:
        text = text[::-1]

    for character in text:
        if character.isdigit():
            return character
    raise Exception("Couldn't find any number")


def normalize_number(current_number: str, reverse=False) -> str:
    if current_number.isdigit():
        if reverse:
            return current_number[-1]
        return current_number[0]
    else:
        return NUMBERS[current_number]


def search_number_improved(text: str) -> int:
    pattern = r"(^a(?=\s)|one|two|three|four|five|six|seven|eight|nine|[0-9]+)"
    x = re.findall(pattern, text, overlapped=True)
    if len(x) < 1:
        raise Exception("No numbers found")
    first_number = normalize_number(x[0])
    last_number = normalize_number(x[-1], reverse=True)
    return int(first_number + last_number)


complete_list = []
list_input = input_to_list("input.txt")
clean_list = [clean_text(i) for i in list_input]
for line in clean_list:

    complete_list.append(search_number_improved(line))

print(sum(complete_list))





