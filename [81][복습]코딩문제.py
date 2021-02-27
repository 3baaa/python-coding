##안테나##
#내가 쓴코드#
#(결과값이 나온다)#
n=int(input())
a=list(map(int,input().split()))

a.sort()
print(a[(len(a)-1)//2])
