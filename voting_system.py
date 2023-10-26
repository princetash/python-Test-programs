def register_candidates():
    # Initialize an empty list to store candidate names
    candidates = []

    num_candidates = int(input("Enter the number of candidates: "))

    for i in range(num_candidates):
        candidate_name = input(f"Enter the name of candidate {i + 1}: ")
        candidates.append(candidate_name)

    return candidates

def register_voters():
    # Initialize an empty list to store registered voters
    voters = []

    while True:
        voter_name = input("Enter your name (or 'exit' to quit registration): ")
        if voter_name.lower() == 'exit':
            break
        voters.append(voter_name)

    return voters

def voting_system():
    candidates = register_candidates()
    voters = register_voters()

    # Create a dictionary to store candidate votes with initial counts set to zero
    candidate_votes = {candidate: 0 for candidate in candidates}
    
    # Create a set to track voters who have already cast their votes
    voted_voters = set()

    while True:
        name = input("Enter your name (or 'exit' to quit voting): ")

        if name.lower() == 'exit':
            break

        if name not in voters:
            print("You are not registered as a voter.")
            register_choice = input("Do you want to register as a voter? (yes/no): ").strip().lower()
            if register_choice == 'yes':
                voters.append(name)
                print(f"Thank you, {name}, you are now registered as a voter.")
        elif name in voted_voters:
            print("You have already voted. You can't vote again.")
        else:
            print(f"Welcome, {name}! You are eligible for voting.")
            print("Choose one of the candidates below:")
            for candidate in candidates:
                print(candidate)

            choice = input("Enter your choice: ").strip()
            if choice in candidates:
                candidate_votes[choice] += 1
                print(f"You have voted for {choice}.")
                voted_voters.add(name)  # Add the voter to the set of voted voters
            else:
                print("Invalid choice. Try again.")

    print("Voting has ended. Here are the results:")
    for candidate, votes in candidate_votes.items():
        print(f"{candidate}: {votes} votes")

    # Determine the winner
    winner = max(candidate_votes, key=candidate_votes.get)
    print(f"The winner is {winner} with {candidate_votes[winner]} votes!")

if __name__ == "__main__":
    voting_system()
