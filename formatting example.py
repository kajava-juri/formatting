"""
Kirjeldus:
lihtsam versioon 
    saab mängida kahekesi 
		mäng tuvastab olukorra kui üks mängija on võitnud või on saabunud viik
"""

global_board = {
  'k9':9,
  'k8':8,
  'k7':7,
  'k6':6,
  'k5':5,
  'k4':4,
  'k1':1,
  'k2':2,
  'k3':3
  }
def draw_board(board):
    s1 = '''
    {k7} | {k8} | {k9}
    ----------
    {k4} | {k5} | {k6}
    ----------
    {k1} | {k2} | {k3} 
    '''.format(**board)
    print(s1)    

def check_for_winner(board, player):
  print ("kontrollin")
  #horisontaalid
  h1 = board['k1'] == player and board['k2'] == player and board['k3'] == player
  h2 = board['k4'] == player and board['k5'] == player and board['k6'] == player
  h3 = board['k7'] == player and board['k8'] == player and board['k9'] == player
  #vertikaalid
  v1 = board['k1'] == player and board['k4'] == player and board['k7'] == player
  v2 = board['k2'] == player and board['k5'] == player and board['k8'] == player
  v3 = board['k3'] == player and board['k6'] == player and board['k9'] == player
  #diagonaalid
  d1 = board['k7'] == player and board['k5'] == player and board['k3'] == player
  d2 = board['k1'] == player and board['k5'] == player and board['k9'] == player
  if h1 or h2 or h3 or v1 or v2 or v3 or d1 or d2:
    return True
  else:
    return False

print ("X alustab")
player = "X"
for kord in range(9):
  draw_board(global_board)
  sisend = input("Mängija " + player + " vali koht ruudustikus (numbrid 1-9): ")
  global_board['k' + sisend] = player
  
  if kord >= 4:
    if check_for_winner(global_board, player) == True:
      print(player, "on võitnud!")
      break
  if player == "X":
      player = "O"
  else:
      player = "X"
  if kord == 8:
    print ("viik!")