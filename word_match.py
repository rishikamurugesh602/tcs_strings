pattern=input()
string=input()
def solution():
    m=len(pattern)
    n=len(string)
    dp=[[False for _ in range(n+1)]  for _ in range(m+1)]
    dp[0][0]=True
    for i in range(1,m+1):
        if pattern[i-1]=='*':
            dp[i][0]=dp[i-1][0]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if pattern[i-1]=='*':
                dp[i][j]=dp[i-1][j] or dp[i][j-1]
            elif pattern[i-1]=='?' or pattern[i-1]==string[j-1]:
                dp[i][j]=dp[i-1][j-1]
                
            else:
                dp[i][j]=False
    if dp[m][n]:
        print("match")
    else:
        print("no")
solution()
