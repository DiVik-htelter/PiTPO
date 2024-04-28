# пятнашка

def inputData (m:list): # Ввод массива пятнашек и проверка на корректность значений
  check = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
  for i in range(4):
    try:
      m.append(list(map(int, input().split())))
    except:
      m.clear
      print("Не делай так больше")
      return False
    if len(m[i]) !=4: # проверки на корректность данных
      m.clear
      print("Больше/меньше 4 значений")
      return False
    else:
      for j in m[i]:
        try:
          check.remove(j)
        except:
          m.clear
          print("Лишняя цифра")
          return False   
  print(m)
  return True  

m=[]
print(inputData(m))