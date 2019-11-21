from trello import TrelloClient
boardID = "uDtSJilF" # whatever board that is, eg. https://trello.com/b/uDtSJilF/iab207
#init
client = TrelloClient(
    api_key='46e39ef2c47d0a978155d6e097fb333d',
    api_secret='b5943814ebccc4756cdc0e18fa7a05635e313d9b88f61433c9502b971716afb3',
)

# get board
board = client.get_board(boardID)
print(board.id)

# tap that list
list = board.list_lists()
print(list)
list_id=(list[3].id)

for spin in list:
    print(spin)
    list_id= spin.id
    my_list = board.get_list(list_id)
    # shake it up
    for card in my_list.list_cards():
    # throw up
      print(card.name)
      print(card.desc)
