import art
print(art.hammer)

def bid_comparision(bids):
    winner = ""
    heighest_bid = 0
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount>heighest_bid:
            heighest_bid = bid_amount
            winner = bidder
            
    print(f"The winner is {winner} with a heighest bid of {heighest_bid}")

bids = {}   
continue_bidding = True
while continue_bidding:
    name = input("Enter Your name?: ")
    price = int(input("Enter Your price: $"))
    bids[name] = price
    should_continue = input("Is there any other bidder, 'Yes' or 'No': ").lower()
    
    if should_continue == "no":
        bid_comparision(bids)
        continue_bidding = False
        
