import math

import pandas as pd
DEDUCTION_SCALE = 0.1
DEDUCION_DEVITATION = 100000
MAX_RATINGS =  2456123


def rating_review_adjuster(raw_rating:float, n_rating:int):
    if n_rating >= MAX_RATINGS:
        return raw_rating

    diff = MAX_RATINGS - n_rating
    number_of_punish = math.floor(diff / DEDUCION_DEVITATION)
    
    return raw_rating - number_of_punish * DEDUCTION_SCALE


def oscar_value(n_oscar:int):
    if not n_oscar: # 0
        return 0
    if n_oscar < 3: # 1-2
        return 0.3 
    if n_oscar < 6: # 3-5
        return 0.5
    if n_oscar < 11: #6-10
        return 1
    else :
        return 1.5 # +11

if __name__ == '__main__':
    print(rating_review_adjuster(9.3, 2200000))
    print(oscar_value(9))