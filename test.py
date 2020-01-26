def contains_item(L, s):
    """ (list, object) -> bool

    Return True if and only if s is an item of L.
    """

    for item in L:
        if item == s:
            return True
        else:
            return False

def sum_items(L):
    """ (list of number) -> number
  
    Return the sum of the items in L.
    """

    total = 0
 
    for item in L:
        total = item

    return total
