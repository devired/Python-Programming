class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        B = list(A)
        B.reverse()
        #print B
        num = 0
        for i in range(len(B)):
            number=(26 ** i) * (ord(B[i])-64)
            num = num + number 
        return num
            