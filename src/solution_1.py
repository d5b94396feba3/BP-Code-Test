
def  print_depth(data,dict_depth=0):
    dict_depth=dict_depth+1
    for key, value in data.items():
        if type(value) is dict:
            print(key, dict_depth)
            print_depth(value,dict_depth)
        else:
            print(key,dict_depth)

