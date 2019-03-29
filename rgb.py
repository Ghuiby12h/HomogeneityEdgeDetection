import random

def get_max(rgb, data, i, rw, threshold):
    val = data[i][rgb]
    data_size = len(data)
    positions = [i-rw-1, i-rw, i-rw+1, i-1, i+1, i+rw-1, i+rw, i+rw+1]
    result = []
    for pos in positions:
        if pos > 0 and pos < data_size and abs(pos%rw - i%rw) <2:
            result.append(abs(val - data[pos][rgb]))
    return max(result)

def get_R(data, rgb_index, row_width, threshold):
    return get_max(0, data, rgb_index, row_width, threshold)

def get_G(data, rgb_index, row_width, threshold):
    return get_max(1, data, rgb_index, row_width, threshold)

def get_B(data, rgb_index, row_width, threshold):
    return get_max(2, data, rgb_index, row_width, threshold)



def get_edge_data(data, row_width):
    new_data = []
    threshold = 30
    for rgb_index in range(len(data)):
        R = get_R(data, rgb_index, row_width, threshold)
        G = get_G(data, rgb_index, row_width, threshold)
        B = get_B(data, rgb_index, row_width, threshold)
        new_data.append([R,G,B])
    return new_data


test_data = [[random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]  for i in range(16)]
output_data = get_edge_data(test_data, 4)


def get_easy_print(data, rw):
    print("{",end="")
    for pos in range(len(data)):
        print(data[pos], end="")
        print(",", end = " ")
        if pos % rw == rw-1:
            print()
    print("}")

get_easy_print(test_data, 4)
print()
get_easy_print(output_data, 4)
