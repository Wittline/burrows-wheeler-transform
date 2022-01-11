class bwt(object):

    def __init__(self, s):
        self.str = s

    def __sa(s):
        st = sorted([(s[x:], x) for x in range(0, len(s))])
        return map(lambda x: x[1], st)

    def code(self):
        bw = []
        for i in self.__sa(self.str):
            if i == 0:
                bw.append('$')
            else:
                bw.append(self.str[i-1])

        return ''.join(bw)
        


    
    def decode():
        return 0





