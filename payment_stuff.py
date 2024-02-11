import random

def initialize_list(days = 100, baseProductPrice = 1000, minProductSold = 1, maxProductSold = 100000):
    list = []
    for i in range(days):
        list.append(baseProductPrice * random.randrange(minProductSold, maxProductSold))
        if random.randrange(1, 7) <= 2:
            list.append(0)

    return list
def list_with_no_zero(list):
    newList = []
    for i in list:
        if i > 0:
            newList.append(i)
    return newList

def find_min(list):
    return min(list)

def find_max(list):
    return max(list)

def find_medium(list):
    return sum(list) / len(list)

def find_days_above_medium(list):
    medium = find_medium(list)
    return sum(1 for dia in list if dia > medium)