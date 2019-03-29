import random

def get_max(data, i, rw, threshold):
    val = data[i]
    data_size = len(data)
    positions = [i-rw-1, i-rw, i-rw+1, i-1, i+1, i+rw-1, i+rw, i+rw+1]
    result = []
    for pos in positions:
        if pos > 0 and pos < data_size and abs(pos%rw - i%rw) <2:
            result.append(abs(val - data[pos]))
    return max(result)

def get_edge_data(data, row_width):
    new_data = []
    for point in range(len(data)):
        new_data.append(get_max(data, point, row_width, 30))
    return new_data

test_data = [int(random.random() * random.random() * 256) for i in range(16)]
output_data = get_edge_data(test_data, 4)

def get_easy_print(data, rw):
    print("{")
    for pos in range(len(data)):
        print(data[pos], end="")
        print(",", end = " ")
        if pos % rw == rw-1:
            print()
    print("}")

get_easy_print(test_data, 4)
print()
get_easy_print(output_data, 4)
