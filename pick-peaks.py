def pick_peaks(arr):
    pos = []
    peaks = []
    plateau = False
    for index in range(1, len(arr)-1):
        if arr[index] > arr[index-1] and arr[index] > arr[index+1]:
            pos.append(index)
            peaks.append(arr[index])
        if plateau and arr[index] > arr[index+1]:
            pos.append(p_index)
            peaks.append(arr[p_index])
        if arr[index] != arr[index+1]:
            plateau = False
        if arr[index] > arr[index-1] and arr[index] == arr[index+1] and not plateau:
            plateau = True
            p_index = index
    return {'pos': pos, 'peaks': peaks}
