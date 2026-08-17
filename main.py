# mainn tooo
#Python
#xyra to ahhh
#RESULTS SA AKIN

candidates = [
  {"name": "Alice", "votes": 3},
  {"name": "Bob", "votes": 2},
  {"name": "Mesye", "votes": 1}
]

def view_results():
  if len(candidates) == 0:
    print("No candidates available.")
    return

  print("\n-----VOTING RESULTS-----")

  for candidate in candidates:
    print(candidate['name'], '-', candidate['votes'], 'vote(s)')

view_results()
