def max_of_three(arg_1, arg_2, arg_3):
    if arg_1 > arg_2 and arg_1 > arg_3:
        return arg_1
    elif arg_3 < arg_2 and arg_1 < arg_2:
        return arg_2
    else:
        return arg_3
        



print(max_of_three(10, 20, 15))