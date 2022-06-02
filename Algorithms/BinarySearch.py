A=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
#  0  1  2  3  4   5   6   7    8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24

def binarySearch(element,arr):
    min = 0
    max = len(arr)-1
    guess = (max-min)//2
    i=0
    while(arr[guess]!=element):
        # print(min, max, guess, arr[guess])
        # if guess idx is lower than element, search right half
        if arr[guess]<element:
            min = guess +1 
        # else search left half
        else:
            max = guess -1
        guess = min+ (max-min)//2
        # if element does not exist
        if min>max:
            return -1
    return guess

print(binarySearch(37,A))