from umarell import umarell


@umarell
def slow_function():
    my_list = []
    for i in range(1000000):
        my_list.append(i)
    return my_list


@umarell
def fast_function():
    my_list = [i for i in range(1000000)]
    return my_list


if __name__ == '__main__':
    slow_function()
    fast_function()
