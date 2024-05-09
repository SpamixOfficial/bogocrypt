import random, time

print("Russian roulette!!")
time.sleep(1)
print("You will....")
time.sleep(1)
yorn = random.choice([True, False]) #Choose randomly between True or False, 50-50 chance that you survive >:) (killem all)
if yorn:
    print("DIE!!!!!")
else:
    print("survive this time >:(")
