# from replit import clear

bidders = {}
while another_bid != 'no':
    print("Welcome to the blind auction program.")
    name = input("What is your name?\n").lower()
    bid = int(input("What is your bid?\n$"))
    bidders[name] = bid
    another_bid = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
# clear

bids_list = []
# to get the highest bid
for name in bidders:
    bids_list.append(bidders[name])
max_bid = max(bids_list)

# to get the person who made the highest bid
for name in bidders:
    if max_bid == bidders[name]:
        winner = name
    
print(f'The winner opf the auction is {winner} with a bid of ${bidders[winner]}')  # or {max_bid}
