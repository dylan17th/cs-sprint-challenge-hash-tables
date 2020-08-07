def intersection(arrays):

    length = len(arrays)
    my_arr = []
    my_cache = {}

    for ele in arrays:
        for ele2 in ele:
            if ele2 not in my_cache:
                my_cache[ele2] = 1
            elif ele2 in my_cache:
                my_cache[ele2] += 1
            if my_cache[ele2] == length:
                my_arr.append(ele2)

    return sorted(my_arr)


if __name__ == "__main__":
    arrays = [[4,6,7],[4,5,9]]

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
