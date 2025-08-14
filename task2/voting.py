class Voting_System:
    def __init__(self):
        self.__candidates = {}

    def add_candidate(self, name, votes):
        self.__candidates[name] = votes

    def remove_candidate(self, name):
        if name in self.__candidates.keys():
            del self.__candidates[name]
        else:
            print("Insuficient input ")

    def vote_candidate(self, name):
        if name in self.__candidates.keys():
            self.__candidates[name] += 1
            print("Vote added")

    def display_winner(self):
        temp = 0
        for name, votes in self.__candidates.items():
            if votes > temp:
                temp = votes
                winner = name
        winners = []
        for name, votes in self.__candidates.items():
            if votes == temp:
                winners.append(name)

        if len(winners) > 1:
            print(f"Tie {winners}")
        elif len(winners) == 1:
            print(f"Winner : {winner}")


voting = Voting_System()
no_of_candidates = int(input("No. of candidates :"))

for i in range(no_of_candidates):
    name = input("Name : ")
    votes = int(input("No. of votes : "))
    voting.add_candidate(name, votes)

while True:
    user_inp = input(
        "what do you want to do? (ADD votes : add)/(display winner : winner)/(Remove candidate : R,remove)(Quit : q) \n ").lower().strip()
    if user_inp in ["add", "a"]:
        name = input("Name : ").lower().strip()
        voting.vote_candidate(name)

    elif user_inp in ["w", "winner"]:
        voting.display_winner()
        break

    elif user_inp in ["r", "remove"]:
        name = input("Name : ").lower().strip()
        voting.remove_candidate(name)

    elif user_inp in ["q", "quit"]:
        break

    else:
        print("Insuficient input ")
