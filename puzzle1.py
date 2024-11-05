Fcounter = 0
Bcounter = 0
queue = []


x = int(input("Enter the number of people in the queue: "))


for i in range(x):
    people = str(input("Which way is their cap facing? ('F' for forward and 'B' for backward): "))
    if people == "F":
        Fcounter += 1
        queue.append(people)
    elif people == "B":
        Bcounter += 1
        queue.append(people)
    else:
        print("Wear a cap and come back!")


if Fcounter > Bcounter:
    for i in range(len(queue)):
        if queue[i] == "B":
            print("Person in position", i, "please flip your cap forwards")

if Fcounter < Bcounter:
    for i in range(len(queue)):
        if queue[i] == "F":
            print("Person in position", i, "please flip your cap backwards") 
print(queue)
