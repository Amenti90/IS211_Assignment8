# imports for the system function calling and random function generation
import sys
import random
import time
# function for getting the number value from the user
def input_number(prompt='enter the number: ', small=0, large=None):
    """reads only the positive number within the range."""
# while loop for checking the given condition inside the block
    while True:
        # try block for for checking smaller and larger inputs
        try:
            total = int(input(prompt))
            # if statement for checking the given condition
            if (total < small or
                (large is not None and total > large)):
                    print('The entered number is not in the given range!: {} to {}'.format(small, large))
            # else part for bound out of the condition
            else:
                break
# error message printing for getting only number values
        except ValueError:
            print('only numbers are accepted ! so enter only numbers')
            continue
# returning the total value if the given input is number
    return total

# class for throwing the exception during the one combination occurrence during rolling of the dice
class RollOneProblem(Exception):
    pass

# class for representing the dices
class Dice:
    """dice representation."""
# function for select the random players
    def __init__(self):
        self.value = random.randint(1, 6)
# function for dice roll other than the one combination
    def roll(self):
        """Throws exception when it is 1."""

        self.value = random.randint(1, 6)
        if self.value == 1:
            raise RollOneProblem
# block for finding the one combination die rolling
        return self.value

# block for rolled dices
    def __str__(self):
        return "Rolled " + str(self.value) + "."

# class for adding the temporary scores
class Temp:
    """class which saves only the temporary scores."""
    def __init__(self):
        self.value = 0

# function which resets the value to zero if the one combination occurs
    def reset(self):
        self.value = 0

# function for adding the value to the dice
    def dice_value_adding(self, value_of_dice):
        self.value += value_of_dice

# class for adding the total number of players
class Player(object):
    """class for adding different number of players."""

# block for choosing the name of the players and their respective points or scores
    def __init__(self, title=None):
        self.title = title
        self.point = 0

# function for adding the player scores
    def adding_score(self, player_score):
        """adds the player scores ."""

        self.point += player_score

# block which returns the player scores as well their names
    def __str__(self):
        """player point and name return through this function."""

        return str(self.title) + ": " + str(self.point)

# class for setting the computer player names
class ComputerPlayer(Player):
    computer_name=['CPU 0', 'CPU 1', 'CPU 2', 'CPU 3']

# block for assigning the scores to the computer players
    def __init__(self, total):
        """Assigning the names to the cpu when the player chooses the computer player#."""
# if statement for finding the total score for the computer players
        if total < len(self.computer_name):
            title = self.computer_name[total]
        else:
            title = 'Cpu{}'.format(total)
# super statement for setting the name of the respective player
        super(ComputerPlayer, self).__init__(title)

# function for rolling the dice and its temporary score
    def rolling_dices(self, temperoray):
        """Dice rolls randomly until the player selects the hold during the game."""
# while loop for checking whether the computer rolls or computer holds
        while temperoray.value < (25 + random.randint(1, 6)):
            print(" computer rolls the dice again.")
            return True
        # if the above while condition is false then this block will execute
        print("  computer holds the dice.")
        return False

# class for the human players to set their names
class HumanPlayer(Player):
    def __init__(self, title):
        super(HumanPlayer, self).__init__(title)

# function for rolling dices for the human players
    def rolling_dices(self, temperoray):
        """Asks the human player, if they want to keep rolling."""
# getting the inputs from the users during the dice rolling ( if the input is 1 then the player wants to roll again: if the input is 0 then the player holds the dice and don't want to continue)
        human_decision = input_number("  1 - Roll, 0 - Hold ", 0, 1)
        if human_decision == 1:
            return True
# else part will execute if the above condition fails to satisfy
        else:
            return False

# class for control the game players (both human and computer players)
class Game_controller:
    def __init__(self, human_player=1, computer_player=1):
        """starts the game-play, and asking the player names."""

        self.gamers = []
        # if statement for checking whether the number of human players is equal to 1 or not
        if human_player == 1:
            self.gamers.append(HumanPlayer('player(human)'))
        # else part for the players more than one and need to enter the name of the players
        else:
            for i in range(human_player):
                player_name = input('please enter names of player number.{}: '.format(i))
                self.gamers.append(HumanPlayer(player_name))
# finding the total number of computer players
        for i in range(computer_player):
            self.gamers.append(ComputerPlayer(i))

        self.total_number_players = len(self.gamers)

        self.dices = Dice()
        self.temperoray = Temp()

