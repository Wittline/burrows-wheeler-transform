class bwt(object):

    def __init__(self, s):
        self.str = s

    def __sa(self, s):
        st = sorted([(s[x:], x) for x in range(0, len(s))])
        return map(lambda x: x[1], st)

    def __rank(self, bw):
        ts = dict()
        rks = []
        for c in bw:
            if c not in ts:
                ts[c] = 0
            rks.append(ts[c])
            ts[c] += 1
        return rks, ts

    def __fc(self, ts):
        first = {}
        tc = 0
        for c, count in sorted(ts.items()):
            first[c] = (tc, tc + count)
            tc += count
        return first      

    def code(self):
        bw = []
        for i in self.__sa(self.str):
            if i == 0:
                bw.append('$')
            else:
                bw.append(self.str[i-1])

        return ''.join(bw)        
    
    def decode(self, bw):
        rks, ts = self.__rank(bw)
        first = self.__fc(ts)
        ri = 0
        t = '$'
        while bw[ri] != '$':
            c = bw[ri]
            t = c + t            
            ri = first[c][0] + rks[ri]
        return t




