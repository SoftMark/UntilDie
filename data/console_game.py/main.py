from classes.colors import TColors
from classes.add_functions import AdditionalFunctions
from classes.storage import Loader, NamesStorage
from classes.unit_method import SubjectMethods
from classes.units import Objects


day = 1
main_run = True
actions = NamesStorage.main_actions

# Ask to continue
if AdditionalFunctions.ask_to_continue():
    day = Loader.load_data()['day']
    human_data = Loader.load_data()['human']
    player = SubjectMethods.player_loader(human_data)
else:
    player = SubjectMethods.create_human()

while main_run:
    if player.hp == 0:
        player.print_total_hp()
        print(TColors.red + 'Game over.' + TColors.end)
        break
    AdditionalFunctions.print_day(day)
    player.print_info()
    AdditionalFunctions.print_actions(actions)
    main_choice = input()
    print('\n\n')
    if AdditionalFunctions.is_digital(main_choice):
        main_choice = int(main_choice)
        if main_choice == 0:
            main_run = AdditionalFunctions.exit_game(player, day)
        elif main_choice == 1:
            player.work()
            day += 1
        elif main_choice == 2:
            player.go_to_refrigerators_corner()
        elif main_choice == 3:
            player.actions_with_pets()
        elif main_choice == 4:
            player.go_to_mall(Objects.mall_ocean_plaza)
        elif main_choice == 5:
            AdditionalFunctions.ask_to_save(AdditionalFunctions.data_collector(player, day))

