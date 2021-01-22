##블록 이동하기##
'''
#내가쓴 코드#
#(오류가 나온다)#
from collections import deque
import copy

def b(dx,dy,v,a,n):
  state='a'
  q=deque([(0,0),(0,1)])
  c=0
  while q:
    x1,y1=q.popleft()
    x2,y2=q.popleft()
    for i in range(12):
      dx1,dx2=dx[i]
      dy1,dy2=dy[i]
      nx1,ny1=x1+dx1,y1+dy1
      nx2,ny2=x2+dx2,y2+dy2
      if nx1>=0 and nx1<n and ny1>=0 and ny1<n and nx2>=0 and nx2<n and ny2>=0 and ny2<n:
        if a[nx1][ny1]==1 or a[nx2][ny2]==1:
            continue
        if v[nx1][ny1] and v[nx2][ny2]:
            continue
        if i>3:
          if state=='a':
            if i==4:
              if a[x2-1][y2]==1:
                continue
            elif i==5:
              if a[x2+1][y2]==1:
                continue
            elif i==8:
              if a[x1-1][y1]==1:
                continue
            elif i==9:
              if a[x1+1][y1]==1:
                continue
            state='b'
          else:
            if i==6:
              if a[x2][y2+1]==1:
                continue
            elif i==7:
              if a[x2][y2-1]==1:
                continue
            elif i==10:
              if a[x1][y1+1]==1:
                continue
            elif i==11:
              if a[x1][y1-1]==1:
                continue
            state='a'
      q.append((nx1,ny1))
      q.append((nx2,ny2))
      c+=1
      a[nx1][ny1]=c
      a[nx2][ny2]=c
      v[nx1][ny1]=True
      v[nx2][ny2]=True

def solution(board):
    a=copy.deepcopy(board)
    answer = 0
    n=len(board)
    v=[[False]*n for _ in range(n)]
    dx=[(0,0),(0,0),(-1,-1),(1,1),(0,-1),(0,1),(0,-1),(0,-1),(-1,0),(1,0),(1,0),(1,0)]
    dy=[(-1,-1),(1,1),(0,0),(0,0),(0,-1),(0,-1),(0,1),(0,-1),(1,0),(1,0),(1,0),(-1,0)]
    b(dx,dy,v,a,n)
        
    return answer

solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])

##블록 이동하기##
#답#
from collections import deque
def get_next_pos(pos,board):
    next_pos=[]
    pos=list(pos)
    pos1_x,pos1_y,pos2_x,pos2_y=pos[0][0],pos[0][1],pos[1][0],pos[1][1]
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    for i in range(4):
        pos1_next_x,pos1_next_y,pos2_next_x,pos2_next_y=pos1_x+dx[i],pos1_y+dy[i],pos2_x+dx[i],pos2_y+dy[i]
        if board[pos1_next_x][pos1_next_y]==0 and board[pos2_next_x][pos2_next_y]==0:
            next_pos.append({(pos1_next_x,pos1_next_y),(pos2_next_x,pos2_next_y)})
    if pos1_x==pos2_x:
        for i in [-1,1]:
            if board[pos1_x+i][pos1_y]==0 and board[pos2_x+i][pos2_y]==0:
                next_pos.append({(pos1_x,pos1_y),(pos1_x+i,pos1_y)})
                next_pos.append({(pos2_x,pos2_y),(pos2_x+i,pos2_y)})
    elif pos1_y==pos2_y:
        for i in [-1,1]:
            if board[pos1_x][pos1_y+i]==0 and board[pos2_x][pos2_y+i]==0:
                next_pos.append({(pos1_x,pos1_y),(pos1_x,pos1_y+i)})
                next_pos.append({(pos2_x,pos2_y),(pos2_x,pos2_y+i)})
                
    return next_pos
                                 
def solution(board):
    n=len(board)
    new_board=[[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1]=board[i][j]
    q=deque()
    visited=[]
    pos={(1,1),(1,2)}
    q.append((pos,0))
    visited=[]
    while q:
        pos,cost=q.popleft()
        if (n,n) in pos:
            return cost
        for next_pos in get_next_pos(pos,new_board):
            if next_pos not in visited:
                q.append((next_pos,cost+1))
                visited.append(next_pos)
    return 0

##국영수##
#답#
n=int(input())
students=[]

for _ in range(n):
  students.append(input().split())
  
students.sort( key=lambda x: [-int(x[1]),int(x[2]),-int(x[3]),x[0]] )
for student in students:
  print(student[0])
'''