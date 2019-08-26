import random
rels={
    "scissors":{
        "attacks":"paper",
        "draws":"scissors"
    },
    "paper":{
        "attacks":"rock",
        "draws":"paper"
    },
    "rock":{
        "attacks":"scissors",
        "draws":"rock"
    }
}
print("Lets begin")
options=["scissors","paper","rock"]
user_expression="_"
while user_expression:
    user_expression=str(input("Rock Paper Scissors: ")).lower()
    comp_expression=options[random.randint(0,(len(options)-1))]
    try:
        if rels[user_expression]["attacks"]==comp_expression:
            print("I chose ",comp_expression)
            print("Bruh you fuckin won. But here winners always quit")
        elif rels[comp_expression]["attacks"]==user_expression:
            print("I chose ",comp_expression)
            print("You lose bitch! Ha die in hell loser.")
        elif rels[user_expression]["draws"]==comp_expression:
            print("I chose ",comp_expression)
            print("Its an effin' draw ")
    except:
        print("What the fuck did you type you piece of shit human?")
else:
    print("Just leave!")