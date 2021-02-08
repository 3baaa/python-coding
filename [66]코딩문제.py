##청소년 상어##
'''
#내가쓴 코드#
#(잘못쓴 코드)#
from collections import deque
import copy

def fish_small_ch(fish_small,array3):
    for i in range(1,17):
        t=False
        for j in range(4):
            for k in range(4):
                if array3[j][k][0]==i:
                    fish_small.append([j,k])
                    t=True
                    break
            if t:
                break
                    
def ch(nx,ny,array):
    if nx>-1 and nx<4 and ny>-1 and ny<4 and array[nx][ny]!=-1 and array[nx][ny]!=0:
            return True
    return False
    
def fish_move(array3):
    fish_small=[0]
    fish_small_ch(fish_small,array3)
    for i in range(1,17):
        q=deque([fish_small[i]])
        while q:
            x,y=q.popleft()
            for j in range(0,9):
                k=(array3[x][y][1]+j)%8
                nx=x+dx[k]
                ny=y+dy[k]
                if ch(nx,ny,array3):
                    fish_small[ array3[nx][ny][0] ]=[nx,ny]
                    array3[x][y],array3[nx][ny]=array3[nx][ny],array3[x][y]
                    array3[nx][ny][1]=k
                    q.append([nx,ny])
                    break
                        
def shark_move(s):#s=[0,0,array,r=0]
    q=deque([s])
    while q:
        x,y,array2,r=q.popleft()
        z=False
        fish_move(array2)
        for i in range(0,9):
            j=(array2[x][y][1]+i)%9
            nx=x+dx[j]
            ny=y+dy[j]
            if ch(nx,ny):
                z=True
                array3=copy.deepcopy(array2)
                r+=array3[nx][ny]
                array3[x][y]=0
                array3[nx][ny]=-1
                q.append(nx,ny,arry3,r)
                for _ in range(2):
                    nx=nx+dx[j]
                    ny=ny+dy[j]
                    if ch(nx,ny,array):
                        array3=copy.deepcopy(array2)
                        array3[x][y]=0
                        array3[nx][ny]=-1
                        q.append(nx,ny,array3,r)
                    else:
                        break
        if z==False:
            result.append(r)
                

array=[[0]*4 for _ in range(4)]
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]
result=[]

for i in range(4):
    t=list(map(int,input().split()))
    c=0
    for j in range(0,len(t),2):
        a,b=t[j:j+2]
        array[i][c]=[a,b]
        c+=1

shark_move([0,0,array,0])
print(max(result))

#답#
import copy

array = [[None] * 4 for _ in range(4)]

for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        array[i][j] = [data[j * 2], data[j * 2 + 1] - 1]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def turn_left(direction):
    return (direction + 1) % 8

result = 0

def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i, j)
    return None

def move_all_fishes(array, now_x, now_y):
    for i in range(1, 17):
        position = find_fish(array, i)
        if position != None:
            x, y = position[0], position[1]
            direction = array[x][y][1]
            for j in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if 0 <= nx and nx < 4 and 0 <= ny and ny < 4:
                    if not (nx == now_x and ny == now_y):
                        array[x][y][1] = direction
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                        break
                direction = turn_left(direction)
        
def get_possible_positions(array, now_x, now_y):
    positions = []
    direction = array[now_x][now_y][1]
    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        if 0 <= now_x and now_x < 4 and 0 <= now_y and now_y < 4:
            if array[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
    return positions

def dfs(array, now_x, now_y, total):
    global result
    array = copy.deepcopy(array)
    
    total += array[now_x][now_y][0]
    array[now_x][now_y][0] = -1
    
    move_all_fishes(array, now_x, now_y)

    positions = get_possible_positions(array, now_x, now_y)
    if len(positions) == 0:
        result = max(result, total)
        return 
    for next_x, next_y in positions:
        dfs(array, next_x, next_y, total)

dfs(array, 0, 0, 0)
print(result)
'''
