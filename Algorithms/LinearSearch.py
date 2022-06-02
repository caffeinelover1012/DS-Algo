A = [4,6,7,8,3,2,1,9]

# returns index of first occurrence if element is found, else -1
def linearSearch(element,arr):
    for i in range(len(arr)):
        if arr[i]==element:
            return i
    return -1

idx = linearSearch(4,A)
print("Found at ",idx)