def deduped(items):
    """Return new list from items with duplicates removed."""

    no_dupes = set(items)
    lst = list(no_dupes)
    result = sorted(lst)
    print result

# deduped([1, 2, 1, 1, 3])
# deduped([1, 2, 3])
# deduped([])
