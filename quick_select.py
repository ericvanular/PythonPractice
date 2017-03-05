 def quickSelect(seq, k):
    # this part is the same as quick sort
    len_seq = len(seq)
    if len_seq < 2: return seq

    ipivot = len_seq // 2
    pivot = seq[ipivot]

    smallerList = [x for i,x in enumerate(seq) if x <= pivot and  i != ipivot]
    largerList = [x for i,x in enumerate(seq) if x > pivot and  i != ipivot]

    # here starts the different part
    m = len(smallerList)
    if k == m:
        return pivot
    elif k < m:
        return quickSelect(smallerList, k)
    else:
        return quickSelect(largerList, k-m-1)