import math as math_library
import time as time_library
import sys

result_a = []

def cube_calculations(numbers):
    for num in numbers:
        result_a.append(math_library.sqrt(num ** 3))

if __name__ == "__main__":
    # number_list = list(range(5000000))
    number_list = list(range(20000000))
    start_time = time_library.time()
    cube_calculations(number_list)
    end_time = time_library.time()
    with open('results', 'w') as f:
        sys.stdout = f
        print(f"The calculation took {end_time - start_time} second(s). The biggest volume was {result_a[-1]}")
