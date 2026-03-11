import pytest
import re

def regex_test(expected, lines):
    i = 0 ; match = 0
    for token in expected:
        for j in range(i, len(lines)):
            res = re.search(token, lines[j])
            if res is not None:
                i = j + 1
                match += 1
                break
        else:
            print(f'\033[91m Not Found: {token} \033[0m')
            assert False, f'Expect: {expected}'
    else:
        print(f'\033[91m match count: {match} \033[0m')
        assert match == len(expected), f'Expect: {expected}'


@pytest.mark.T1
def test_main_1():
    with open('result1.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    # Input: 5 3 1 2 -> prints 5, 3, 1 (stops when 2 > 1)
    regex_test([r'5.*3.*1'], lines)


@pytest.mark.T2
def test_main_2():
    with open('result2.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    # Input: 10 7 4 1 8 -> prints 10, 7, 4, 1 (stops when 8 > 1)
    regex_test([r'10.*7.*4.*1'], lines)

@pytest.mark.T3
def test_main_3():
    with open('result3.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    # Input: 20 15 10 5 25 -> prints 20, 15, 10, 5 (stops when 25 > 5)
    regex_test([r'20.*15.*10.*5'], lines)

@pytest.mark.T4
def test_main_4():
    with open('result4.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    # Input: 100 50 25 200 -> prints 100, 50, 25 (stops when 200 > 25)
    regex_test([r'100.*50.*25'], lines)
