def input_to_list(path):
    with open(path, "r") as f:
        return f.readlines()


def clean_text(text):
    return text.strip()
