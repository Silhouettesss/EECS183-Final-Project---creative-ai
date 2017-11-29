################################################################################
# The following functions are stubbed for you. You must pass all of our test
# cases for these functions as part of the core. To run your functions with our
# test cases, run this file as main. This file uses python's doctest module,
# which will run your implementations against the test cases contained in each
# function. Do NOT change any of the comments in this file or we will NOT be
# able to grade your project.

# Turn off bytecode .pyc files
import sys
sys.dont_write_bytecode = True

def return_dictionary(D):
    return D


def keyInDict(D, K):
    if K in D:
        return True
    else:
        return False


def returnKeyVal(D, K):
    return D[K]


def setKeyVal(D, K, V):
    D[K] = V
    return D


def setKeyValList(D, K, V1, V2, V3, V4):
    D[K] = [V1, V2, V3, V4]
    return D


def asciiAssociate():
    asciiDict = {'a' : 97,
                 'b' : 98,
                 'c' : 99,
                 'd' : 100,
                 'e' : 101,
                 'f' : 102,
                 'g' : 103,
                 'h' : 104,
                 'i' : 105,
                 'j' : 106,
                 'k' : 107,
                 'l' : 108,
                 'm' : 109,
                 'n' : 110,
                 'o' : 111,
                 'p' : 112,
                 'q' : 113,
                 'r' : 114,
                 's' : 115,
                 't' : 116,
                 'u' : 117,
                 'v' : 118,
                 'w' : 119,
                 'x' : 120,
                 'y' : 121,
                 'z' : 122}
    return asciiDict


def getColor(favoriteColors, name):
    return favoriteColors[name][0]


def translate(vocab, word, language):
    return vocab[word][language]


def nestedDictionary():
    D = {'a' : {},
         'b' : {},
         'c' : {},
         'd' : {},
         'e' : {},
         'f' : {},
         'g' : {},
         'h' : {},
         'i' : {},
         'j' : {},
         'k' : {},
         'l' : {},
         'm' : {},
         'n' : {},
         'o' : {},
         'p' : {},
         'q' : {},
         'r' : {},
         's' : {},
         't' : {},
         'u' : {},
         'v' : {},
         'w' : {},
         'x' : {},
         'y' : {},
         'z' : {}}
    return D


def nestedDictionary3D(L1,L2):
    D1 = {}
    D2 = {}
    for i in range(len(L2)):
        setKeyVal(D2,L2[i],{})
    for i in range(len(L1)):
        D1[L1[i]] = D2
    return D1


def valueFrom3D(D, K1, K2, K3):
    return D[K1][K2][K3]


def keysIn2D(D, L1, L2):
    for keyL1 in L1:
        for keyD in D.keys():
            if keyL1 == keyD:
                for keyL2 in L2:
                    if keyL2 == D[keyD]:
                        return True
    return False


class warmup(object):
 
    def makeBand(self):

        self.bandName = 'The Beatles'
        pass

    def setAlbum(self, album):

        self.album = album
        pass

    def printAlbum(self):

        return self.album + " by " + self.bandName
        pass

###############################################################################
# Main
###############################################################################

if __name__ == '__main__':
    import doctest
    doctest.testmod()
