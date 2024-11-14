# Input: [(6,7), (7,9), (10,11) ,(10,12), (8,10), (9,11), (6,8)]
    

x = int(input("Enter the number of celebrities attending the party: "))
comengo = []

for i in range(x):
    celebinput = int(input("Please enter when the celebrity will come: "))
    celebleave = int(input("And when will they leave? "))
    comengo.append((celebinput, celebleave))


minhour = min(start for start, _ in comengo)
max_hour = max(end for _, end in comengo)


besthour = minhour
maxcelebs = 0

for hour in range(minhour, max_hour):
    count = sum(1 for start, end in comengo if start <= hour < end)
    if count > maxcelebs:
        maxcelebs = count
        besthour = hour


print(f"The best time to attend is hour {besthour}, where you'll meet {maxcelebs} celebrities.")