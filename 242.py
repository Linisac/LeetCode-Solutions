class Solution(object):
    def isAnagram(self, s, t):
        map_s = dict()
        map_t = dict()
        lens = len(s)
        lent = len(t)
        if lens != lent:
            return False
        else:
            for i in range(lens):
                if s[i] in map_s:
                    map_s[s[i]] += 1
                else:
                    map_s[s[i]] = 1
                if t[i] in map_t:
                    map_t[t[i]] += 1
                else:
                    map_t[t[i]] = 1
            return map_s == map_t