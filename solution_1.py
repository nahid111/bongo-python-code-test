def print_depth(data, lvl=1):
    if type(data) is not dict:
        return None

    for k, v in data.items():
        print("{0} {1}".format(k, lvl))
        if type(v) is dict:
            print_depth(v, lvl=lvl+1)


