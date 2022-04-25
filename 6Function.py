def temper(temp):
    Htemper=float(32+temp*1.8)
    return Htemper
def main():
    global q
    q=input("Type 'p' to exit:   ")
    while(q!="p"):
        Ctemper=float(input("Please input Celsius temperature:   "))
        print(f"The  Fahrenheit temperature is: {temper(Ctemper)}")