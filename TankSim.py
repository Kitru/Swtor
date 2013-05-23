import random

print("Kitru's Tank Simulator v. 1.0");

iterations = int(input("How many iterations:"))
duration = int(input("How many GCDs duration for each:"))
tankMaxHp  = int(input("Tank's Max HP:"))
global tankDef 
tankDef = float(input("Tank's Defense chance in decimal form:"))
global tankRes
tankRes = float(input("Tank's Resist chance in decimal form:"))
global tankShield
tankShield = float(input("Tank's Shield chance in decimal form:"))
global tankAbs
tankAbs = float(input("Tank's Absorb value in decimal form:"))
global tankKEDR
tankKEDR = float(input("Tank's K/E damage reduction in decimal form:"))
global tankIEDR
tankIEDR = float(input("Tank's I/E damage reduction in decimal form:"))
tankSelfHeal = float(input("Tank's average self healing per GCD, if any:"))
tankAbsShield = float(input("Tank's average damage absorb shield per GCD, if any:"))

basicHit = int(input("Attacker's basic attack damage:"))
booleanParse = bool(input("Is the basic attack melee/ranged, T/F:"))
basicHitMR = False
if booleanParse in ['true', '1', 't', 'True', 'T']:
        basicHitMR = True
basicHitKE = False
booleanParse = bool(input("Is the basic attack kinetic/energy, T/F:"))
if booleanParse in ['true', '1', 't', 'True', 'T']:
        basicHitKE = True
        
bigHit = int(input("Attacker's big attack damage:"))
bigHitInterval = int(input("How many GCDs pass between big attack uses:"))
bigHitMR = False
booleanParse = bool(input("Is the big attack melee/ranged, T/F:"))
if booleanParse in ['true', '1', 't', 'True', 'T']:
        bigHitMR = True
bigHitKE = False
booleanParse = bool(input("Is the big attack kinetic/energy, T/F:"))
if booleanParse in ['true', '1', 't', 'True', 'T']:
        bigHitKE = True

basicHeal = int(input("Healers' average heal amount, per GCD:"))
bigHeal = int(input("Healers' big heal amount, per use:"))
bigHealInterval = int(input("How often can the big heal be used, in GCDs:"))
booleanParse = bool(input("Is allowable overhealing quantity determined by value(T) or percent(F):"))
if booleanParse in ['true', '1', 't', 'True', 'T']:
  overHealType = True
else: overHealType = False
overHealAllowValue = 0
overHealAllowPercentage = 0
if overHealType == True:
	overHealAllowValue  = int(input("How much overhealing is permissable per cast, in hp:"))
else:
	overHealAllowPercent = float(input("How much overhealing is permissable per cast, in percent of total heal:"))


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

def attack(damage, attackType, damageType):
	"Determines the damage of an delivered attack"
	if attackType == True:
		if random.random() < tankDef:
			return 0;
		if damageType == True:
			if random.random() < tankShield:
				return damage * (1 - tankAbs) * (1 - tankKEDR)
			else:
				return damage * (1 - tankKEDR)
	else:
		if random.random() < tankRes:
			return 0
		else:
			return damage * (1 - tankIEDR)

for i in range (0, iterations):
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
                elif hitAction == 0:
                        tankHp = tankHp - (attack(basicHit, basicHitMR, basicHitKE) - tankAbsShield)
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
                elif healAction == 1:
                        tankHp += basicHeal
                        if tankHp > tankMaxHp:
                                tankHp = tankMaxHp		

                if overHealAllowValue != 0:
                        if tankHp < (tankMaxHp - (bigHeal - overHealAllowValue)) and time > bigHealInterval:
                                nextHealAction = 2
                        elif tankHp < (tankMaxHp - (basicHeal - overHealAllowValue)):
                                nextHealAction = 1
                        else:
                                nextHealAction = 0
                else:
                        if tankHp < (tankMaxHp - (bigHeal * overHealAllowPercent)) and time > bigHealInterval:
                                nextHealAction = 2
                        elif tankHp < (tankMaxHp - (basicHeal * overHealAllowPercent)):
                                nextHealAction = 1
                        else:
                                nextHealAction = 0
                time = time + 1
        if time != duration and dead == True:
                numDeaths = numDeaths + 1
        elif lowestHp < lowestLowHp:
                lowestLowHp = lowestHp
                lowestArray.append(lowestHp)
        time = 0
        lowestHp = tankMaxHp

averageLowest = 0
for i in range (0, len(lowestArray)):
        averageLowest += lowestArray[i]
if len(lowestArray) != 0:
        averageLowest = averageLowest / len(lowestArray)
        lowestLowHp = 0
else:
        averageLowest = 0

print("Number of deaths:" + repr(numDeaths))
print("Lowest low hp: " + repr(lowestLowHp))
print("Average lowest hp (ignoring deaths): " + repr(averageLowest))
