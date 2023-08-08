def robot_circle(input_commands: str) -> bool:
    # commands
        # U = 1
        # D = -1
        # L = -1
        # R = 1
    commands = {"U": 1, "D": -1, "L": -1, "R": 1}
    # create two vars to track x val and y val
    x, y = 0, 0
    # iterate through input commands
    for command in input_commands:
        if command == "U" or command == "D":
            y += commands[command]
        if command == "L" or command == "R":
            x += commands[command]
        # if command is U or D update y val
        # if command is L or R update x val
    return True if x == 0 and y == 0 else False


def self_dividing_num(left: int, right: int) -> list[int]:
    # initialize res var
    res = []
    # iterate through range on nums from left to right
    for i in range(left, right + 1):
        if is_self_dividing(i):
            res.append(i)

    return res

def is_self_dividing(num: int) -> bool:
    num_str = str(num)
    for val in num_str:
        if int(val) == 0 or num % int(val) != 0:
            return False

    return True


print(self_dividing_num(1, 22) == [1,2,3,4,5,6,7,8,9,11,12,15,22])
