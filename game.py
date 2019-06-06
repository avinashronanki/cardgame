import random
outdated_deck=[] 
player1_has_resurrect=True
player2_has_resurrect=True 
player1_has_godspell=True
player2_has_godspell=True 
player1_score=0
player2_score=0
i = 0

# import random
def dice():
  print('start the game')
  p1=random.randint(1,6)# generats a random number with in the specified range 
  print("player1 rolled",p1)

  p2=random.randint(1,6)
  print("player2 rolled",p2)
  if (p1>p2):
    print('player1 is winner')
    return(1)
  elif(p2>p1):
    print('player2 is winner')
    return(2)
  else:
    print('roll the dices again')
    dice()
# dice()


def cards():
#   print("roll the dices")
#   print('Start the game')
  print('winner has to either start the battel or choose god spell',)
  list_card=[{'name':'virat','matchs':300,'runs':12000,'wickets':5,'mom':20},
  {'name':'hitman','matchs':295,'runs':11000,'wickets':15,'mom':18},
  {'name':'dhawan','matchs':250,'runs':10000,'wickets':2,'mom':10},
  {'name':'dhoni','matchs':350,'runs':14000,'wickets':8,'mom':30},
  {'name':'kl','matchs':50,'runs':4000,'wickets':9,'mom':6},
  {'name':'jaddu','matchs':150,'runs':1400,'wickets':170,'mom':3},
  {'name':'kedhar','matchs':80,'runs':4500,'wickets':18,'mom':4},
  {'name':'bhuvi','matchs':180,'runs':500,'wickets':250,'mom':4}]

  random.shuffle(list_card)#shuffling cards using random.shuffle function
#   for card in list_card: 
#       print(card)
#   print('\n')
  
  global player1,player2
  player1=list_card[0:4]
#   for p1 in player1:
#     print(p1)

  print('\n')

  player2=list_card[4:]
#   for p2 in player2:
#     print(p2)
    
  print('\n') 
cards()
next_turn=dice()    


def battle():
  global next_turn, outdated_deck, player1, player2, player1_score, player2_score
  
  if next_turn == 1:
    print('Player1 has to choose the strength: matchs or runs or wickets or mom')
  else:
    print('Player2 has to choose the strength: matchs or runs or wickets or mom')
    
  strength=input()
  if player1[0][strength]>player2[0][strength]:#comparing the cards with strength 
    player1_score=player1_score+1# adding the score to the player
    print('player1 is winnner')
    next_turn = 1 
  else:
    player2_score=player2_score+1
    print ('player2 is winner')
    next_turn = 2
  print("player1 score",player1[0][strength],"player2 score",player2[0][strength])
  outdated_deck.append(player1[0])    #outdated deck  
  outdated_deck.append(player2[0])    
  #outdated_deck
  player1=player1[1:] # removing the first card of the list 
  player2=player2[1:]


  #resurrect spell condition
# outdated_deck=[]
def resurrect(player_number):
  global player1,player2,player1_has_resurrect,player2_has_resurrect,outdated_deck
  if player_number==1:
    if player1_has_resurrect:
      print('has ressurect')
      random.shuffle(outdated_deck)
      picked_card=outdated_deck[0]
#        picked_card = random.choice(outdated_deck)
      player1 = [picked_card]+player1
      outdated_deck = outdated_deck[1:]
      player1_has_resurrect=False 
    else:
      print('resurrect has been used')
  else:
    if player2_has_resurrect:
      print('has ressurect')
      random.shuffle(outdated_deck)
      picked_card=outdated_deck[0]
      player2 = [picked_card]+player2
      outdated_deck = outdated_deck[1:]
      player2_has_resurrect=False 
    else:
      print('resurrect has been used')  

      #god spell
def god(player_number): 
  global player1,player2,player2_has_godspell,player1_has_godspell
  if (player_number==1):
    if player1_has_godspell:
#       print('player has god spell to use')
      print('player1 has to pick a card from opnent deck')
      print('The number of cards the opponent has:', len(player2))
      choice = int(input())  
      if(len(player2)==1):
          print('cannot choose god spell has the player left with one card')
          return    
      if(choice >= len(player2)):
        print('invalid choice, enter again')
        god(player_number)
      remove_card=player2.pop(choice)
      player2 = [remove_card] + player2
      player1_has_godspell=False
    else:  
      print('godspell has been used')
      
  else:
    if player2_has_godspell:
      print('player2 has to pick a card from opnent deck')
      print('The number of cards the opponent has:', len(player1))
      choice = int(input())  
      if(len(player1)==1):
          print('cannot choose god spell has the player left with one card')
          return    
      if(choice >= len(player1)):
        print('invalid choice, enter again')
        god(player_number) 
      remove_card=player1.pop(choice)
      player1 = [remove_card] + player1
      player2_has_godspell=False
    else:  
      print("godspell has been used ")

      

def round(turn):
  global player1,player2, player1_score, player2_score, next_turn
  if next_turn == 1:
    print('Player 1 turn')
  else:
    print('Player 2 turn')
    
  print(' press B to choose battle or RS to choose Resurect spell or GS to god spell')
  players_option=input()
  if (players_option=='b'): 
    battle()
  elif(players_option=='rs'):
    print('player has to choosen Resurrect spell')
    resurrect(next_turn)
    print('oppnent has option to choose RS. Press p to pass.')
    next_rs=input()
    if(next_rs == 'rs'):
      if next_turn == 1:
        resurrect(2)
        battle()
      else:
        resurrect(1)
        battle()
    elif(next_rs=='p'):
      battle()      
  elif(players_option=='gs'):
    print('player has choose god spell,can pick choice of his card from opponent deck')
    god(next_turn)
    print('oppnent has option to choose RS. Press p to pass.')
    next_rs=input()
    if(next_rs == 'rs'):
      if next_turn == 1:
        resurrect(2)
        battle()
      else:
        resurrect(1)
        battle()
    elif(next_rs=='p'):
      battle() 
  else: 
    print('wrong option,Choose B or RS or GS')
    players_option=input()
  
  
while len(player1) > 0 and len(player2) > 0:
  round(i)
  i += 1

  
print("game ends")
if (player1_score==player2_score): 
  print("Its a Draw" )
elif(player1_score>player2_score):
   print('player1 has won the game',player1_score)
else:
  print('player2 has won the game',player2_score)
               



  