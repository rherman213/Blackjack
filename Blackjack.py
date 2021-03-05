from tkinter import *
import random

def playHand():
    global money
    global betAmount
    checkAmount = checkBet()
    if (int(betAmount) > int(money) - int(betAmount)) and int(money) - int(betAmount) >= 0 :
        betButton.pack_forget()
        hitButton.pack(side=LEFT)
        standButton.pack(side=RIGHT)
        playerLabel.config(text='Player Cards    \n\n')
        betAmount = int(betAmountSpin.get())
        money -= betAmount
        moneyLabel.config(text="$" + str(money) + " \t\t           ")
        dealCards()
    elif checkAmount == 0:
        betButton.pack_forget()
        hitButton.pack(side=LEFT)
        standButton.pack(side=RIGHT)
        doubleButton.pack(side = RIGHT)
        playerLabel.config(text='Player Cards    \n\n')
        betAmount = int(betAmountSpin.get())
        money -= betAmount
        moneyLabel.config(text = "$"+str(money)+ " \t\t           ")
        dealCards()
    elif checkAmount == -1:
        playerLabel.config(text="Player Cards \n Not Enough Funds\n\n")
    elif checkAmount == -2:
        playerLabel.config(text="Player Cards \n Cannot bet 0\n\n")
    elif checkAmount == -3:
        playerLabel.config(text="Player Cards \n  Illegal Bet \n\n")


def checkBet():
    #Return 0 = Good Bet    -1 = Not enough funds   -2 = Zero Bet     -3 = Negative Bet
    global money
    global betAmount
    betAmount = betAmountSpin.get()
    if int(betAmount) == 0:
        return -2
    if int(betAmount) > int(money):
        return -1
    if int(betAmount) < 0:
        return -3
    else:
        return 0

def dealCards():
    global dealerCards
    global playerCards
    global roundCards
    global cards
    global cardNum
    dealerCards = []
    playerCards = []
    pOriginal = []
    dOriginal = []
    roundCards = []
    cardNum = 0

    cards = ["A♤", "2♤", "3♤", "4♤", "5♤", "6♤", "7♤", "8♤", "9♤", "10♤", "J♤", "Q♤", "K♤",
             "A♧", "2♧", "3♧", "4♧", "5♧", "6♧", "7♧", "8♧", "9♧", "10♧", "J♧", "Q♧", "K♧",
             "A♢", "2♢", "3♢", "4♢", "5♢", "6♢", "7♢", "8♢", "9♢", "10♢", "J♢", "Q♢", "K♢",
             "A♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥"]
        #      1     2     3     4     5     6      7     8     9      10    11     12     13
        #     14    15    16    17    18    19     20    21    22      23    24     25     26
        #     27    28    29    30    31    32     33    34    35      36    37     38     39
        #     40    41    42    43    44    45     46    47    48      49    50     51     52

    for i in range(20):
        n = random.randint(1,51)
        if n in roundCards:
            n = random.randint(1, 51)
        else:
            roundCards.append(n)
    print(roundCards)

    #Deal cards to dealer
    dealerCards.append(roundCards[cardNum])
    cardNum += 1
    dealerCards.append(roundCards[cardNum])
    cardNum += 1
    dealerCardsLabel.config(text = cards[dealerCards[0]] + "    ?? \n\n")

    #Deal Cards to player
    playerCards.append(roundCards[cardNum])
    cardNum +=1
    playerCards.append(roundCards[cardNum])
    cardNum +=1
    playerCardsLabel.config(text = cards[playerCards[0]] + "   " + cards[playerCards[1]])
    checkHand()

def double():
    global playerCards
    global roundCards
    global cardNum
    global cards
    global doubleDown
    global betAmount
    global money
    doubleDown = True
    playerCards.append(roundCards[cardNum])
    cardNum += 1
    money -= betAmount
    moneyLabel.config(text="$" + str(money) + " \t\t           ")
    checkHand()
    stand()

def hit():
    global playerCards
    global roundCards
    global cards
    global cardNum
    global pOriginal
    global playerValue
    stringy = ""
    playerCards.append(roundCards[cardNum])
    doubleButton.pack_forget()
    cardNum += 1
    checkHand()

def stand():
    global playerCards
    global dealerCards
    global roundCards
    global cards
    global cardNum
    global dealerValue
    global money
    global betAmount
    global doubleDown

    playerValue = checkHand()
    dealerValue = dealerTurn()
    doubleButton.pack_forget()

    if playerValue > 21:
        playerLabel.config(text="Player Cards \n Bust \n" + str(playerValue))
    elif (dealerValue < playerValue and doubleDown) or (dealerValue > 21 and doubleDown):
        money += betAmount * 3
        playerLabel.config(text="Player Cards \n Player Win (Double) \n" + str(playerValue))
        moneyLabel.config(text="$" + str(money) + " \t\t           ")
    elif dealerValue > 21:
        playerLabel.config(text="Player Cards \n Dealer Bust \n" + str(playerValue))
        money += betAmount * 2
        moneyLabel.config(text="$" + str(money) + " \t\t           ")
    elif dealerValue > playerValue:
        playerLabel.config(text="Player Cards \n Dealer Win \n" + str(playerValue))
    elif dealerValue < playerValue:
        playerLabel.config(text="Player Cards \n Player Win \n" + str(playerValue))
        money += betAmount * 2
        moneyLabel.config(text="$" + str(money) + " \t\t           ")
    elif dealerValue == playerValue:
        money += betAmount
        playerLabel.config(text="Player Cards \n Push \n" + str(playerValue))
        moneyLabel.config(text="$" + str(money) + " \t\t           ")

    betButton.pack()
    hitButton.pack_forget()
    standButton.pack_forget()
    doubleDown = False

