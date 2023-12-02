def input_to_list(path: str) -> list:
    with open(path, "r") as f:
        return f.readlines()


def clean_text(text: str) -> str:
    return text.strip()
