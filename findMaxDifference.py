def findMaxDifference(size, Array):

    #if size is less than 0 means no elements in the array
    #so we say its an empty list
    if size <= 0:
        return ('empty list')

    # check if the size is less than 2
    # to find difference atleast two elements are need in the list
    if size < 2:
        return ('atleast 2 elements are needed to calculate max difference ')

    i = 0
    # set max difference is 0 at the beginging
    maxDifference = 0
    # repeat loop until the last element
    while i + 1 < size:
        #find the difference between the ith index and the i+1 index which is also called adjacent
        difference = Array[i] - Array[i + 1]

        # Replace the value of difference with maxDifference
        # if difference is greater the maxDifference
        if difference > maxDifference:
            maxDifference = difference
        i += 1

    print(maxDifference)


def getInput():
    size = int(input())
    list1 = []
    for i in range(size):
        list1.append(int(input()))
    findMaxDifference(size, list1)



getInput()
