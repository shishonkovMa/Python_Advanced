# I have added a unit test, a stress test, and a maximum test to my code.
# However, I stumbled very much on stress tests, on these tests with a huge variation.
# And I realized how disgusting my algorithm was written.
# The tests are good, no matter how I change the algorithmic component
# - at almost every step there is a true hitch, the tests do not miss a bad algorithm:)
# It's good. I wonder how I passed the grader?! =D


import math
import numpy as np
from random import seed, randint
from copy import deepcopy
import time


def find_percentile(a, b, p):
    result = []
    i, j = 0, 0
    n = len(a)
    m = len(b)
    if n == 0 and m == 0:
        return -math.inf
    while i < n and j < m:
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    while i < n:
        result.append(a[i])
        i += 1
    while j < m:
        result.append(b[j])
        j += 1
    size = len(result)
    return result[int(math.ceil((size * p) / 100)) - 1]


def test_find_percentile(a, b, p, correct_answer):
    find_percentile_test = find_percentile(a, b, p)
    error_str = 'The test failed!\nInput: {0},{1},{2}\nOutput: {3}\nCorrect output: {4}'
    assert find_percentile_test == correct_answer, error_str.format(a, b, p, find_percentile_test, correct_answer)


def run_unit_tests():
    test_find_percentile([1], [], 30, 1)
    test_find_percentile([6], [23], 50, 6)
    test_find_percentile([23], [6], 50, 6)
    test_find_percentile([15, 20], [25, 40, 50], 40, 20)
    test_find_percentile([15, 20, 35, 40, 50], [], 30, 20)
    print('Unit test passed!')


def run_stress_test(max_test_size=150000, max_attempts=1000, max_right_border=1000):
    seed(100)
    for attempt in range(max_attempts):
        print(f'Attempt №{attempt+1} ')
        for test_size_1 in range(max_test_size):
            for test_size_2 in range(max_test_size):
                for right_border in range(0, max_right_border):
                    t_a, t_b, t_p = get_random_test(test_size_1, test_size_2, right_border)
                    test_find_percentile(t_a, t_b, t_p, selection_find(t_a, t_b, t_p))
    print('Stress test passed!')


def get_random_test(test_size_1, test_size_2, right_border):
    test_a = []
    test_b = []
    test_p = randint(1, 100)
    for i in range(test_size_1):
        test_a.append(randint(0, right_border))
    for i in range(test_size_2):
        test_b.append(randint(0, right_border))
    return test_a, test_b, test_p


def selection_find(inp_a, inp_b, inp_p):
    a, b, p = deepcopy(inp_a), deepcopy(inp_b), deepcopy(inp_p)
    sorted_list = sorted(a + b)
    n = len(a)
    m = len(b)
    if n == 0 and m == 0:
        return -math.inf
    if len(sorted_list) == 1:
        return sorted_list[0]
    # percent = p/100 * len(sorted_list)
    if len(sorted_list) >= 2:
        return np.percentile(sorted_list, p, interpolation='higher')


def run_max_test():
    seed(100)
    t_a, t_b, t_p = get_random_test(150000, 150000, 100000)
    test_find_percentile(t_a, t_b, t_p, selection_find(t_a, t_b, t_p))
    print('Max test passed!')


if __name__ == '__main__':
    run_unit_tests()
    run_stress_test()
    start = time.time()
    run_max_test()
    end = time.time()
    time_max_test = end - start
    print(f'Time of run_max_test() is: {time_max_test}')
