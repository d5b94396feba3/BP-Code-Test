
class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father
        
def  print_depth(data,dict_depth=0):
    
    dict_depth=dict_depth+1

    for key, value in data.items():

        if key is not "class_name":
            
            if "key" not in key:
                key+=':'
            if type(value) is dict:
                print(key, dict_depth)
                print_depth(value,dict_depth)
            elif value.__class__.__name__ is Person.__name__:
                print(key, dict_depth)
                print_depth(value.__dict__,dict_depth)
            else:
                print(key,dict_depth)
