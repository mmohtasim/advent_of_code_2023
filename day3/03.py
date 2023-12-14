import re


def check_up(lines, line_num, low, high):
    if line_num:
        search_str = lines[line_num - 1][low:high]
        if any(ss in search_str for ss in syms):
            return True
        else:
            return False
    else:
        return False


def check_down(lines, line_num, low, high):
    if line_num != (len(lines) - 1):
        search_str = lines[line_num + 1][low:high]
        if any(ss in search_str for ss in syms):
            return True
        else:
            return False
    else:
        return False


def check_right(lines, line_num, low, high):
    if high != len(lines[line_num]):
        try:
            if lines[line_num][high] in syms:
                return True
            else:
                return False
        except Exception as e:
            print(line_num)
            print(high)
            raise e
    else:
        return False


def check_left(lines, line_num, low, high):
    if low:
        if lines[line_num][low - 1] in syms:
            return True
        else:
            return False
    else:
        return False


def check_up_left(lines, line_num, low, high):
    if line_num and low:
        if lines[line_num - 1][low - 1] in syms:
            return True
        else:
            return False
    else:
        return False


def check_up_right(lines, line_num, low, high):
    if line_num and high != len(lines[line_num]):
        if lines[line_num - 1][high] in syms:
            return True
        else:
            return False
    else:
        return False


def check_down_left(lines, line_num, low, high):
    if line_num != (len(lines) - 1) and low:
        if lines[line_num + 1][low - 1] in syms:
            return True
        else:
            return False
    else:
        return False


def check_down_right(lines, line_num, low, high):
    if line_num != (len(lines) - 1) and high != len(lines[line_num]):
        if lines[line_num + 1][high] in syms:
            return True
        else:
            return False
    else:
        return False


def check_sides(lines, line_num, low, high):
    if (
        check_up(lines, line_num, low, high)
        or check_down(lines, line_num, low, high)
        or check_left(lines, line_num, low, high)
        or check_right(lines, line_num, low, high)
        or check_up_left(lines, line_num, low, high)
        or check_up_right(lines, line_num, low, high)
        or check_down_left(lines, line_num, low, high)
        or check_down_right(lines, line_num, low, high)
    ):
        return True
    else:
        return False


with open("./day3/input") as f:
    lines = [line.rstrip("\n") for line in f]

num_locs = []

syms = ("*", "#", "$", "+", "-", "/", "@", "%", "&", "=")

for i, line in enumerate(lines):
    num_locs.append([])
    idxs = re.finditer("\d+", line)
    for idx in idxs:
        num_locs[i].append(idx.span())


sum = 0
for line_num, line in enumerate(num_locs):
    for loc in line:
        low, high = loc
        if check_sides(lines, line_num, low, high):
            sum += int(lines[line_num][low:high])
print(sum)
