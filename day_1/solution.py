from utilities import input_to_list, clean_text


def search_number(text, is_reverse=False):
    if is_reverse:
        text = text[::-1]

    for character in text:
        if character.isdigit():
            return character
    raise Exception("Couldn't find any number")


complete_list = []
list_input = input_to_list("input.txt")
clean_list = [clean_text(i) for i in list_input]
for i, line in enumerate(clean_list):
    first_number = search_number(clean_list[i])
    second_number = search_number(clean_list[i], is_reverse=True)
    complete_list.append(int(first_number + second_number))

print(sum(complete_list))





