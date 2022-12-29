from random import shuffle, randint

class HiddenValue(object):
    def __init__(self, v):
        self.__value = v

    def _compare(self, other):  # self compared to other
        if (self.__value < other.__value):
            return -1
        elif (self.__value > other.__value):
            return 1
        else:
            return 0

class Nut(HiddenValue):
    def __init__(self, l, v):
        HiddenValue.__init__(self, v)
        self.__label = l.upper()

    def testBolt(self, bolt):
        #if (isinstance(bolt, Bolt)):
        return HiddenValue._compare(self, bolt)
        #return None

    def __str__(self):
        return "" + self.__label


class Bolt(HiddenValue):
    def __init__(self, l, v):
        HiddenValue.__init__(self, v)
        self.__label = l.lower()

    def testNut(self, nut):
        #if (isinstance(nut, Nut)):
        return HiddenValue._compare(self, nut)
        #return None

    def __str__(self):
        return "" + self.__label


## Code to create randomized nut and bolt list
def createNutsAndBoltsMix(n):
    labels = {}
    while (len(labels) < 2 * n):
        labels[chr(65 + randint(0, 25)) + chr(65 + randint(0, 25))] = ""

    nL = list(labels.keys())[:n]
    bL = list(labels.keys())[n:]

    sz = list(range(1, n * 25))
    shuffle(sz)
    sz = sorted(sz[:n])

    outN = [Nut(nL[i], sz[i]) for i in range(n)]
    outB = [Bolt(bL[i], sz[i]) for i in range(n)]

    ans = ""
    for i in range(n):
        ans += str(outN[i]) + " -- " + str(outB[i]) + " @ value of " + str(sz[i]) + "\n"

    shuffle(outN)
    shuffle(outB)

    return outN, outB, ans

## Your code to match the bolts to the nuts here
def partition(arr, low, high, compareFunc):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if compareFunc(arr[j], pivot) < 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def randomPartition(arr, low, high, compareFunc):
    r = randint(low, high)
    arr[r], arr[high] = arr[high], arr[r]
    return partition(arr, low, high, compareFunc)

def quicksort(arr, other, low, high, compareFunc, nut):
    if low < high:
        if nut == True:
            p = randomPartition(arr, low, high, compareFunc)
        else:
            p = randomPartition(arr, low, high, compareFunc)
        quicksort(arr, other, low, p - 1, compareFunc, nut)
        quicksort(arr, other, p + 1, high, compareFunc, nut)

def matchNutsAndBolts(nuts, bolts):
    def nut_compare(nut, bolt):
        return nut.testBolt(bolt)

    def bolt_compare(bolt, nut):
        return bolt.testNut(nut)

    quicksort(nuts, bolts, 0, len(nuts) - 1, nut_compare, True)
    quicksort(bolts, nuts, 0, len(bolts) - 1, bolt_compare, False)

    return nuts, bolts  ##return the nuts and bolts list sorted
## ==============================================

##general testing cycle
while (True):
    N = 0
    user = input("Enter the number of nut and bolt pairs to test: ")
    if (user.isnumeric()):
        N = int(user)
    else:
        print("...enter only numbers\n")
        continue

    nutList, boltList, ans = createNutsAndBoltsMix(N)

    print("\n\nStarting list of nuts and bolts\n")
    print("\tnuts:  " + " ".join([str(n) for n in nutList]))
    print("\tbolts: " + " ".join([str(b) for b in boltList]))
    print("\n")

    ansNut, ansBolt = matchNutsAndBolts(nutList, boltList)

    print("your coding result:\n")
    print("\tnuts:  " + " ".join([str(n) for n in ansNut]))
    print("\tbolts: " + " ".join([str(b) for b in ansBolt]))
    print("\n")

    print("answers\n")
    print(ans)
    print("\n")

    input("Enter any key to continue...")





