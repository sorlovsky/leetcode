def reverse(x):
    reverse = ''
    x = str(x)
    startIndex = 0
    if x[0] == '-':
        reverse += '-'
        startIndex = 1

    for i in range(len(x), startIndex, -1):
        print(i-1)
        reverse += x[i-1] 

    return reverse 

x = '-123'
print(reverse(int(x)))
