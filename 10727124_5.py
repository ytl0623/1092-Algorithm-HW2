# 演算法分析機測
# 學號 : 10727124
# 姓名 : 劉宇廷
# 中原大學資訊工程系
# 西洋棋騎士 (Chess Knight)

class cell :
  def __init__( self, x = 0, y = 0, dist = 0 ) :
    self.x = x
    self.y = y
    self.dist = dist

def isInside( x, y, N ) :  # checks whether x, y is inside the board
  if ( x >= 1 and x <= N and y >= 1 and y <= N ) :
    return True

  return False

def minStepToReachTarget( knightpos, targetpos, N ) :
  dx = [ 2, 2, -2, -2, 1, 1, -1, -1 ]  # possible movments
  dy = [ 1, -1, 1, -1, 2, -2, 2, -2 ]

  queue = []

  queue.append( cell( knightpos[ 0 ], knightpos[ 1 ], 0 ) )  # start position

  visited = [ [ False for i in range( N + 1 ) ] for j in range( N + 1 ) ]  # default not visited

  visited[ knightpos[ 0 ] ][ knightpos[ 1 ] ] = True

  while( len( queue ) > 0 ) :
    t = queue[ 0 ]
    queue.pop( 0 )

    if( t.x == targetpos[ 0 ] and t.y == targetpos[ 1 ] ) :  # current(t) cell equal to target
      return t.dist

    for i in range( 8 ) :  # simulation all posible
      x = t.x + dx[ i ]
      y = t.y + dy[ i ]

      if( isInside( x, y, N ) and not visited[ x ] [y ] ) :
        visited[ x ][ y ] = True
        queue.append( cell( x, y, t.dist + 1 ) )

def locatePosition( str, list ) :
  if ( str[ 0 ] == "a" ) :
    list.append( 1 )
  elif ( str[ 0 ] == "b" ) :
    list.append( 2 )
  elif ( str[ 0 ] == "c" ) :
    list.append( 3 )
  elif ( str[ 0 ] == "d" ) :
    list.append( 4 )
  elif ( str[ 0 ] == "e" ) :
    list.append( 5 )
  elif ( str[ 0 ] == "f" ) :
    list.append( 6 )
  elif ( str[ 0 ] == "g" ) :
    list.append( 7 )
  elif ( str[ 0 ] == "h" ) :
    list.append( 8 )

  list.append( int( str[ 1 ] ) )

if __name__ == '__main__' :
  print( "Please enter the number...[Exit: 0 0]" )

  while True :
    x, y = input().split()
    if x == "0" and y == "0" :
      break

    knightpos = []
    targetpos = []
    locatePosition( x, knightpos )
    locatePosition( y, targetpos )
    print( "From " + x + " to " + y + ", Knight Moves = " + str( minStepToReachTarget( knightpos, targetpos, 8 ) ) )
    print()