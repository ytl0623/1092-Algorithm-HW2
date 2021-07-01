# 演算法分析機測
# 學號 : 10727124
# 姓名 : 劉宇廷
# 中原大學資訊工程系
# 單一源 最短路徑 (Single-Source Shortest Paths)

import sys

class Graph() :
  def __init__( self, vertices ) :
    self.V = vertices
    self.graph = [ [ 0 for column in range( vertices ) ] for row in range( vertices ) ]

  def build( self, v1, v2, value ) :
    self.graph[ v1 - 1 ][ v2 - 1 ] = value

  def printSolution( self, dist, SourceVertex ) :
    print()
    for node in range( self.V ) :
      if node != SourceVertex - 1 :  # number vs. index
        print( str( SourceVertex ) + " to " + str( node + 1 ) + " = " + str( dist [ node ] ) )
    print()

  def minDistance( self, dist, sptSet ) :
    min = sys.maxsize
    min_index = 0

    for v in range( self.V ) :
      if dist[ v ] < min and sptSet[ v ] == False :
        min = dist[ v ]
        min_index = v

    return min_index

  def dijkstra( self, SourceVertex ) :
    dist = [ sys.maxsize ] * self.V  # adjacency matrix
    dist[ SourceVertex - 1 ] = 0  # number vs. index
    sptSet = [ False ] * self.V

    for cout in range( self.V ) :
      u = self.minDistance( dist, sptSet )  # u is first index

      sptSet[ u ] = True  # put minimum distance vertex in shotest path tree

      for v in range( self.V ) :  # if current(v) distance > u's
        if self.graph[ u ][ v ] > 0 and sptSet[ v ] == False and dist[ v ] > dist[ u ] + self.graph[ u ][ v ] :
          dist[ v ] = dist[ u ] + self.graph[ u ][ v ]

    self.printSolution( dist, SourceVertex )

if __name__ == '__main__' :
  print( "Please enter the number...[Exit: 0]" )

  while True :
    n = int( input( ) )
    if n == 0 :
      break
    g = Graph( n )

    edge = int ( input() )
    SourceVertex = int( input() )

    for _ in range( edge ) :
      v1, v2, value = input().split()
      v1 = int( v1 )
      v2 = int( v2 )
      value = int( value )
      g.build( v1, v2, value )

    g.dijkstra( SourceVertex )  # number vs. index