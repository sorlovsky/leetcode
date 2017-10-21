def maxSubArray(ls):
    if len(ls) == 0:
       raise Exception("Array empty") # should be non-empty

    runSum = maxSum = ls[0]
    i = 0
    start = finish = 0

    for j in range(1, len(ls)):
        if ls[j] > (runSum + ls[j]):
            runSum = ls[j]
            i = j
        else:
            runSum += ls[j]

        if runSum > maxSum:
            maxSum = runSum
            start = i
            finish = j

    print("maxSum =>", maxSum)
    print("start =>", start, "; finish =>", finish)

# maxSubArray([-2, 11, -4, 13, -5, 2])
# maxSubArray([-15, 29, -36, 3, -22, 11, 19, -5])

def maxAverageSubArray(A, k):
    max_ending_here = max_so_far = A[0:k]
    for x in A[k:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far