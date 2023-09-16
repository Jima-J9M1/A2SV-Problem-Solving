class Solution:
    def __init__(self):
        self.dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    def is_valid(self, heights, mx):
        ROWS, COLS = len(heights), len(heights[0])
        q = deque()
        seen = [[False for _ in range(COLS)] for _ in range(ROWS)]
        q.append((0, 0))
        seen[0][0] = True

        while q:
            r, c = q.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                return True
            for dr, dc in self.dirs:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < ROWS and 0 <= new_c < COLS and not seen[new_r][new_c] and abs(heights[r][c] - heights[new_r][new_c]) <= mx:
                    seen[new_r][new_c] = True
                    q.append((new_r, new_c))

        return False

    def minimumEffortPath(self, heights):
        L, R = 0, 10**9
        best = R
        
        while L <= R:
            M = L + (R - L) // 2
            if self.is_valid(heights, M):
                R = M - 1
                best = min(best, M)
            else:
                L = M + 1
        
        return best
