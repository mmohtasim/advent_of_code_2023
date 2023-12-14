import re

red_limit = 12
green_limit = 13
blue_limit = 14


def values(line, line_num, low, high):
    current_game = line[low:high]
    print(current_game, f"line num:{line_num}")
    red_val, green_val, blue_val = 0, 0, 0
    red_idx = current_game.find("red")
    green_idx = current_game.find("green")
    blue_idx = current_game.find("blue")
    if red_idx != -1:
        red_val = int(current_game[red_idx - 3 : red_idx])
    if green_idx != -1:
        green_val = int(current_game[green_idx - 3 : green_idx])
    if blue_idx != -1:
        blue_val = int(current_game[blue_idx - 3 : blue_idx])

    return red_val, green_val, blue_val


with open("./day2/input", "r") as f:
    sum = 0
    for line_num, line in enumerate(f):
        start_loc = line.find(":")
        idxs = re.finditer(";", line)
        low = start_loc + 1
        game_count = len(re.findall(";", line)) + 1
        valid_game_count = 0
        for idx in idxs:
            high = idx.span()[0]
            red_val, green_val, blue_val = values(line, line_num, low, high)
            if (
                red_val <= red_limit
                and green_val <= green_limit
                and blue_val <= blue_limit
            ):
                valid_game_count += 1
                # print("possible")
            low = high + 1
        high = len(line)
        red_val, green_val, blue_val = values(line, line_num, low, high)
        if red_val <= red_limit and green_val <= green_limit and blue_val <= blue_limit:
            valid_game_count += 1
        if valid_game_count == game_count:
            sum += line_num + 1

print(sum)
