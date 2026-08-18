voters = [
    {
        "id": "Chi",
        "has_voted": False
    },
    {
        "id": "Mitch",
        "has_voted": False
    }
]

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


def cast_vote():

    if len(voters) == 0:
        print("No registered voters.")
        return

    if len(candidates) == 0:
        print("No candidates available.")
        return

    print("\n===== CANDIDATES =====")

    for i, candidate in enumerate(candidates):
        print(i + 1, "-", candidate["name"])

    # Keep asking for Voter ID until it is registered
    while True:

        voter_id = input("\nEnter Voter ID: ").strip()

        selected_voter = None

        # Search for the voter
        for voter in voters:
            if voter["id"] == voter_id:
                selected_voter = voter
                break

        # If voter is not registered, ask again
        if selected_voter is None:
            print("Voter is not registered.")
            print("Please enter a registered Voter ID.")
            continue

        # Voter is registered
        break

    # Check if voter already voted
    if selected_voter["has_voted"]:
        print("You have already voted!")
        return

    # Ask voter to choose a candidate
    while True:

        try:
            choice = int(
                input("Enter Candidate Number to Vote: ")
            )

            if 1 <= choice <= len(candidates):

                candidates[choice - 1]["votes"] += 1
                selected_voter["has_voted"] = True

                print("\n------------------------------")
                print("Vote cast successfully!")
                print(
                    "You voted for:",
                    candidates[choice - 1]["name"]
                )
                print("------------------------------")

                break

            else:
                print("Invalid candidate number.")
                print("Please choose a valid candidate.")

        except ValueError:
            print("Please enter a valid number.")


#Start voting
cast_vote()
