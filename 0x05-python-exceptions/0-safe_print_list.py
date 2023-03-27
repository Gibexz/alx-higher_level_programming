#!/usr/bin/python3

#if __name__ == "__main__":
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        while (i < x):
            print(my_list[i], end="")
            i += 1
    except IndexError:
        pass
    finally:
        print()
        return i
