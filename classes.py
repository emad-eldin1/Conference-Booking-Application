conferenceName = "Python Conference"

ticketPrice = {
    "egypt": 5,
    "libia": 2,
    "spain": 20
}

setOfCountries = {"egypt", "libia", "spain"}

listOfUsers = []

conferenceTickets = {
    "egypt": 50,
    "libia": 30,
    "spain": 10,
}

def validateUserInput(user):
    if len(user["name"]) < 3:
        return "Invalid name"
    elif user["age"] < 18:
        return "Invalid Age"
    elif '@' not in user["email"]:
        return "Invalid Email"
    elif user["country"] not in setOfCountries:
        return "The conference is not available in your country"
    elif user["numberOfTickets"] > conferenceTickets[user["country"]]:
        return f'You can\'t book {user["numberOfTickets"]} tickets, there are only {conferenceTickets[user["country"]]} tickets available'
    else:
        return None

def checkOut(newUser):
    cost = newUser["numberOfTickets"] * ticketPrice[newUser["country"]]
    listOfUsers.append(newUser)
    conferenceTickets[newUser["country"]] -= newUser["numberOfTickets"]
    return cost

def isTicketsAvailable():
    count = 0
    for _, value in conferenceTickets.items():
        if value == 0:
            count += 1
    return count != len(conferenceTickets)
