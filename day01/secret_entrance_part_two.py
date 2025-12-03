def saves_data_in_list():
    with open("../day01/data.txt", "r") as f:
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

    zero_clicks = 0   # toutes les fois où la flèche passe sur 0 (clic compris)
    zero_stops = 0    # nombre de rotations dont la position finale est 0

    sequences = parse_sequences()

    for direction, steps in sequences:
        if direction == "R":
            delta = 1
        elif direction == "L":
            delta = -1
        else:
            raise ValueError("Direction inconnue")

        # On simule chaque clic
        for _ in range(steps):
            position = (position + delta) % 100
            if position == 0:
                zero_clicks += 1

        if position == 0:
            zero_stops += 1

    print(f"Nombre total de clics sur 0 (passages + arrêts) : {zero_clicks}")
    print(f"Nombre d'arrêts sur 0 : {zero_stops}")
    print(f"Nombre de passages sans arrêt (0 traversé seulement) : {zero_clicks - zero_stops}")

set_the_dial()