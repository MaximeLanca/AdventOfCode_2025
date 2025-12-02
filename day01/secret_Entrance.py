def saves_data_in_list():
    with open("day01/data.txt", "r") as f:
        return [line.strip() for line in f]


def parse_sequences():
    sequences = saves_data_in_list()
    parsed = []

    for seq in sequences:
        direction = seq[0]
        number = int(seq[1:])
        parsed.append((direction, number))

    return parsed


def set_the_dial():
    position = 50
    zero_count = 0
    sequences = parse_sequences()

    for direction, steps in sequences:
        if direction == "R":
            position = (position + steps) % 100
        elif direction == "L":
            position = (position - steps) % 100
        else:
            raise ValueError("Direction inconnue")

        if position == 0:
            zero_count += 1

    print(f"The password is : {zero_count}")


set_the_dial()
