#Problem Statement: https://www.geeksforgeeks.org/queue-in-python/
#Reference: https://www.youtube.com/watch?v=UeE67iCK2lQ&list=PLgUwDviBIf0rGEWe64KWas0Nryn7SCRWw&index=5&ab_channel=takeUforward

from collections import deque
class Solution:
    def bfsOfGraph(self, V, adj):
        def bfs(root):
            q = deque()
            q.append(i)
            while q:
                node = q.popleft()
                ans.append(node)
                for it in adj[node]:
                    if vis[it]!=1:
                        q.append(it)
                        vis[it] = 1
        ans = []
        vis = [0] * V #for graph having more than 1 component
        for i in range(0, V): #1
            if vis[i]!=1:
                bfs(i)
        return ans
        
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
      
