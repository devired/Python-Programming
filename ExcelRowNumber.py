class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        i = 0
        b = list()
        while(A>26):
            i = A %26
            if(i==0):
                b.append(chr(90))
                A = A -1
            else:   
                b.append(chr(i+64))
            A = A / 26
        b.append(chr(A+64))
        b.reverse()
        return ''.join(map(str,b))