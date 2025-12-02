
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
    zero_number = 0
    dial_direction_and_number = set_dial_direction_and_number()
    #print(dial_direction_and_number)

    for sequence in dial_direction_and_number:
        arrow_direction = sequence[0]
        sequence_of_number = sequence[1]
        print (sequence_of_number)

    if arrow_direction == "R" :
        for number in sequence_of_number:
            dial_position = sequence_of_number + number
            if dial_position == 0:
                zero_number += 1 
            elif dial_position >99 :

        

def set_dial_direction_and_number():
    sequence_of_rotation = saves_data_in_list()
    redefined_sequence_of_rotation = []
    redefined_data = []
    redefined_number = []

    for sequence in sequence_of_rotation:
        arrow_direction = sequence[0]
        number = int(sequence[1:])
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