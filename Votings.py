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

    # Keep the voting system running
    while True:

        print("\n==============================")
        print("        VOTING SYSTEM")
        print("==============================")

        print("\n----- CANDIDATES -----")

        for i, candidate in enumerate(candidates):
            print(i + 1, "-", candidate["name"])

        # Keep asking for a valid voter ID
        while True:

            voter_id = input("\nEnter Voter ID: ").strip()

            selected_voter = None

            # Find voter
            for voter in voters:
                if voter["id"] == voter_id:
                    selected_voter = voter
                    break

            # ID does not exist
            if selected_voter is None:
                print("Voter is not registered.")
                print("Please enter a registered Voter ID.")
                continue

            # ID has already voted
            if selected_voter["has_voted"]:
                print("This Voter ID has already voted!")
                print("Please enter another Voter ID.")
                continue

            # Valid voter who has not voted
            break

        # Ask for candidate
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

        # Return to Voter ID after voting
        print("\nReady for the next vote.")

        continue


#Start voting
cast_vote()
