# rotating the array using another array
# time complexity is O(n)
# space complexity is O(d)
def rotate_one(arr, n, d):
    temp = []
    k = len(arr) - d
    t = 0
    for i in range(n):
        if i < d:
            temp.append(arr[i])
        else:
            arr[i-d] = arr[i]
    for i in range(d):
        arr[k] = temp[i]
        k += 1
    return arr

# function to rotate the list by one element
def left_rotate_by_one(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp

# function to rotate the list d times
# time complexity is O(n*d)
# space complexity is O(1)
def left_rotate(arr, n, d):
    for i in range(d):
        left_rotate_by_one(arr, n)
    return arr


# function to reverse a list
def reverse_list(arr, si, ei):
    while si < ei:
        arr[si], arr[ei] = arr[ei], arr[si]
        si += 1
        ei -= 1


# function to rotate a list using reversal algorithm
# time complexity is O(n)
# space complexity is O(1)
def rotate_reverse(arr, n, d):
    if d == 0:
        return
    d = d % n
    reverse_list(arr, 0, d-1)
    reverse_list(arr, d, n-1)
    reverse_list(arr, 0, n-1)
    return arr

a = [1, 2, 3, 4, 5, 6, 7]
r = 2
length = len(a)
print("Rotating list using method one",rotate_one(a, length, r))
# original list is [3, 4, 5, 6, 7, 1, 2]
print("Rotating list using method two",left_rotate(a, length, r))
# original list is [5, 6, 7, 1, 2, 3, 4]
print("Rotating list using reversal algorithm", rotate_reverse(a, length, r))
