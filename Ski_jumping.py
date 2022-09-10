# Competition and season simpe simulation.
import random

class Player:
    def __init__(self,name,skils,sports_form):
        self.name = name
        self.skils = skils
        self.sports_form = sports_form

    def __repr__(self):
        return self.name

class Ski_jump:
    def __init__(self,name,construction_point,ski_jump_record):
        self.name = name
        self.construction_point = construction_point
        self.ski_jump_record = ski_jump_record

    def __repr__(self):
        return self.name

    def turnament_simulation(self,players_list):
        self.players_list = players_list
        print("Ski jump name:",self.name)
        print("Players list:",str(len(players_list)))

        results = {}
        points_per_competition=[100,90,80]
        self.general_classification={}

        for player in players_list:
            wind= random.randint(-10, 10)
            other_factors = random.randint(-10, 10)
            jump_length = self.construction_point + player.skils + (2 * player.sports_form) + (
                    2 * wind) + other_factors
            print("Player",player.name,"got length",jump_length,"m.")
            if jump_length > self.ski_jump_record:
                print("Ski jump record was beat by ",player.name)
                self.ski_jump_record = jump_length
            elif jump_length == self.ski_jump_record:
                print("Ski jump record was align by", player.name, "!")
            results[jump_length] = player
        results = sorted(results.items(),reverse=True)

        print("*******************")
        print("Competition results", self.name, ":")
        for key,value in results:
            print(value,key,"m.")
        for i in range(len(results)):
            self.general_classification[results[i][1]]=points_per_competition[i]

        print("*******************")
        print("Points to general classification after competition: ")
        for key in self.general_classification:
            print(key,self.general_classification[key])
        print("#######################################################################################")

class Season:
    def __init__(self,name,players_list,ski_jump_list):
        self.name = name
        self.players_list = players_list
        self.ski_jump_list = ski_jump_list

    def __repr__(self):
        return self.name

    def season_simulation(self):
        print(repr(Season("SEASON 2022",players_list,ski_jump_list)))
        temporary_season_summary = []
        for ski_jump in ski_jump_list:
            ski_jump.turnament_simulation(players_list)
            temporary_season_summary.append(ski_jump.general_classification)

        final_season_summary = {}
        for dictionary in temporary_season_summary:
            for k, v in dictionary.items():
                if k in final_season_summary:
                    final_season_summary[k] += v
                else:
                    final_season_summary[k] = v

        final_summary = sorted(final_season_summary,key=lambda x : final_season_summary[x], reverse=True)

        print("General classification after season: ")

        for key in final_summary:
            print(key,final_season_summary[key],"points")

players_list = [
    Player(name="Adam Małysz",skils=10,sports_form=10),
    Player(name="Robert Mateja",skils=5,sports_form=10),
    Player(name="Simon Ammann",skils=9,sports_form=10),
]

ski_jump_list = [
    Ski_jump("Vikersund",200,253.5),
    Ski_jump("Planica",200,252),
    Ski_jump("Harrachov",185,214.5),
]
tournament1 = Season("SEASON 2022",players_list,ski_jump_list)
tournament1.season_simulation()


