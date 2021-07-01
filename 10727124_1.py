# 演算法分析機測
# 學號 : 10727124
# 姓名 : 劉宇廷
# 中原大學資訊工程系
# 雙子星塔 (Twin Towers)

def LCS( X, Y, m, n ) :  # Longest Common Subsequence
  dp = [ [ 0 for y in range( n + 1 ) ] for x in range( m + 1 ) ]  # Dynamic Programming

  for i in range( m + 1 ) :
    for j in range( n + 1 ) :
      if i == 0 or j == 0 :
        dp[i][j] = 0
      elif X[ i - 1 ] == Y[ j - 1 ] :
        dp[i][j] = dp[i-1][j-1] + 1
      else :
        dp[i][j] = max( dp[i-1][j], dp[i][j-1] )

  res = dp[m][n]
  return res

if __name__ == '__main__' :
  cnt = 0
  print( "Please enter the number...[Exit: 0 0]" )

  while True :
    cnt += 1
    m, n = map( int, input().split() )
    if m == 0 and n == 0 :
      break

    A = list( map( int, input().split() ) )
    B = list( map( int, input().split() ) )

    print( "Twin Towers #%d" %cnt )
    print( "Number of Tiles : %d" %LCS( A, B, m, n ) )
    print()