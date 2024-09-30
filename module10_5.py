# -*- coding: utf-8 -*-
import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)
    return all_data

if __name__ == '__main__':

    filenames = [f'./file_{number}.txt' for number in range(1, 5)]


    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    print(f"Линейный вызов: {time.time() - start_time}")


    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    print(f"Многопроцессный вызов: {time.time() - start_time}")