def get_votes(candidate):
    return candidate["votes"]


def view_results(candidates):

    if not candidates:
        print("\nNo candidates available.")
        return

    print("\n------- VOTING RESULTS -------")
    print("Candidates              Votes")
    print("--------------------------------")

    # Sort candidates from highest votes to lowest
    sorted_candidates = sorted(
        candidates,
        key=get_votes,
        reverse=True
    )

    for candidate in sorted_candidates:
        print(
            f"{candidate['name']:<20} "
            f"{candidate['votes']} vote(s)"
        )

    # Calculate total votes
    total = sum(
        candidate["votes"]
        for candidate in candidates
    )

    winner = sorted_candidates[0]

    print("--------------------------------")
    print(f"Total Votes: {total}")

    print(
        f"\nWinner: {winner['name']} "
        f"with {winner['votes']} votes!"
    )
