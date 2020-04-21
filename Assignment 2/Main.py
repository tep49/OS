import os
import itertools
import random


def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst


def fifo(page, frameSize):
    pageFaults = 0
    frames = []
    # Initialize all frames to null
    for i in range(frameSize):
        frames.append("NULL")
    for x in range(100):
        flag = 0
        for y in range(frameSize):
            # Check if there is an empty frame
            if frames[y] == "NULL":
                frames[y] = page[x]
                pageFaults += 1
                flag = 1
                break
            # Check if page value already exists in frames
            if frames[y] == page[x]:
                flag = 1
                break
        if flag == 1:
            continue
            # Pop oldest page in queue and append new page
        else:
            frames.pop(0)
            frames.append(page[x])
            pageFaults += 1
    print "FIFO Page Faults: "
    print pageFaults
    return pageFaults


def lru(page, frameSize):
    pageFaults = 0
    frames = []
    # Initialize all frames to null
    for i in range(frameSize):
        frames.append("NULL")

    for x in range(100):
        flag = 0
        for y in range(frameSize):
            # Check if there is an empty frame
            if frames[y] == "NULL":
                frames[y] = page[x]
                pageFaults += 1
                flag = 1
                break
            # Check if page value already exists in frames
            if frames[y] == page[x]:
                flag = 1
                break
        if flag == 1:
            continue
            # Find the least recently used page
        else:
            prevDist = 0
            oldest = 0
            for y in frames:
                dist = 0
                pos = 100 - x
                rev = Reverse(page)

                for z in range(pos,100):
                    if rev[z] == y:
                        if dist >= prevDist:
                            prevDist = dist
                            oldest = frames.index(y)
                        break
                    else:
                        dist += 1
            frames[oldest] = page[x]
            pageFaults += 1
    print "LRU Page Faults: "
    print pageFaults
    return pageFaults


def opt(page, frameSize):
    pageFaults = 0
    frames = []
    # Initialize all frames to null
    for i in range(frameSize):
        frames.append("NULL")

    for x in range(100):
        flag = 0
        for y in range(frameSize):
            # Check if there is an empty frame
            if frames[y] == "NULL":
                frames[y] = page[x]
                pageFaults += 1
                flag = 1
                break
            # Check if page value already exists in frames
            if frames[y] == page[x]:
                flag = 1
                break
        if flag == 1:
            continue
            # Find the page which won't be used for the longest time
        else:
            prevDist = 0
            oldest = 0
            for y in frames:
                dist = 0

                for z in range(x, 100):
                    if page[z] == y:
                        if dist >= prevDist:
                            prevDist = dist
                            furthest = frames.index(y)
                        break
                    else:
                        dist += 1
            frames[furthest] = page[x]
            pageFaults += 1
    print "OPT Page Faults: "
    print pageFaults
    return pageFaults


if __name__ == '__main__':

    page = []

    fifoLog = open("fifo.txt", "w")
    lruLog = open("lru.txt", "w")
    optLog = open("opt.txt", "w")

    # Generate page values
    for i in range(100):
        page.append(random.randint(0,49))

    sel = input("Enter Frame Size or 0 for all frame sizes 1-30: ")

    if sel == 0:
        # Run each algorithm 30 times, i = frame size
        for i in range(1,31):
            faults = fifo(page, i)
            fifoLog.write(str(faults) + "\n")
            faults = lru(page, i)
            lruLog.write(str(faults) + "\n")
            faults = opt(page, i)
            optLog.write(str(faults) + "\n")
    else:
        faults = fifo(page, int(sel))
        faults = lru(page, int(sel))
        faults = opt(page, int(sel))

