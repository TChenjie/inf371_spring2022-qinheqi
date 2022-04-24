thisdic={
    "strength":12,
    "dexterity":12,
    "constitution":14,
    "intelligence":15,
    "wisdom":20,
    "charisma":15
}
print(thisdic)
b=0
for a in thisdic.keys():
    if a=="strength":
        b+=1
if b!=0:
    print (thisdic["strength"])
else:
    print("strength isn't a character stat")
