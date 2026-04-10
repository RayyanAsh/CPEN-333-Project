# Group #: B51
# Student Names: Rayyan Ashar, Sasha Jatskevich
 
import threading
import queue
import time, random

def consumerWorker (queue, consumerID):
    """target worker for a consumer thread""" 
    tems = 0
    wholeItems = int(items*producerNumber/consumerNumber)
    remainder = items*producerNumber - wholeItems*consumerNumber
    while tems < wholeItems + int((remainder+consumerID-1)/consumerNumber): #assigns extra capacity to consumer threads if needed 
        time.sleep(round(random.uniform(randMin, randMax), 2)) #a random delay (range set in __main__)
        nextConsumed = queue.get()
        print(f"C{consumerID} Consuming: ", nextConsumed)
        tems+=1
    print(f"Consumer {consumerID} is full, #yummers")

def producerWorker(queue, producerID):
    """target worker for a producer thread"""
    tems = 0
    while tems < items:
        time.sleep(round(random.uniform(randMin, randMax), 2)) #a random delay (range set in __main__)
        potentialItems = ["Peashooter", "Sunflower", "Cherry Bomb", "Wall-nut", "Potato Mine", "Snow Pea", "Chomper", "Repeater", "Puff-shroom", "Sun-shroom", "Fume-shroom", "Grave Buster", "Hypno-shroom", "Scaredy-shroom", "Ice-shroom", "Doom-shroom", "Lily Pad", "Squash", "Threepeater", "Tangle Kelp", "Jalapeno", "Spikeweed", "Torchwood", "Tall-nut", "Sea-shroom", "Plantern", "Cactus", "Blover", "Split Pea", "Starfruit", "Pumpkin", "Magnet-shroom", "Cabbage-pult", "Flower Pot", "Kernel-pult", "Coffee Bean", "Garlic", "Umbrella Leaf", "Marigold", "Melon-pult", "Gatling Pea", "Twin Sunflower", "Gloom-shroom", "Cattail", "Winter Melon", "Gold Magnet", "Spikerock", "Cob Cannon", "Imitator"]
        nextProduced = random.choice(potentialItems) # producer outputs, replace .choice(potentialItems) with .randint(0,9) if you prefer a simpler test case
        queue.put(nextProduced)
        print(f"P{producerID} Producing: ", nextProduced)
        tems +=1
    print(f"Producer {producerID} is empty")

if __name__ == "__main__":
    buffer = queue.Queue()
    thread = [] # initialize thread list
    
    #producer/consumer parameters
    items = 5 #items per producer
    producerNumber = 4
    consumerNumber = 5
    randMin = .1 #delay window in seconds
    randMax = .3

    #spin up required number of producer threads
    for _ in range(1,producerNumber+1):
      t1 = threading.Thread(target = producerWorker, args = (buffer, _,))
      t1.start()
      thread.append(t1)

    #spin up required number of consumer threads
    for _ in range(1,consumerNumber+1):
      t2 = threading.Thread(target = consumerWorker, args = (buffer, _,))
      t2.start()
      thread.append(t2)

    #merge threads
    for t in thread:
        t.join() 

    print("Test complete, all produced items consumed")    