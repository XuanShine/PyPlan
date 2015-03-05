from utils import *

dict_test1 = {1: {2, 3, 4}, 5:[5, 8, 9, 5], "a": (7, 6, 4)}
dict_test2 = {"e": {7, 4}, "r": {4, 2}, 1: {3, 5, 7}, 5: {7, 2}, "b": set()}

assert keys_of_min_len_in_dict(dict_test1) == {1, "a"}

assert complete_dict_by_empty_set(dict_test1, dict_test2) ==\
        {1: {2, 3, 4}, 5:[5, 8, 9, 5], "a": (7, 6, 4), "e": set(), "r": set(),
         "b": set()}
dict_test3 = complete_dict_by_empty_set(dict_test1, dict_test2)
print(search_personn(dict_test3, dict_test1)


