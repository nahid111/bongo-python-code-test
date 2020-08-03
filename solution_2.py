class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


def print_depth(data, lvl=1, is_obj=False):
    if type(data) is not dict:
        return None

    for k, v in data.items():

        if type(v) is Person:
            is_obj = True

        if is_obj:
            print("{0}: {1}".format(k, lvl))
        else:
            print("{0} {1}".format(k, lvl))

        if type(v) is dict:
            print_depth(v, lvl=lvl+1)
        elif type(v) is Person:
            print_depth(v.__dict__, lvl=lvl+1, is_obj=True)



