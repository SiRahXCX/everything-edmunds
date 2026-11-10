from math import pow


def is_armstrong(num: int) -> bool:
    if not isinstance(num, int) or isinstance(num, bool):
        raise TypeError(f'Expected int, got {type(num).__name__}')
    
    num_length = len(str(num))
    partial_num = num
    acc = 0

    while partial_num > 0:
        acc += int(pow(partial_num % 10, num_length))
        partial_num //= 10

    return num == acc 


if __name__ in '__main__':
    try:
        assert is_armstrong(153) == True
        assert is_armstrong(9474) == True
        assert is_armstrong(178) == False
    except TypeError as e:
        print(f'Error caught: {e}')

