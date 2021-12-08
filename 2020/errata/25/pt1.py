def determineLoopSize(subNum, publicKey):
    curr = 1
    loop = 0
    while curr != publicKey:
        curr *= subNum
        curr = curr % 20201227
        loop += 1
    return loop


def transform(subNum, loopSize):
    curr = 1
    for _ in range(loopSize):
        curr *= subNum
        curr = curr % 20201227
    return curr


pk1 = 1965712
pk2 = 19072108
cardLoops = determineLoopSize(7, pk1)
print(transform(pk2, cardLoops))
