def ships(S):
    # write your code in Python 2.7
    sum_left, sum_right = 0, sum(a)
    for index,value in enumerate(a):
        sum_right -= value
        if sum_left == sum_right:
            yield index
        sum_left += value
    return index
