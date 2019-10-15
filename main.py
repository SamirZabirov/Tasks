from random import randint
cat = 1
dog = 1
dogs =[]

while cat <=5: 
  cat += 1 
  text2 = randint(1,6) 
  line = int(input('вводите число, от одного до 5:')) 
  perem = abs (line - text2)
 
  if perem == 0: 
    dog = 6 
    dogs.append(cat) 
  elif perem == 1: 
    dog = 5 
    dogs.append(cat) 
  elif perem == 2: 
    point = 4 
    dogs.append(cat) 
  elif perem == 3: 
    dog = 3 
    dogs.append(cat) 
  elif perem == 4: 
    dog = 2 
    dogs.append(cat) 
  elif perem == 2: 
    dog = 4 
    dogs.append(cat)
  elif perem == 5: 
    dog = 1 
    dogs.append(cat) 
  print("кол-ов очков: ",cat ) 
  every = sum(dogs) 

print ("общее кол - во очков",every)
if every< 25: 
  print("вы проиграли")
else: 
  print ("вы выйграли")