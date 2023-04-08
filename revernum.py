class Solution():
    def rever(self,x):
        """
        :param x:
        :return:
        """
        if x>=0:
            rever_x=int(str(x)[::-1])
        else:
            rever_x=-int(str(x)[::-1])
        if -2**31<x<2**31-1:
            return rever_x
        else:
            return  0