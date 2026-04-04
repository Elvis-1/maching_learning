# import games.game_of_life
# import games.oo_wordgames

from games import game_of_life as gol,oo_wordgames as wg

def main():
  games = {
     'Word games': wg.main,
     'Game of life':  gol.main
  }

  games_list = list(games.keys())
  for i,val in enumerate(games_list):
     print(f'{i+1}. {val}')

  select_one = input('Pick one > ')
  
  if not select_one.isnumeric():
     print('Pick a valid menu')
     return
     
  select_one = int(select_one.strip())
  list_num = select_one - 1

  if len(games_list) > list_num and list_num >= 0:
    game_name = games_list[list_num]
    games[game_name]()
  else:
     print('Pick a valid menu')



if __name__ == '__main__':
    main()