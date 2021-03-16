import sys

# 실수를 받아 가장 가까운 정수를 반환하는 함수
def closestint(i):
	if abs(i-int(i))>0.5:
		return int(i)+1 if i>0 else int(i)-1
	return int(i)

# Dynamic Programming, '기억하며 풀기' 기법으로 실행 시간을 단축한다.
dp=[[0]*5 for _ in range(10005)]

# Frame–Stewart algorithm
def T(n,r):
	if n==1: return 1
	if r==3:
		return 2**n-1
	if dp[n][r]: return dp[n][r]
	# 본래는, [1,n) 범위의 정수 중 2*T(k,r)+T(n-k,r-1)을 최소로 만드는 k를 찾는다.
	k=n-closestint((2*n+1)**.5)+1 # 4-peg 문제에서 최적의 k는 이와 같다.
	dp[n][r]=2*T(k,r)+T(n-k,r-1)
	return dp[n][r]

for idx,i in enumerate(map(int,sys.stdin)):
	print("Case %d: %d"%(idx+1,T(i,4)))