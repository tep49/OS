import os
import threading
import itertools
import random

#Global Variables
winner = True           #Winner flag

def dealer(cards, log, i):
    random.shuffle(cards)
    currentPlayer = i + 1

    for j in range(3):
        out = ("Player " + str(currentPlayer) + " gets " + str(cards[j][0]) + " of " + str(cards[j][1]) + " from the dealer\n")
        currentPlayer += 1
        if currentPlayer > 3:
            currentPlayer = 1
        log.write(out)


def player1(cards, log, roundNum,hand):

    if roundNum == 0:
        hand.append(cards.pop(0))
    else:
        hand.append(cards.pop(0))

        log.write("Player 1 draws: ")
        log.write(str(hand[1]))

        log.write("\nPlayer 1 Hand: ")
        for x in hand:
            out = str(x) + ' '
            log.write(out)
        log.write("\n")

        x = hand[0]
        y = hand[1]
        if (x[0] == y[0]):
            log.write("\n\nPlayer 1 wins and exits\n\n")
            global winner                                      #Grabs global winner flag
            winner = False                                      #Sets flag
            cards.append(hand[0])
            cards.append(hand[1])
            hand.pop()
            hand.pop()
        else:
            z = random.randrange(0,1)
            cards.append(hand[z])
            hand.pop(z)
            log.write("Player 1 discards: ")
            log.write(str(hand[z]))
            log.write("\n\n")



def player2(cards, log, roundNum, hand):

    if roundNum == 0:
        hand.append(cards.pop(0))
    else:
        hand.append(cards.pop(0))

        log.write("Player 2 draws: ")
        log.write(str(hand[1]))

        log.write("\nPlayer 2 Hand: ")
        for x in hand:
            out = str(x) + ' '
            log.write(out)
        log.write("\n")

        x = hand[0]
        y = hand[1]
        if (x[0] == y[0]):
            log.write("\n\nPlayer 2 wins and exits\n\n")
            global winner                                       #Grabs global winner flag
            winner = False                                      #Sets flag
            cards.append(hand[0])
            cards.append(hand[1])
            hand.pop()
            hand.pop()
        else:
            z = random.randrange(0,1)
            cards.append(hand[z])
            hand.pop(z)

            log.write("Player 2 discards: ")
            log.write(str(hand[z]))
            log.write("\n\n")


def player3(cards, log, roundNum, hand):

    if roundNum == 0:
        hand.append(cards.pop(0))
    else:
        hand.append(cards.pop(0))

        log.write("Player 3 draws: ")
        log.write(str(hand[1]))

        log.write("\nPlayer 3 Hand: ")
        for x in hand:
            out = str(x) + ' '
            log.write(out)
        log.write("\n")

        x = hand[0]
        y = hand[1]
        if (x[0] == y[0]):
            log.write("\n\nPlayer 3 wins and exits\n\n")
            global winner                                       #Grabs global winner flag
            winner = False                                      #Sets flag
            cards.append(hand[0])
            cards.append(hand[1])
            hand.pop()
            hand.pop()

        else:
            z = random.randrange(0,1)
            cards.append(hand[z])
            hand.pop(z)

            log.write("Player 3 discards: ")
            log.write(str(hand[z]))
            log.write("\n\n")

if __name__ == '__main__':

    seed = raw_input("Enter seed: ");
    random.seed(a=seed)

    cards = list(itertools.product(range(1, 14), ['Spade', 'Club', 'Heart', 'Diamond']))

    log = open("Logs.txt", "w")

    p1Hand = []
    p2Hand = []
    p3Hand = []

    for i in range(3):

        dealerThread = threading.Thread(group=None, target=dealer, name='dealer', args=(cards,log,i,))
        dealerThread.start()

        while dealerThread.isAlive():   #Waits to give dealer thread time before starting game
            print("Awaiting Dealer Thread")

        roundNum = 0
        win = 0
#       Currently have it set to loop a few times just to check output, will change to while win == 0 to loop until a thread wins
        while win == 0:
#           Should probably make this part better VVVVVVVV
            if i == 0:
                if winner:  #Checks if flag set, if not player plays
                    p1Thread = threading.Thread(group=None, target=player1, name='player1', args=(cards,log,roundNum,p1Hand,))
                    p1Thread.start()
                if winner:  #Checks if flag set, if not player plays
                    p2Thread = threading.Thread(group=None, target=player2, name='player2', args=(cards,log,roundNum,p2Hand,))
                    p2Thread.start()
                if winner:  #Checks if flag set, if not player plays
                    p3Thread = threading.Thread(group=None, target=player3, name='player3', args=(cards,log,roundNum,p3Hand,))
                    p3Thread.start()
                    win = 0

            if i == 1:
                if winner:  # Checks if flag set, if not player plays
                    p2Thread = threading.Thread(group=None, target=player2, name='player2',
                                                args=(cards, log, roundNum, p2Hand,))
                    p2Thread.start()
                if winner:  # Checks if flag set, if not player plays
                    p3Thread = threading.Thread(group=None, target=player3, name='player3',
                                                    args=(cards, log, roundNum, p3Hand,))
                    p3Thread.start()
                if winner:  # Checks if flag set, if not player plays
                    p1Thread = threading.Thread(group=None, target=player1, name='player1',
                                                    args=(cards, log, roundNum, p1Hand,))
                    p1Thread.start()
                if not winner:
                    win = 0

            if i == 2:
                if winner:  # Checks if flag set, if not player plays
                    p3Thread = threading.Thread(group=None, target=player3, name='player3',
                                                 args=(cards, log, roundNum, p3Hand,))
                    p3Thread.start()
                if winner:  # Checks if flag set, if not player plays
                    p1Thread = threading.Thread(group=None, target=player1, name='player1',
                                                 args=(cards, log, roundNum, p1Hand,))
                    p1Thread.start()
                if winner:  # Checks if flag set, if not player plays
                    p2Thread = threading.Thread(group=None, target=player2, name='player2',
                                                 args=(cards, log, roundNum, p2Hand,))
                    p2Thread.start()
                if not winner:
                    win = 0

            roundNum += 1

            while p1Thread.isAlive() or p2Thread.isAlive() or p3Thread.isAlive():   #Checks if any player threads running
                print("Awaiting Player Threads")                                    #if threads are running it waits before
                                                                                    #queueing more overlapping work
            log.write("\n\nCURRENT DECK: \n")
            for z in cards:
                log.write(str(z))
            log.write("\n\n")
            if winner == False:
                while p1Hand:
                    x = p1Hand.pop()
                    cards.append(x)
                while p2Hand:
                    x = p2Hand.pop();
                    cards.append(x)
                while p3Hand:
                    x = p3Hand.pop();
                    cards.append(x)
                win = 1
                winner = True