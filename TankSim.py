import random
import fileinput

print("Kitru's Tank Simulator v. 1.0");

iterations = int(input("How many iterations:"))
duration = int(input("How many GCDs duration for each:"))

global tankDef
global tankRes
global tankShield
global tankAbs
global tankKEDR
global tankIEDR

inputArray = []

booleanParse = 0
while booleanParse == 0:
        booleanParse = input("Import Tank Stats? (Y/N)")
        if booleanParse in ['yes', '1', 'y', 'Yes', 'Y']:
                inputType = True
        elif booleanParse in ['no','No','N','n','0']:
                inputType = False
        else:
                print("Improper Input.")        
booleanParse = 0

if inputType == False:
        tankMaxHp  = int(input("Tank's Max HP:"))
        tankDef = float(input("Tank's Defense chance in decimal form:"))
        tankRes = float(input("Tank's Resist chance in decimal form:"))
        tankShield = float(input("Tank's Shield chance in decimal form:"))
        tankAbs = float(input("Tank's Absorb value in decimal form:"))
        tankKEDR = float(input("Tank's K/E damage reduction in decimal form:"))
        tankIEDR = float(input("Tank's I/E damage reduction in decimal form:"))
        tankSelfHeal = float(input("Tank's average self healing per GCD, if any:"))
        tankAbsShield = float(input("Tank's average damage absorb shield per GCD, if any:"))
else:
        inputFileName = input("Name of Tank Stat File: ")
        for line in fileinput.input(inputFileName):
                inputArray.append(line.rstrip())
        tankMaxHp  = int(inputArray.pop(0))
        tankDef = float(inputArray.pop(0))
        tankRes = float(inputArray.pop(0))
        tankShield = float(inputArray.pop(0))
        tankAbs = float(inputArray.pop(0))
        tankKEDR = float(inputArray.pop(0))
        tankIEDR = float(inputArray.pop(0))
        tankSelfHeal = int(inputArray.pop(0))
        tankAbsShield = int(inputArray.pop(0))

booleanParse = 0
while booleanParse == 0:
        booleanParse = input("Import Attacker Info? (Y/N)")
        if booleanParse in ['yes', '1', 'y', 'Yes', 'Y']:
                inputType = True
        elif booleanParse in ['no','No','N','n','0']:
                inputType = False
        else:
                print("Improper Input.")
booleanParse = 0

if inputType == False:
        basicHit = int(input("Attacker's basic attack damage:"))
        booleanParse = input("Is the basic attack melee/ranged, T/F:")
        if booleanParse in ['true', '1', 't', 'True', 'T']:
                basicHitMR = True
        else:
                basicHitMR = False
        booleanParse = input("Is the basic attack kinetic/energy, T/F:")
        if booleanParse in ['true', '1', 't', 'True', 'T']:
                basicHitKE = True
        else:
                basicHitKE = False
        bigHit = int(input("Attacker's big attack damage:"))
        bigHitInterval = int(input("How many GCDs pass between big attack uses:"))
        booleanParse = input("Is the big attack melee/ranged, T/F:")
        if booleanParse in ['true', '1', 't', 'True', 'T']:
                bigHitMR = True
        else:
                bigHitMR = False
        booleanParse = input("Is the big attack kinetic/energy, T/F:")
        if booleanParse in ['true', '1', 't', 'True', 'T']:
                bigHitKE = True
        else:
                bigHitKE = False
else:
        inputFileName = input("Name of Enemy Info File: ")
        for line in fileinput.input(inputFileName):
                inputArray.append(line.rstrip())
        basicHit  = int(inputArray.pop(0))
        booleanParse = inputArray.pop(0)
        if booleanParse in ['true', '1', 't', 'True', 'T']:
                basicHitMR = True
        else:
                basicHitMR = False
        booleanParse = inputArray.pop(0)
        if booleanParse in ['true', '1', 't', 'True', 'T']:
                basicHitKE = True
        else:
                basicHitKE = False
        bigHit = int(inputArray.pop(0))
        bigHitInterval = int(inputArray.pop(0))
        booleanParse = inputArray.pop(0)
        if booleanParse in ['true', '1', 't', 'True', 'T']:
                bigHitMR = True
        else:
                bigHitMR = False
        booleanParse = inputArray.pop(0)
        if booleanParse in ['true', '1', 't', 'True', 'T']:
                bigHitKE = True
        else:
                bigHitKE = False
                
booleanParse = 0
while booleanParse == 0:
        booleanParse = input("Import Healer Info? (Y/N)")
        if booleanParse in ['yes', '1', 'y', 'Yes', 'Y']:
                inputType = True
        elif booleanParse in ['no','No','N','n','0']:
                inputType = False
        else:
                print("Improper Input.")
booleanParse = 0
        
if inputType == False:
        basicHeal = int(input("Healers' average heal amount, per GCD:"))
        bigHeal = int(input("Healers' big heal amount, per use:"))
        bigHealInterval = int(input("How often can the big heal be used, in GCDs:"))
        booleanParse = input("Is allowable overhealing quantity determined by value(T) or percent(F):")
        if booleanParse in ['true', '1', 't', 'True', 'T']:
        	overHealType = True
        else: overHealType = False
        overHealAllowValue = 0
        overHealAllowPercentage = 0
        if overHealType == True:
        	overHealAllowValue  = int(input("How much overhealing is permissable per cast, in hp:"))
        else:
        	overHealAllowPercent = float(input("How much overhealing is permissable per cast, in percent of total heal:"))
