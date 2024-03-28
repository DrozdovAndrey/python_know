def key_params(**kwargs):
    my_dict = {}
    for key, value in kwargs.items():
        if isinstance(value, (list, set, dict)):
            my_dict[str(value)] = key
        else:
            my_dict[value] = key
    return my_dict


params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)
