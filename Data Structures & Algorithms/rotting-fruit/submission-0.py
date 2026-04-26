class Solution:

    def bfs(self, grid, queue):
        direc = [(-1,0), (1,0), (0,-1), (0,1)]
        ans = 1000000
        # print(queue)
        while queue:
            cr, cc, step= queue.popleft()

            ans = step

            for i,j in direc:
                nr = cr+i
                nc = cc+j

                if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]):
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc, step+1))
                        # print(queue)

        return ans


    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        ans = 100000
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                    temp = self.bfs(grid, queue)
                    ans = min(ans, temp)
        
        print(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return ans