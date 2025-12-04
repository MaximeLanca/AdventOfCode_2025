def tranform_data():

    with open("../day02/data.txt", "r") as f:
        data_list = [line.strip() for line in f]
        print(data_list)
    raw_data = data_list[0]

    list_two_step = []

    list_first_step = raw_data.split(",")
    for range in list_first_step:
        list_two_step.append(range.split("-"))

    return list_two_step
    


def search_invalid_ID():
    data_list = tranform_data()
    invalid_value_id = []
    result = 0

    for data in data_list:

        start_range = int(data[0])
        end_range = int(data[1])

        for number in range (start_range, end_range + 1):
            if len(str(number)) % 2 != 0 :
                continue
            else:
                s = str(number)
                mid = len(s) // 2
                print(mid)
                left = s[:mid]
                rigth = s[mid:]

                if left == rigth:
                    invalid_value_id.append(number)
            

    for r in invalid_value_id:
        result = result + r
    print(result)
search_invalid_ID()