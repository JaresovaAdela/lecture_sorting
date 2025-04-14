import csv
import os


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path) as file:
        reader = csv.DictReader(file)
        data = {}
        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))
    return data

def selection_sort(num_seznam, direction = "ascending"):
    """
    :param list num_seznam: list with numeric array
    :param str direction: string indicating sorting direction: ascending, descending
    :return: sorted numeric array
    """
    n = len(num_seznam)
    for i in range(n):
        min_max_i = i
        for num_idx in range(i+1, n):
            if direction == "ascending":
                if num_seznam[num_idx] < num_seznam[min_max_i]:
                    min_max_i = num_idx
            elif direction == "descending":
                if num_seznam[num_idx] > num_seznam[min_max_i]:
                    min_max_i = num_idx
        num_seznam[i], num_seznam[min_max_i] = num_seznam[min_max_i], num_seznam[i]
    return num_seznam

def bubble_sort(num_seznam):
    """
    :param list num_seznam: list with numeric array
    :return: sorted numeric array
    """
    n = len(num_seznam)
    for i in range(n-1):
        for j in range(n-i-1):
            if num_seznam[j] > num_seznam[j+1]:
                num_seznam[j], num_seznam[j+1] = num_seznam[j+1], num_seznam[j]
    return num_seznam

def insertion_sort(num_seznam):
    n = len(num_seznam)
    for i in range(1, n):
        insert_index = i
        current_value = num_seznam.pop(i)
        for j in range(i - 1, -1, -1):
            if num_seznam[j] > current_value:
                insert_index = j
        num_seznam.insert(insert_index, current_value)
    return num_seznam

def main():
    data = read_data("numbers.csv")
    print(data)
    selection = selection_sort(data["series_1"])
    print(selection)
    bubble = bubble_sort(data["series_2"])
    print(bubble)
    insertion = insertion_sort(data["series_3"])
    print(insertion)
    pass


if __name__ == '__main__':
    main()
