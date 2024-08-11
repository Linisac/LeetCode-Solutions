class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        adjmat = [list() for _ in range(numCourses)]
        for item in prerequisites:
            adjmat[item[1]].append(item[0])
        #0 for 'unprocessed'
        #1 for 'being processed' (in stack)
        #2 for 'processed' (out of stack)
        status = [0 for _ in range(numCourses)]
        stack = list()
        #perform DFS for the whole graph
        for i in range(numCourses):
            if status[i] == 0:
                status[i] = 1
                stack.append(i)
                while len(stack) > 0:
                    topOfStack = stack[-1]
                    if len(adjmat[topOfStack]) == 0:
                        status[topOfStack] = 2
                        stack.pop()
                    else:
                        if status[adjmat[topOfStack][-1]] == 0:
                            toPush = adjmat[topOfStack].pop()
                            status[toPush] = 1
                            stack.append(toPush)
                        elif status[adjmat[topOfStack][-1]] == 1:
                            return False
                        else:
                            adjmat[topOfStack].pop()
        return True
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        