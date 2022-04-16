import random

def gen_random():
    num=random.randrange(1,1000)
    return num

ran_num=gen_random()
print(f"The random number is {ran_num}")
