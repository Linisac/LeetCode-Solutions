class Solution(object):
    def isIsomorphic(self, s, t):
        lens = len(s)
        lent = len(t)
        if lens != lent:
            #If s and t have different lengths, then they cannot be isomorphic.
            return False
        else:
            #len(s) == len(t)
            #Assume that s and t have the same length. Traverse both strings simultaneously from left to right to see
            #if {(s[i], t[i]) | 0 <= i <= lens - 1} is a one-to-one (hence invertible, in this case) function: To achieve
            #this, maintain two mappings, stMapping and tsMapping, the
            #one-to-one-ness is checked by determining whether
            #(1) t[i] is what it is supposed to be, if s[i] exists in stMapping
            #(2) t[i] is absent in tsMapping, if s[i] does not alreay exist in stMapping
            #for all i.
            stMapping = dict()
            tsMapping = dict()
            for i in range(lens):
                if s[i] in stMapping:
                    if t[i] != stMapping[s[i]]:
                        return False
                else:
                    #s[i] not in stMapping
                    if t[i] in tsMapping:
                        return False
                    else:
                        #s[i] not in stMapping and t[i] not in tsMapping
                        stMapping[s[i]] = t[i]
                        tsMapping[t[i]] = s[i]
            return True
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        