# method for welcoming message
    @staticmethod
    def message():
        """welcoming message before starting the game."""

        print("#" * 50)
        print("Pig Dice game welcomes you!" .center(50))
        print("#" * 50)
        #rules of the game
        print("Rules of the game" .center(50))
        print("For winning this game a player needs to point 100 points at first." .center(50))
        print("for every turn,every player suppose to roll the dice." .center(50))
        print("for every occurrence to every player the die will save the temporary point." .center(50))
        print("(If the die combination is 1 then no points were awarded also the temporary point will lose," .center(50))
        print("also the turn will automatically goes to the next waiting player.)" .center(50))
        print("waiting player will continues after this," .center(50))
        print("waiting player may also hold for another player to play." .center(50))
        print("points will be added according the temporary point condition is pass." .center(50))
        print("if 1 combination occurs then the temporary point will lost! " .center(50, "#"))
        #game tricks
        print("It is good advice that don't roll to much times " .center(50, "#"))
        print("All the best " .center(50, "#"))
        print("Think and play the game ! " .center(50, "#"))
        print()
        # automatic allocation of the intial player
        print("System will automatically generate that who will start " .center(50, " "))
        print()

# function for choosing the automatic first player selection
    def random_first_player_deciding(self):
        """function for random player selection."""

        self.currently_playing_gamer = random.randint(1, self.total_number_players) % self.total_number_players

        print('{} starts'.format(self.gamers[self.currently_playing_gamer].title))

# function for waiting player
    def upcoming_player(self):
        """function for next waiting player turn."""
        self.currently_playing_gamer = (self.currently_playing_gamer + 1) % self.total_number_players

# function for
    def player_before(self):
        """Function for previous player details."""

        self.currently_playing_gamer = (self.currently_playing_gamer - 1) % self.total_number_players
# function for getting the total score

    def total_score_getting(self):
        """function for previous player scores."""

        return ', '.join(str(player) for player in self.gamers)

# function for game play
    def play_game(self):
        """function for full game."""

        self.message()
        self.random_first_player_deciding()
# while condition for checking the 100 game winning point for the players
        while all(player.point < 100 for player in self.gamers):
            print('\npoint now is >> {}'.format(self.total_score_getting()))
            print('\n*** {} play next ***'.format(self.gamers[self.currently_playing_gamer].title))
            self.temperoray.reset()

            while self.rolling_dices():
                pass
# adding scores to the previous game points
            self.gamers[self.currently_playing_gamer].adding_score(self.temperoray.value)
            self.upcoming_player()

        # block for the previous player winning..
        self.player_before()
        print(' {} has won the game '.format(self.gamers[self.currently_playing_gamer].title).center(50, '#'))

    # function for dice rolling
    def rolling_dices(self):
        # try block for checking the temporary score and adds the score to the existing score
        try:
            value_of_dice = self.dices.roll()
            self.temperoray.dice_value_adding(value_of_dice)
            print('Last roll is: {}, fresh score value is: {}'.format(value_of_dice, self.temperoray.value))

            return self.gamers[self.currently_playing_gamer].rolling_dices(self.temperoray)
# if the one combination occurs then temporary scores resets to zero
        except RollOneProblem:
            print('  Rolls one time. next turn starts')
            self.temperoray.reset()
            return False
# main function which chooses total number players and computers are going to play this game
class Game(object):
    
    def __init__(self, gamers='gamers', currently_playing_gamer='currently_playing_gamer'):
       
        pigplayers = PlayerFactory()
        self.gamers = pigplayers.player_type(args.gamers)
        self.currently_playing_gamer = pigplayers.player_type(args.currently_playing_gamer)
        self.die = Die()
        self.turn(self.gamers)

  
class TimedGameProxy(Game):
   
    def __init__(self):
      
        self.start_time = time.time()
        Game.__init__(self, 'gamers', 'currently_playing_gamer')

    def time_keeper(self):
        if time.time() - self.start_time >= 60:
            if self.gamers.total_score_getting > self.currently_playing_gamer.total_score_getting:
                print ('Time is up! {} '
                       'wins with a score '
                       'of {}.').format(self.gamers.name,
                                        self.gamers.total_score_getting)
            else:
                print ('Time is up! {} '
                       'wins with a score '
                       'of {}.').format(self.currently_playing_gamer.name,
                                        self.currently_playing_gamer.total_score_getting)
                raise SystemExit
        else:
            time_left = time.time() - self.start_time
            print ('{} one minute has elapsed since the start of the game').format(time_left)
def main():
    human_players = input_number('choose number of human players to play the game? ')
    players_of_computers = input_number('choose number of computer(CPU) players to play the game? ')
     # game controller block for controlling both computer and human players
    gaming_console = Game_controller(human_players, players_of_computers)
    gaming_console.play_game()

# main block
if __name__ == '__main__':
    main()
#end of the pig dice program
