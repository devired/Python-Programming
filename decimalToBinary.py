class Solution:
    # @param A : integer
    # @return a strings
    def findDigitsInBinary(self, A):
        b = list()
        i = 1
        while (i>0):
            i = A/2
            j = A%2
            A = i
            b.insert(0,j)
        c = ''.join(map(str,b))
        return c