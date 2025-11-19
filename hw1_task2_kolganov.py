import random
import numpy as np
from typing import Tuple, List

def generate_random_task(num_elems: int) -> Tuple[np.ndarray, int, int]:
    """ Задача задается случайным вектором чисел заданной длины и случайной длиной промежутка """
    arr = np.random.randint(0, 100, num_elems)
    segment_len = random.randint(1, 5)
    
    is_even_segment= 1 if segment_len % 2 == 0 else 0
    
    return arr, segment_len, is_even_segment


def calculate_medians(arr: np.ndarray, segment_len: int, is_even_segment: bool) -> List[float]:
    """ Вычисление медиан """
    medians = []
    
    for i in range(0, len(arr), segment_len):
        segment = arr[i:i + segment_len]
        sorted_segment = np.sort(segment)
        
        if is_even_segment:
            right_num = len(sorted_segment) // 2
            left_num = right_num - 1
            median = (sorted_segment[left_num] + sorted_segment[right_num]) / 2
        else:
            median = sorted_segment[len(sorted_segment) // 2]
        
        medians.append(median)
    
    return medians


def generate_task(num_elems: int, segment_len: int) -> Tuple[np.ndarray, int, int]:
    """ Задание задачи с заданной длиной массива чисел и заданной длиной промежутка """
    arr = np.random.randint(0, 100, num_elems)
    
    # Проверка кратности длины массива длине сегмента
    if len(arr) % segment_len == 0:
        print("lenght of arr corresponding to segment lenght")
    else:
        print("lenght of arr not corresponding to segment lenght")
    
    is_even_segment = 1 if segment_len % 2 == 0 else 0
    
    return arr, segment_len, is_even_segment


def main():
    arr, segment_len, flag = generate_task(25, 4)
    print(f"arr = {arr}")
    print(f"segment lenght = {segment_len}, even_flag = {flag}")
    
    medians = calculate_medians(arr, segment_len, flag)
    print(f"medians =  {medians}")
    
    arr_rand, segment_len_rand, flag_rand = generate_random_task(20)
    print(f"rand arr = {arr_rand}")
    print(f"rand segment lenght = {segment_len_rand}, even flag = {flag_rand}")
    
    medians_rand = calculate_medians(arr_rand, segment_len_rand, flag_rand)
    print(f"medians = {medians_rand}")


if __name__ == '__main__':
    main()