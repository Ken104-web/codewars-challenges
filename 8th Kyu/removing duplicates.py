def distinct(seq):
    duplicates=[]
    already_seen = set()
    for i in seq:
        if i not in already_seen:
            already_seen.add(i)
            duplicates.append(i)
    return duplicates