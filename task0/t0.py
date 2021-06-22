import random 

mas=[random.randint(-100,100) for x in range(30)]
print(mas)

nomer = mas[0]
pos = 0

for x in range(1, len(mas)):
 if mas[x] > nomer:
  nomer = mas[x]
  pos = x + 1
print("Max element:", nomer, "Sequence number:", pos)

print("Pairs of negative numbers standing side by side:")
for x in range(x):
  if mas[x] < 0 and mas[x + 1] < 0:
    print(mas[x], mas[x + 1])
  
