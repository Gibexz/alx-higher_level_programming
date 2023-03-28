#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    newList = []
    for i in range(list_length):
        try:
            newList.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            newList.append(0)
        except (TypeError, ValueError):
            print("wrong type")
            newList.append(0)
        except IndexError:
            print("out of range")
            newList.append(0)
        finally:
            pass
    return newList
