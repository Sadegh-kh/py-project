def two_sum(my_list: list, target: int):
    """Finding the indices of the sum of two numbers with the target
    #example
    >> ls = [11,2,15,7,9]
    >> target = 9
    >> print(two_sum(ls,target))
    [1,3]
    """
    hash_table = {}
    for index, num in enumerate(my_list):
        if num in hash_table.keys():
            return [hash_table[num], index]
        hash_table[target - num] = index


if __name__ == "__main__":
    ls = [11, 2, 15, 7, 9]
    print(two_sum(ls, 9))
