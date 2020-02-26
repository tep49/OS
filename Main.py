import os
import threading
import itertools
import random


def dealer(cards, log, i):
    random.shuffle(cards)
    currentPlayer = i + 1

    for j in range(3):
        out = ("Player " + str(currentPlayer) + " gets " + str(cards[j][0]) + " of " + str(cards[j][1]) + " from the dealer\n")
        currentPlayer += 1;
        if currentPlayer > 3:
            currentPlayer = 1;
        log.write(out)


def player1(cards, log, roundNum,hand):

    if roundNum == 0:
        hand.append(cards.pop(0))
    else:
        hand.append(cards.pop(0))

        log.write("Player 1 Hand: ")
        for x in hand:
            out = str(x) + ' '
            log.write(out)
        log.write("\n")

        x = hand[0]
        y = hand[1]
        if (x[0] == y[0]):
            print "win!"
        else:
            z = random.randrange(0,1)
            cards.append(hand[z])
            hand.pop(z)


def player2(cards, log, roundNum, hand):

    if roundNum == 0:
        hand.append(cards.pop(0))
    else:
        hand.append(cards.pop(0))

        log.write("Player 2 Hand: ")
        for x in hand:
            out = str(x) + ' '
            log.write(out)
        log.write("\n")

        x = hand[0]
        y = hand[1]
        if (x[0] == y[0]):
            print "win!"
        else:
            z = random.randrange(0,1)
            cards.append(hand[z])
            hand.pop(z)


def player3(cards, log, roundNum, hand):

    if roundNum == 0:
        hand.append(cards.pop(0))
    else:
        hand.append(cards.pop(0))

        log.write("Player 3 Hand: ")
        for x in hand:
            out = str(x) + ' '
            log.write(out)
        log.write("\n")

        x = hand[0]
        y = hand[1]
        if (x[0] == y[0]):
            print "win!"
        else:
            z = random.randrange(0,1)
            cards.append(hand[z])
            hand.pop(z)


if __name__ == '__main__':

    cards = list(itertools.product(range(1, 14), ['Spade', 'Club', 'Heart', 'Diamond']))

    log = open("Logs.txt", "w")

    win = 5

    p1Hand = []
    p2Hand = []
    p3Hand = []

    for i in range(3):
        dealerThread = threading.Thread(group=None, target=dealer, name='dealer', args=(cards,log,i,), kwargs={})
        dealerThread.start()
        roundNum = 0
        while win >= 0:
#           Should probably make this part better VVVVVVVV
            if i == 0:
                p1Thread = threading.Thread(group=None, target=player1, name='player1', args=(cards,log,roundNum,p1Hand,), kwargs={})
                p1Thread.start()
                p2Thread = threading.Thread(group=None, target=player2, name='player2', args=(cards,log,roundNum,p2Hand,), kwargs={})
                p2Thread.start()
                p3Thread = threading.Thread(group=None, target=player3, name='player3', args=(cards,log,roundNum,p3Hand,), kwargs={})
                p3Thread.start()
            if i == 1:
                p2Thread = threading.Thread(group=None, target=None, name='player2', args=(), kwargs={})
                p2Thread.start()
                p3Thread = threading.Thread(group=None, target=None, name='player3', args=(), kwargs={})
                p3Thread.start()
                p1Thread = threading.Thread(group=None, target=player1, name='player1', args=(cards,log,i,), kwargs={})
                p1Thread.start()
            if i == 2:
                p3Thread = threading.Thread(group=None, target=None, name='player3', args=(), kwargs={})
                p3Thread.start()
                p1Thread = threading.Thread(group=None, target=player1, name='player1', args=(cards,log,i,), kwargs={})
                p1Thread.start()
                p2Thread = threading.Thread(group=None, target=None, name='player2', args=(), kwargs={})
                p2Thread.start()
            roundNum += 1
            win -= 1
