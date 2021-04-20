def printDiamondPattern(n):
    temp = n
    space = 1
    star1 = 1
    space1 = n * 2 -1

    totalStarsCount = 0

    while n > 0:
        starsCount = 0
        starsCount += printingUpwardStars(n)

        printingUpwardSpace(space)
        starsCount += printingUpwardStars(n)

        print( "- " ,starsCount)

        print("\n")
        totalStarsCount += starsCount

        n -= 1
        space += 2


    while temp > 0:
        starsCount = 0
        starsCount += printingUpwardStars(star1)

        printingUpwardSpace(space1)
        starsCount += printingUpwardStars(star1)

        print("-", starsCount)
        print("\n")
        totalStarsCount += starsCount

        temp -= 1
        star1 += 1
        space1 -= 2
    print("total no of stars are ",totalStarsCount)



def printingUpwardStars(n):
    i = 0
    starsCount = 0
    while i < n:
        print('*', end='')
        print(" ", end='')
        i += 1
        starsCount += 1
    return starsCount


def printingUpwardSpace(space):
    sp = 0
    while sp < space:
        print(" ", end='')
        print(" ", end='')
        sp += 1







printDiamondPattern(7)
