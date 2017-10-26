import sys

def nsort(arr):
    min = sys.maxsize
    max = -sys.maxsize - 1
    
    # Get max and min
    for i in arr:
        if i < min:
            min = i

        if i > max:
            max = i

    # Create array of max + offset
    offset = 0
    if min < 0:
        offset = -min

    # Create array with size max value + 1 to accommodate max value
    temparr = [0] * (max + offset + 1)

    # Populate temporary array
    for i in arr:
        temparr[i + offset] += 1
    print(temparr, len(temparr))

    # Create return array
    retarr = [0] * len(arr)

    # Populate return array
    r_c = 0
    t_c = 0

    while t_c < len(temparr):
        if temparr[t_c] > 0:
            for i in range(t_c, t_c + temparr[t_c]):
                retarr[r_c] = t_c - offset
                r_c += 1
        t_c += 1
    return retarr

