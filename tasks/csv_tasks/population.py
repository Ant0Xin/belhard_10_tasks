"""
Написать функцию max_delta, в которой будет происходить чтение csv
файла world_population.csv и функцию должна возвращать год, в котором
наибольший процент прироста населения.
"""

import csv


PERCENT = "world_population.csv"


def max_delta(f_name: str) -> str:
    with open(f_name) as csvfile:
        reader = csv.reader(csvfile)
        percent_list = [[i[2], i[0]] for i in reader]
        return max(percent_list[1:])[1]


if __name__ == "__main__":
    print(max_delta(PERCENT))
