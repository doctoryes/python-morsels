
def tail(things, num_items):
    if num_items <= 0:
        return []
    x = list(things)
    return [i for i in x[max(len(x)-num_items, 0):]]
