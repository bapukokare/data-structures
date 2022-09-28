#Problem Statement: https://www.geeksforgeeks.org/queue-in-python/
#Reference: https://www.youtube.com/watch?v=UeE67iCK2lQ&list=PLgUwDviBIf0rGEWe64KWas0Nryn7SCRWw&index=5&ab_channel=takeUforward

class Solution:
    def dfsOfGraph(self, V, adj):
        def dfs(node):
            ans.append(node)
            vis[node] = True
            for i in adj[node]:
                if not vis[i]:
                    dfs(i)        
        ans = []
        vis = [False] * V
        for i in range(0, V):
            if not vis[i]:
                dfs(i)
        return ans


# Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# Driver Code Ends
