#!/bin/python3

# sort an array in acending order
# [ 2, 3,1] = [1,2,3]
def sort_array(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
    return array


if __name__ == "__main__":
    file = open("main.log", "a")
    array = [2, 3, 1]
    file.write(f"array before sort is {array}\n")
    sort_array(array)
    file.write(f"array after sort is {array}\n")
    file.write("-------------------------------\n")
