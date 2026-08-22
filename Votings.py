voters = [
    {"id": "Chi", "has_voted": False},
    {"id": "Xyy", "has_voted": False},
    {"id": "Ray", "has_voted": False},
    {"id": "A", "has_voted": False},
    {"id": "B", "has_voted": False},
    {"id": "C", "has_voted": False},
    {"id": "D", "has_voted": False},
    {"id": "E", "has_voted": False},
    {"id": "F", "has_voted": False},
]


def cast_vote(voters, candidates):

    if len(voters) == 0:
        print("\nNo registered voters.")
        return

    if len(candidates) == 0:
        print("\nNo candidates available.")
        return

    print("\n==============================")
    print("        CAST YOUR VOTE")
    print("==============================")

    print("\n----- CANDIDATES -----")

    for i, candidate in enumerate(candidates, 1):
        print(i, "-", candidate["name"])

    # Ask for voter ID
    while True:

        voter_id = input("\nEnter Voter ID: ").strip()

        selected_voter = None

        # Find the voter
        for voter in voters:
            if voter["id"] == voter_id:
                selected_voter = voter
                break

        # Voter ID does not exist
        if selected_voter is None:
            print("\nVoter is not registered.")
            print("Please enter a registered Voter ID.")
            continue

        # Voter has already voted
        if selected_voter["has_voted"]:
            print("\nThis Voter ID has already voted!")
            print("Please enter another Voter ID.")
            continue

        # Valid voter
        break

    # Ask for candidate
    while True:

        try:
            choice = int(
                input("Enter Candidate Number to Vote: ")
            )

            if 1 <= choice <= len(candidates):

                # Add vote
                candidates[choice - 1]["votes"] += 1

                # Mark voter as having voted
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
                print("\nInvalid candidate number.")
                print("Please choose a valid candidate.")

        except ValueError:
            print("\nPlease enter a valid number.")
            print("\nPlease enter a valid number.")
