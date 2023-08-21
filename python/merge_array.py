f_array = [0, 3, 4, 22, 31]
s_array = [4, 6, 13, 30]


def merge_array(first_array: list[int], second_array: list[int]):
    if not isinstance(first_array, list) or not isinstance(second_array, list):
        raise ValueError("the arguments must be lists")

    result: list[int] = []
    final_length = len(first_array) + len(second_array) - 2
    f_index = 0
    s_index = 0

    for i in range(0, final_length):
        if f_index >= len(first_array):
            result.extend(second_array[s_index:])
            break
        elif s_index >= len(second_array):
            result.extend(first_array[f_index:])
            break
        elif first_array[f_index] < second_array[s_index]:
            result.append(first_array[f_index])
            f_index += 1
        else:
            result.append(second_array[s_index])
            s_index += 1

    return result


print(merge_array(f_array, s_array))
