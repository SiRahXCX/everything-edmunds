def reverse_number(num: int) -> int:
    reversed_num = 0
    
    while num > 0:
        reversed_num = reversed_num * 10 + (num % 10)
        num //= 10

    return reversed_num
    

def is_palindrome(num: int) -> bool:
    if not isinstance(num, int) or isinstance(num, bool):
        raise TypeError(f'Expected int, got {type(num).__name__}')

    return num == reverse_number(num)


if __name__ in '__main__':
    try:
        assert is_palindrome(12321) == True
        assert is_palindrome(16783) == False 
    except TypeError as e:
        print(f'Error caught: {e}')