else:
        inputFileName = input("Name of Healer Info File: ")
        for line in fileinput.input(inputFileName):
                inputArray.append(line.rstrip())
        basicHeal  = int(inputArray.pop(0))
        bigHeal = int(inputArray.pop(0))
        bigHealInterval = int(inputArray.pop(0))
        overHealType = inputArray.pop(0)
        overHealAllowValue = 0
        overHealAllowPercentage = 0
        if overHealType == True:
                overHealAllowValue = int(inputArray.pop(0))
        else:
                overHealAllowPercent = float(inputArray.pop(0))

time = 0
dead = False
tankHp = tankMaxHp
lowestHp = tankMaxHp
hitAction = 0
healAction = 0
nextHealAction = 0
bigHealAvail = 0
numDeaths = 0
lowestArray = []
lowestLowHp = tankHp
averageLowest = 0

def attack(damage, attackType, damageType):
        "Determines the damage of an delivered attack"
        if attackType == True:
                if random.random() <= tankDef:
                        #print("Defend, 0 damage")
                        return 0
                if damageType == True:
                        if random.random() <= tankShield:
                                #print("M/R K/E Shield, " + repr(damage * (1 - tankAbs) * (1 - tankKEDR)) + " damage")
                                return damage * (1 - tankAbs) * (1 - tankKEDR)
                        else:
                                #print("M/R K/E Hit, " + repr(damage * (1 - tankKEDR)) + " damage")
                                return damage * (1 - tankKEDR)
                else:
                        if random.random() <= tankShield:
                                #print("M/R I/E Shield, " + repr(damage * (1 - tankAbs) * (1 - tankKEDR)) + " damage")
                                return damage * (1 - tankAbs) * (1 - tankIEDR)
                        else:
                                #print("M/R I/E Hit, " + repr(damage * (1 - tankIEDR)) + " damage")
                                return damage * (1 - tankIEDR)
        else:
                if random.random() < tankRes:
                        #print("Resist, 0 damage")
                        return 0
                if damageType == True:
                        if random.random() <= tankShield:
                                #print("F/T K/E Shield, " + repr(damage * (1 - tankAbs) * (1 - tankKEDR)) + " damage")
                                return damage * (1 - tankAbs) * (1 - tankKEDR)
                        else:
                                #print("F/T K/E Hit, " + repr(damage * (1 - tankKEDR)) + " damage")
                                return damage * (1 - tankKEDR)
                else:
                        #print("F/T I/E Hit, " + repr(damage * (1 - tankIEDR)) + " damage")
                        return damage * (1 - tankIEDR)

for i in range (0, iterations):
        time = 0
        dead = False
        tankHp = tankMaxHp
        lowestHp = tankMaxHp
        hitAction = 0
        healAction = 0
        nextHealAction = 0
        bigHealAvail = 0
        while time < duration and dead == False:
                if time % bigHitInterval == 0 and time != 0:
                        hitAction = 1
                else:
                        hitAction = 0
                if nextHealAction == 2:
                        healAction = 2
                elif nextHealAction == 1:
                        healAction = 1
                else:
                        healAction = 0

                if hitAction == 1:
                        tankHp = tankHp - (attack(bigHit, bigHitMR, bigHitKE) - tankAbsShield)
                        #print("Tank Hp " + repr(tankHp))
                elif hitAction == 0:
                        tankHp = tankHp - (attack(basicHit, basicHitMR, basicHitKE) - tankAbsShield)
                        #print("Tank Hp " + repr(tankHp))
                if tankHp < lowestHp:
                        if tankHp <= 0:
                                dead = True
                        else:
                                lowestHp = tankHp

                tankHp += tankSelfHeal
                if(tankHp > tankMaxHp):
                        tankHp = tankMaxHp

                if healAction == 2:
                        tankHp += bigHeal
                        bigHealAvail = time + bigHealInterval
                        if tankHp > tankMaxHp:
                                tankHp = tankMaxHp
                        #print("Big Heal " + repr(bigHeal))
                        #print("Tank Hp " + repr(tankHp))
                elif healAction == 1:
                        tankHp += basicHeal
                        if tankHp > tankMaxHp:
                                tankHp = tankMaxHp
                        #print("Basic Heal " + repr(basicHeal))
                        #print("Tank Hp " + repr(tankHp))
                #elif healAction == 0:
                        #print("No Heal ")
                        #print("Tank Hp " + repr(tankHp))

                if overHealAllowValue != 0:
                        if tankHp <= (tankMaxHp - (bigHeal - overHealAllowValue)) and time >= bigHealAvail:
                                nextHealAction = 2
                        elif tankHp <= (tankMaxHp - (basicHeal - overHealAllowValue)):
                                nextHealAction = 1
                        else:
                                nextHealAction = 0
                else:
                        if tankHp <= (tankMaxHp - (bigHeal * overHealAllowPercent)) and time >= bigHealAvail:
                                nextHealAction = 2
                        elif tankHp <= (tankMaxHp - (basicHeal * overHealAllowPercent)):
                                nextHealAction = 1
                        else:
                                nextHealAction = 0
                time = time + 1
        if time != duration and dead == True:
                numDeaths = numDeaths + 1
        elif lowestHp < lowestLowHp:
                lowestLowHp = lowestHp
                lowestArray.append(lowestHp)

for i in range (0, len(lowestArray)):
        averageLowest += lowestArray[i]
if len(lowestArray) != 0:
        averageLowest = averageLowest / len(lowestArray)
else:
        lowestLowHp = "dead"
        averageLowest = 0

print("Number of deaths:" + repr(numDeaths))
print("Lowest low hp: " + repr(lowestLowHp))
print("Average lowest hp (ignoring deaths): " + repr(averageLowest))