def dealerTurn():
    global dealerCards
    global cardNum
    global cards
    global dOriginal
    global dealerCards2
    global dealerValue
    stringy = ""
    dealerValue = 0
    dealerCards2 = [0] * len(dealerCards)

    for i in range(len(dealerCards)):
        dealerCards2[i] = dealerCards[i] % 13
    for i in range(len(dealerCards)):
        if dealerCards2[i] == 9 or dealerCards2[i] == 10 or dealerCards2[i] == 11 or dealerCards2[i] == 12:
            dealerValue += 10
        elif dealerCards2[i] == 0:
            if dealerValue + 11 <= 21:
                dealerValue += 11
            else:
                dealerValue += 1
        else:
            dealerValue += (int(dealerCards2[i])+1)

    while(dealerValue<16):
        dealerValue = dealerHit()

    for i in range(len(dealerCards)):
        stringy = stringy + str(cards[dealerCards[i]]) + "   "
    dealerCardsLabel.config(text=stringy + "\n\n")

    return dealerValue

def dealerHit():
    global cardNum
    global dealerCards2
    global dealerValue
    dealerValue = 0

    dealerCards.append(roundCards[cardNum])
    cardNum += 1

    dealerCards2 = [0] * len(dealerCards)

    for i in range(len(dealerCards)):
        dealerCards2[i] = dealerCards[i] % 13

    for i in range(len(dealerCards)):
        if dealerCards2[i] == 9 or dealerCards2[i] == 10 or dealerCards2[i] == 11 or dealerCards2[i] == 12:
            dealerValue += 10
        elif dealerCards2[i] == 0:
            if dealerValue + 11 <= 21:
                dealerValue += 11
            else:
                dealerValue += 1
        else:
            dealerValue += (int(dealerCards2[i])+1)

    if dealerValue > 21:
        if 0 in dealerCards2:
            dealerValue -= 10

    return dealerValue

def checkHand():
    global playerCards
    global roundCards
    global cards
    global cardNum
    global dealerCards
    global pOriginal
    playerCards2 = [0] * len(playerCards)

    dealerValue = 0
    playerValue = 0
    stringy = ""

    for i in range(len(playerCards)):
        playerCards2[i] = playerCards[i] % 13

    for i in range(len(playerCards)):
        if playerCards2[i] == 9 or playerCards2[i] == 10 or playerCards2[i] == 11 or playerCards2[i] == 12:
            playerValue += 10
        elif playerCards2[i] == 0:
            if playerValue + 11 <= 21:
                playerValue += 11
            else:
                playerValue += 1
        else:
            playerValue += (int(playerCards2[i])+1)

    for i in range(len(playerCards)):
        stringy = stringy + str(cards[playerCards[i]]) + "   "
    playerCardsLabel.config(text = stringy)

    if playerValue > 21:
        if 0 in playerCards2:
            playerValue -= 10
    if playerValue > 21:
        playerLabel.config(text = "Player Cards \n Bust \n" + str(playerValue))
        hitButton.pack_forget()
        standButton.pack_forget()
        betButton.pack()
        dealerCardsLabel.config(text=cards[dealerCards[0]] + "   " + cards[dealerCards[1]] + " \n\n")
    else:
        playerLabel.config(text="Player Cards \n\n" + str(playerValue))

    return playerValue


money = 100
doubleDown = False
mainFrame = Tk()
mainFrame.geometry("300x350")

dealerCards = []
playerCards = []
roundCards = []
cards = []
pOriginal = []
dOriginal = []
cardNum = 0
betAmount = 0

oneFrame = Frame(mainFrame)
oneFrame.pack()
twoFrame = Frame(mainFrame)
twoFrame.pack()
threeFrame = Frame(mainFrame)
threeFrame.pack()
fourFrame = Frame(mainFrame)
fourFrame.pack()
fiveFrame = Frame(mainFrame)
fiveFrame.pack()
sixFrame = Frame(mainFrame)
sixFrame.pack()

topLabel = Label(oneFrame,text = 'Welcome to Blackjack\n\n')
topLabel.pack()

dealerLabel = Label(twoFrame, text = 'Dealer Cards:')
dealerLabel.pack(side = TOP)

dealerCardsLabel = Label(twoFrame, text = 'XX   ??   \n\n')
dealerCardsLabel.pack(side = BOTTOM)

playerCardsLabel = Label(threeFrame, text = "XX   XX")
playerCardsLabel.pack(side = TOP)

playerLabel = Label(threeFrame, text = 'Player Cards    \n\n')
playerLabel.pack(side = BOTTOM)

hitButton = Button(fourFrame, text = 'Hit', command = hit)
#hitButton.pack(side = LEFT)

standButton = Button(fourFrame, text = 'Stand',command = stand)
#standButton.pack(side = RIGHT)

doubleButton = Button(fourFrame,text = 'Double', command = double)
#doubleButton.pack(side = RIGHT)

balanceLabel = Label(fiveFrame, text = "Balance: \t\t  ")
balanceLabel.pack(side = LEFT)


betAmountSpin = Spinbox(fiveFrame, from_ = 1, to = 100000) #Change to max
betAmountSpin.pack(side = RIGHT)

moneyLabel = Label(sixFrame,text = "$"+str(money)+ " \t\t           ")
moneyLabel.pack(side = LEFT)

betButton = Button(sixFrame,text = 'Bet', command = playHand)
betButton.pack()

mainFrame.mainloop()