# 演算法分析機測
# 學號 : 10727124
# 姓名 : 劉宇廷
# 中原大學資訊工程系
# 0-1背包問題 (0-1 Knapsack)

def printknapSack( W, wt, val, n ) :
  K = [ [ 0 for w in range( W + 1 ) ] for i in range( n + 1 ) ]  # Dynamic Programming

  for i in range( n + 1 ) :
    for w in range( W + 1 ) :
      if i == 0 or w == 0 :
        K[i][w] = 0
      elif wt[i - 1] <= w :
        K[i][w] = max( val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w] )
      else :
        K[i][w] = K[i - 1][w]

  res = K[n][W]
  print( "Total Values = " + str( res ) )

  w = W
  items = []
  for i in range( n, 0, -1 ) :  # bottom up
    if res <= 0 :
      break

    if res == K[i - 1][w] :
      continue
    else :  # res == val[i-1] + K[i-1] [w-wt[i-1]]
      items.append( i )

      res = res - val[i - 1]
      w = w - wt[i - 1]

  items.sort()
  print( "Items ", end = "" )
  i = 0
  while ( i < len( items ) ) :
    print( items[i], end = "" )
    if ( i != len( items ) - 1 ) :
      print( ", ", end = "" )
    i += 1
  print( "\n" )

if __name__ == '__main__' :
  print( "Please enter the number...[Exit: 0]" )

  while True :
    wt = []
    val = []
    W = int( input() )
    if W == 0 :
      break
    n = int( input() )

    for _ in range( n ) :
      a, b = input().split()
      wt.append( int(a) )
      val.append( int(b) )

    printknapSack( W, wt, val, n )