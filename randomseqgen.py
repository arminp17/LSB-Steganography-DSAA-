import random

def unique(sequence):
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]

def set_seed(password):
    seed = 0
    for char in password:
        seed+=ord(char)
    random.seed(seed)

def gen_rand_sequence(message_length,rows,cols,channels):
    randlist=[]
    for i in range(message_length):
        randlist.append((random.randint(0,rows-1),random.randint(0,cols-1),random.randint(0,channels-1)))
    return unique(randlist)
