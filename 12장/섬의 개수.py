from typing import List
def numIslands(grid : List[List[str]]):
  def sink(row, col):
    grid[row][col] = "0" # 0으로 갱신하여 물로 잠기게 함 
    for r,c in [ # 인접한 땅 탐색 
        (row -1 ,col), # 상
        (row + 1, col), # 하
        (row,col - 1), # 좌
        (row,col + 1) # 우  
        ]:
          if 0 <= r <len(grid) and 0 <= c < len(grid[r]): # 행과 열의 인덱스 범위설정  
            if grid[r][c] == "1": # 인접한 곳이 땅이라면 
              sink(r,c) # 잠기게 하고 또 인접한 곳 탐색 

  cnt = 0 # 땅의 개수 
  for r in range(len(grid)): # 행 루프 
    for c in range(len(grid[r])): # 열 루프 
      if grid[r][c] == "1":
        cnt += 1
        sink(r,c) # 인접한 땅이 있으면 물로 잠기게 한다 
  return cnt    

lst2nd = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
numIslands(lst2nd)
