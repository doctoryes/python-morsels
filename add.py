from copy import deepcopy


def _add_two_lists(list1, list2):
    """
    Add together two lists of numbers of the same length.
    """
    if len(list1) != len(list2):
        raise IndexError()
    return [(list1[idx] + list2[idx]) for idx in range(len(list1))]


def add(*lists):
    """
    Add together an arbitrary number of lists.
    """
    answer = None
    for curr_lists in lists:
        if answer is None:
            answer = deepcopy(curr_lists)
        else:
            for idx in range(len(curr_lists)):
                try:
                    answer[idx] = _add_two_lists(answer[idx], curr_lists[idx])
                except IndexError:
                    raise ValueError("Given matrices are not the same size.")

    return answer
