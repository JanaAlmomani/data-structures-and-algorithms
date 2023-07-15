
def left_join(hashmap1, hashmap2):
    new_hashmap = []
    for key in hashmap1:
        row = []
        row.append(key)
        row.append(hashmap1[key])
        if key in hashmap2:
            row.append(hashmap2[key])
        else:
            row.append(None)
        new_hashmap.append(row)
    return new_hashmap
