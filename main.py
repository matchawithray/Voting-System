candidates = [
    {
        "name": "Xyra",
        "votes": 0
    },
    {
        "name": "Mitchie",
        "votes": 0
    },
    {
        "name": "Raymart",
        "votes": 0
    }
]

voters = [
    {
        "id": "V001",
        "has_voted": False
    }
]


# ------------------------------
# CAST VOTE
# ------------------------------

def cast_vote():

    print("\n===== VOTING SYSTEM =====")

    # Show candidates first
    print("\n----- CANDIDATES -----")

    for i, candidate in enumerate(candidates):
        print(i + 1, "-", candidate["name"])

    # Ask for voter ID
    voter_id = input("\nEnter Voter ID: ")

    selected_voter = None

    # Check if voter is registered
    for voter in voters:
        if voter["id"] == voter_id:
            selected_voter = voter
            break

    if selected_voter is None:
        print("Voter is not registered.")
        return

    # Check if already voted
    if selected_voter["has_voted"]:
        print("You have already voted!")
        return

    # Ask for candidate
    try:
        choice = int(input("Enter Candidate Number to Vote: "))

        if 1 <= choice <= len(candidates):

            candidates[choice - 1]["votes"] += 1
            selected_voter["has_voted"] = True

            print("\n------------------------------")
            print("Vote cast successfully!")
            print("You voted for:",
                  candidates[choice - 1]["name"])
            print("------------------------------")

        else:
            print("Invalid candidate number.")

    except ValueError:
        print("Please enter a valid number.")


# Start voting
cast_vote()
