# Time complexity : O(H*W*k) --> k = (H*W) C (n)
# Space complexity : O(H*W*k) --> k = (H*W) C (n)
# Leetcode : Solved

class Placement:
    def findMinDistance(self, H, W, n):
        # make a grid of size W * H and declare the min_dist as infinity
        grid = [[-1 for _ in range(W)] for _ in range(H)]
        self.min_dist = float('inf')
        
        # call the backtrack function with the starting index on grid
        self.backtrack(grid, 0, 0, H, W, n)
        
        # return the min_dist found after all the iterations
        return self.min_dist
    
    def backtrack(self, grid, row, col, rows, cols, n):
        # base
        # if we have reached 0, meaning we have placed all the buildings, then call the bfs to find out the minimum distance
        if n == 0:
            self.bfs(grid, rows, cols)
            return
        
        # logic
        # out of bounds for the column, if we reach the end of columns, then move to next line
        if col == cols:
            row += 1
            col = 0
        
        # traverse over the grid
        for i in range(row, rows):
            for j in range(col, cols):
                
                # action
                # place the building at the current index
                grid[i][j] = 0
                
                # recurse
                # recursively call the backtrack function by decrementing n by 1 and incrementing col by 1
                self.backtrack(grid, row, col + 1, rows, cols, n-1)
                
                # backtrack
                # replace the building placed to -1
                grid[i][j] = -1
            
            # after each line completion, move the column to 0
            c = 0
                
    def bfs(self, grid, rows, cols):
        # default values of dist is 0 and make a visited array same as grid
        dist = 0
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        
        # maintain a queus as we are using BFS
        q = collections.deque([])
        
        # put all the buildings location in the queue and mark them visited
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited[i][j] = True
                    
        # make the direction array
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        
        # traverse until the queue is empty
        while q:
           
            # maintain the size as we need to maintain the dist or leve;
            size = len(q)
            for i in range(size):
                # pop the first element from queue
                curr = q.popleft()
                
                # check for all 4-directions
                for di in dirs:
                  
                    # get new index on grid
                    nr = curr[0] + di[0]
                    nc = curr[1] + di[1]
                    
                    # check for boundary condition and also if they are not marked visited
                    if nr >= 0 and nr < H and nc >= 0 and nc < W and not visited[nr][nc]:
                        # append to the queue and mark them visited
                        q.append((nr,nc))
                        visited[nr][nc] = True
            
            # increment the dist variable after each level
            dist += 1
        
        # update the min_dist with the min of the curr dist -1 
        self.min_dist = min(self.min_dist, dist-1)

# code to call the above function
# obj = Placement()
# H = 3
# W = 2
# n = 1
#print(obj.findMinDistance(H, W, n))
