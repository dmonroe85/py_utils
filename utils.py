def is_num(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def print_row(row, spacing=10):
    str_row = []
    for x in row:
        if is_num(x):
            str_row.append(" "*(spacing-len("%.3f" % x)) + "%.3f" % x)
        else:
            str_row.append(" "*(spacing-len(x)) + "%s" % x)
    print ''.join(str_row)

def checkEqual(iterator):
      try:
         iterator = iter(iterator)
         first = next(iterator)
         return all(first == rest for rest in iterator)
      except StopIteration:
         return True

def transpose_list(list_data):
    return [list(x) for x in zip(*list_data)]