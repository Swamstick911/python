# Savings, needs and wants

print("Enter your name please")
name = input()
print(f"Hi there {name}, this is a savings, needs and wants calculator!")

print("Is this for the arcade by hackclub?")
arcade = input().lower()



def play():
    print("Hello this is ticket counter for arcade!")
    print("Enter the tickets you want")
    wantedTickets = int(input())
    print("Enter the tickets you have")
    tickets =  int(input())
    ticketsPercent = tickets/wantedTickets * 100
    print(f"{name} you have completed {ticketsPercent}% of your goal!")
    ticketsLeft = wantedTickets - tickets
    ticketsLeftPercent = ticketsLeft / wantedTickets * 100
    print(f"You have to get {ticketsLeft} more which is {ticketsLeftPercent}%.")


def nsw():
    print("Enter the money you have")
    money = int(input())


    print("Enter the currency")
    currency = input()

    needs = 30/100 * money
    wants = 30/100 * money
    savings = 60/100 * money

    print(f"{name}, you should spend {savings} {currency} towards savings")
    print(f"{needs} {currency} towards needs")
    print(f"and {wants} {currency} towards wants")


if arcade == "yes" or "y":
    nsw()
elif arcade == "no" or "n": 
    play()
