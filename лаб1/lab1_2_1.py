
print("Построчно вводите целые числа(5 штук в строке)")
count=0

def checkRaund(number:list) -> list:
  categori=[0]*12
  count=0
  for i in number:
    count+=1
    categori[i-1]+=i # 1-6 категория, суммы выброшеных едииниц, двоек и тд
    categori[6]+=i # сумма всех чисел на костях

  for i in range(6):
    if categori[i]>=(i+1)*3: # 3 одинаковые + проверка на фулл-хаус
        categori[7] = sum(number)

        for k in range(6): # прверка на фулл-хаус
          if k != i and categori[k] >= (k+1)*2:
            categori[11] = 40

    if categori[i]>=(i+1)*4: # 4 одинаковые
        categori[8] = sum(number)
  
  for k in range(2): # короткий стрит 25
    endOfShortStreet = number[k + 3]
    if number[k] + 3 == endOfShortStreet and number[k + 1] + 2 == endOfShortStreet and number[k + 2] + 1 == endOfShortStreet:
        categori[9] = 25
  endOfShortStreet = number[4]

  # короткий стрит 35
  if number[0] + 4 == endOfShortStreet and number[1] + 3 == endOfShortStreet and number[2] + 2 == endOfShortStreet and number[3]+1 == endOfShortStreet:
    categori[10] = 35

  return categori
     
def checkCategori(temp:list, globCat:list) -> list:
  maxtempk = 0
  for i in range(len(temp)):
    if temp[i] - globCat[i] > 0:
      maxtempk = i
  globCat[maxtempk] = temp[maxtempk]
  return globalCat
          
globalCat = [0]*12
while True:
  r = list(map(int, input().split()))
  count+=1
  if count == 13 or r[0] == 0: break # конец игры и подсчет итоговых баллов или начало следующей
  
  temp = checkRaund(r)
  globalCat = checkCategori(temp, globalCat)

print(globalCat, sum(globalCat))