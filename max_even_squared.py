def max_even_square(nums):
    if not isinstance(nums, (list, tuple)):
        raise TypeError("not a list")
    
    max_num = None

    for n in nums:
        if not isinstance(n, int):
            raise TypeError("only integers are allowed")
        if n % 2 == 0:
            if max_num is None or n > max_num:
                max_num = n
    
    if max_num is None:
        raise ValueError("no even numbers found")
    
    return max_num ** 2