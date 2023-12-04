import regex as re
from utilities import input_to_list, clean_text

RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14

CUBES_IN_BAG = {"red": RED_CUBES, "green": GREEN_CUBES, "blue": BLUE_CUBES}


def get_game_id(text: str) -> (int, str):
    line_parts = text.split(":")
    return int(line_parts[0].split(" ")[1]), line_parts[1]


def search_cubes(text: str) -> list:
    pattern = r"(^a(?=\s)|red|green|blue|[0-9]+)"
    return re.findall(pattern, text)


def get_possible_matches(cube_items: list) -> bool:
    number = 0
    color = None
    for item in cube_items:
        if item.isdigit():
            number = int(item)
        else:
            color = item
            if number != 0 and color in CUBES_IN_BAG.keys() and number > CUBES_IN_BAG[color]:
                return False
            # reset variables
            number = 0
            color = None

    return True


def get_game_result(c_game_set: str) -> bool:
    for c_match in c_game_set.split(";"):
        c_cubes = search_cubes(c_match)
        match_result = get_possible_matches(c_cubes)
        if match_result is False:
            return False
    return True


list_input = input_to_list("input.txt")
final_results = []
for line in list_input:
    g_id, game_set = get_game_id(line)
    print(f"Game id: {g_id}")
    game_result = get_game_result(game_set)
    print(f"game is possible: {game_result}")
    if game_result is True:
        final_results.append(g_id)

print(sum(final_results))
