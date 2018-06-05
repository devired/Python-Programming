class Solution:
    # @param A : integer
    # @return an integer
    def isPrime(self, A):
        b = int(math.sqrt(A))
        #print b
        if A > 1:
            for i in range (2,b+1):
                if(A % i == 0):
                    return 0
            else:
                return 1
        else:
            return 0