def has_negatives(a):
    """
    YOUR CODE HERE
    """
    my_hashtable = {}
    my_negative_arry = []

    for ele in a: 
        my_hashtable[ele] = ele

        if ele is not 0 and -ele in my_hashtable:
            my_negative_arry.append(abs(ele))

    return my_negative_arry    


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
