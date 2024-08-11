class Solution(object):
    def simplifyPath(self, path):
        components = path.replace('/', ' ').split()
        parts = list()
        while components != []:
            elem = components.pop(0)
            if elem == '.':
                pass
            elif elem == '..':
                if parts != []:
                    parts.pop()
            else:
                parts.append(elem)
        result = '/'.join(parts)
        result = '/' + result
        return result
        """
        :type path: str
        :rtype: str
        """
        