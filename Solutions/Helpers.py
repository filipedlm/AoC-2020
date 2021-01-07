import time


def import_one_line_input(file):
    with open(file) as f:
        return f.readline()


def import_input(file):
    with open(file) as f:
        inputs = f.readlines()
        return [str(x).removesuffix('\n') for x in inputs]


def import_input_and_replace(data, replacement_dict):
    input_replaced = []
    for inp in data:
        for k, v in replacement_dict.items():
            inp = inp.replace(k, v)
        input_replaced.append(inp)
    return input_replaced


def print_map(list_of_list, max_depth=50):
    for i, l in enumerate(list_of_list):
        if i == max_depth:
            break
        print(l)


def print_dict(dict_of_list, max_keys=50):
    counter = 0
    for k, v in dict_of_list.items():
        if counter == max_keys:
            break
        print(k, v)
        counter += 1


def transform_to_groups(data, sep=''):
    print('Number of groups:', data.count(sep) + 1)

    groups = []
    i = 0
    while i < len(data):
        k = 0
        regrouped_data = []
        while i + k < len(data) and data[i + k] != sep:
            regrouped_data.append(data[i + k])
            k += 1
        # stop criterion
        if i + k == len(data) or data[i + k] == sep:
            groups.append(regrouped_data)
            i += k
        # jump next blankline
        i = i + 1

    return groups


# decorator for timing
def timeit(f):
    def timed(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        if te - ts >= 0.1:
            print('func:%r took: %2.4f sec' % (f.__name__, te - ts))
        return result

    return timed
