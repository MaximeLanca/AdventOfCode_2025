
def saves_data_in_list():
    data_list = []
    file = open("day01/data.txt","r")
    line = file.readline()

    while line != "":
        data_list.append(line.replace("\n",""))
        line = file.readline()

    return data_list


def set_the_dial():
    dial_position = 0
    dial_position_and_number = set_dial_positon_and_number()
    print(dial_position_and_number)
    #if arrow_direction == "R" :
        

def set_dial_positon_and_number():
    sequence_of_rotation = saves_data_in_list()
    redefined_sequence_of_rotation = []
    redefined_data = []
    redefined_number = []

    for sequence in sequence_of_rotation:
        arrow_direction = sequence[0]
        number = int(sequence[1:])
        print(number)
        if number > 99 :
            redefined_number = redefine_number(number)

        redefined_sequence_of_rotation.append([arrow_direction,redefined_number])

    return redefined_sequence_of_rotation

def redefine_number(sequence_number):
    terms_list = []

    while sequence_number > 99:
        sequence_number = sequence_number - 99

        if sequence_number> 99:
            terms_list.append(99)
        elif sequence_number == 0 :
            terms_list.append(0)
            return terms_list
        elif sequence_number < 99:
            terms_list.append(sequence_number)
            return terms_list


set_the_dial()