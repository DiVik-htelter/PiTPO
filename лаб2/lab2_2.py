# число блоков
# число имен в блоке
# текущая последовательность имен
# желаемая последовательность имен
#
# пример входных данных:
#1   кол-во блоков
#3   кол-во имен
#Yertle
#Duke of Earl
#Sir Lancelot
#Duke of Earl
#Yertle
#Sir Lancelot

import random

mass = []
corrMass = []
# Input data
def InputData(mass:list, corrMass:list):
  q = int(input("Введите кол-во блоков: ")) # кол-во блоков
  for i in range(q):
    n = int(input("Введите кол-во имен: ")) # кол-во нужных имен в блоке(а сам блок в 2 раза больше)
    temp = list()
    sortTemp = list()
    for j in range(n):
      temp.append(input())
    for j in range(n):
      sortTemp.append(input())

    mass.append(temp)
    corrMass.append(sortTemp)

def shell_sort(lst:list):
  g = len(lst) // 2

  while g>0:
    for v in range(g, len(lst)):
      name = lst[v]
      pos = v
      while pos >= g and lst[pos-g] > name:
        lst[pos] = lst[pos-g]
        pos-=g
        lst[pos] = name
    g //=2
  print("log^ ", lst)
  return lst
def data(mass:list, corrMass:list): # заполняет массивы рандомными блоками с рандомными типа именами
  for i in range(random.randint(1,50)):
    char = "qwertyuiopasdfghjklzxcvbnm1234567890"
    lenth = len(char)-1
    temp = list()
    for j in range(random.randint(3,10)):
      s = random.randint(0, lenth)
      temp.append(char[s])
      char = char.replace(char[s],'')
      lenth-=1

    mass.append(temp)
    corrMass.append(sorted(temp))      

def give_index(mass, corr:list): # составляет массив чисел, который является индексами сортированного сопоставленный с значениями не сортированного массива
  index_mass =[]
  
  for i in range(len(corr)):
    index_mass.append(corr.index(mass[i]))
  return index_mass

def swap(mass:list, index:list, buff:list, count=0): # сортирует массив с помощью массива индексов через рекурсию, заменяя ячейку буфером - в буффер заменяемую ячейку и вызывая саму себя
  if  buff[1] == index[buff[1]]: # проверка, что бы буфер не зациклился сам на себе, нужно заменить счетчик на что то по надежнее
    localCount = 0
    while index[localCount] == localCount and localCount<len(mass)-1:
      localCount+=1 # перебираются числа до того, пока число не будет совпадать с собственным индексом, что бы не было замыкания
    buffTemp = [mass[localCount], index[localCount]]
  else:
    buffTemp = [mass[buff[1]], index[buff[1]]]
    mass[buff[1]] = buff[0]
    index[buff[1]] = buff[1]

  if count >= len(mass)*2:
    return mass
  else:
    print("Recursion+1", index)
    count+=1
    return swap(mass, index, buffTemp,count)



# Main function
data(mass, corrMass)
print(mass,"\n",corrMass,'\n'*3)

for i in range(len(mass)):
  index = give_index(mass[i],corrMass[i])
  print(swap(mass[i], index, [mass[i][0],index[0]] ))

for i in range(len(mass)):
  print("Local result: ", mass[i]==corrMass[i])  









def sortF(mass:list, corrMass:list): # первая версия сортировки, работает кое как, как и в прочем последующая
  for name in range(len(mass)): 
    for i in range(name,len(mass)):
      if corrMass[i] == mass[name]:
        buff = '' 
        buff = mass[i] # place name in buffer
        mass[i] = mass[name] # assign name 
        mass[name] = buff
        break

#data(mass,corrMass)
#print("maass^ ")
#for i in mass:
#  print(i)

#print("correctMass")

#for i in corrMass:
#  print(i)



#count=0
#countB=0
#for block in mass: 
#  while True:
#    if block == corrMass[count]:
#      break
#    else:
#      sortF(block,corrMass[count])
#      print("...")
#      if countB>=len(mass)**2:
#        print("time out")
#        break
#      countB+=1
#  count+=1

#print("After^ ")
#for i in mass:
#  print(i)