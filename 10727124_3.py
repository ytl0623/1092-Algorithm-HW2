# 演算法分析機測
# 學號 : 10727124
# 姓名 : 劉宇廷
# 中原大學資訊工程系
# 霍夫曼碼 (Huffman Codes)

class Node :
  def __init__( self, freq, char ) :
    self.left = None
    self.right = None
    self.father = None
    self.freq = freq
    self.char = char

  def isLeft( self ) :
    return self.father.left == self

def createNodes( freqs, char ) :
  newNode = Node( freqs, char )
  return newNode

def createHuffmanTree( nodes ) :
  queue = nodes[:]

  while len( queue ) > 1 :  # one by one by nodes
    queue.sort( key = lambda item : item.freq )

    node_left = queue.pop( 0 )  # extract min and put in left
    node_right = queue.pop( 0 )  # extract second-min and put in right
    node_father = Node( node_left.freq + node_right.freq, None )  # add left's and right's frequence together
    node_father.left = node_left
    node_father.right = node_right
    node_left.father = node_father
    node_right.father = node_father

    queue.append( node_father )  # new node insert queue

  queue[ 0 ].father = None
  return queue[ 0 ]  # return root of the huffman tree

def huffmanEncoding( nodes, root ) :
  codes = [''] * len( nodes )

  for i in range( len( nodes ) ) :
    node_tmp = nodes[ i ]

    while node_tmp != root :
      if node_tmp.isLeft() :
        codes[ i ] = "0" + codes[ i ]
      else :
        codes[ i ] = "1" + codes[ i ]

      node_tmp = node_tmp.father

  return codes

if __name__ == '__main__' :
  cnt = 1
  print( "Please enter the number...[Exit: 0]" )

  while 1 :
    n = int( input() )
    if n == 0 :
      break

    frequency = []
    for _ in range( n ) :
      tempList = input().split()
      tempList[ 1 ] = int( tempList[ 1 ] )
      frequency.append( tuple( tempList ) )

    nodes = []
    for i in range( len( frequency ) ) :
      nodes.append( createNodes( frequency[ i ][ 1 ], frequency[ i ][ 0 ] ) )  # allocate new nodes

    print()
    root = createHuffmanTree( nodes )  # create huffman tree by nodes
    codes = huffmanEncoding( nodes, root )

    temp = []
    for item in zip( frequency, codes ) :
      temp.append( item )

    temp.sort( key = lambda tup : tup[ 0 ] )

    print( "Huffman Codes #%d" %cnt )

    for item in temp :
      print( item[ 0 ][ 0 ], item[ 1 ] )

    print()
    cnt += 1