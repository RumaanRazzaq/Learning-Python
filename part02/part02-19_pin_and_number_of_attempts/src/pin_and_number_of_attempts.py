# Write your solution here
attempts = 0
while True:
    pin = int(input("PIN: "))
    attempts += 1
    if pin == 4321:
        if(attempts > 1):
            print(f"Correct! It took you {attempts} attempts")
        else:
            print("Correct! It only took you one single attempt!")
        break
    else:
        print("Wrong")