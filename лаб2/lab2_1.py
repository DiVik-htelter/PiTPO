# сначала нам дают словарь, далее 2 слова(пару) и мы должны найти цепочку слов, 
# которая по 1 букве изменяеся и приводит от одного слова к другому

def letter_mathcers(w1,w2)-> int: # сколько букв совпадает
  count = 0
  for i in range(len(w1)):
    if w1[i] == w2[i]:
      count+=1
  return count

# проверка на то, что слова различаются лишь на 1 букву
def compasion_words(w1: str,w2:str) -> bool:
  # предполагается, что их длинна одинаковая
  count=0
  for i in range(len(w1)):
    if w1[i] != w2[i]:
      count+=1
    if count == 2:  return False
  if count == 0: # words identical
    return False
  return True

# возвращает список отличных от исходного слов на 1 букву
def scan_ident_words(word1, russ_words)-> list:
  ident_w = []
  for i in russ_words:
    if len(i) == len(word1):
      if compasion_words(i, word1):
        ident_w.append(i)

  return ident_w

f = open("D:\\2_курс\\4 семестр\\проектирование и тестирование по\\russian.txt")
russ_words = list(map(str, f.read().split("\n")))
f.close()

word1, word2 = list(map(str, input("Введите пару русских слов одинаковой длинны через пробел: ").split()))
if len(word1) != len(word2):
  exit()

ident_w = [word1]
for g in range(len(word1) - letter_mathcers(word1,word2)):
  count=0
  for i in range(count, len(ident_w)):
    ident_w += scan_ident_words(ident_w[i], russ_words)
    count+=1
  for i in range(count,len(ident_w)): # удаляем из общего списка найденые слова, что бы они в дальнейшем не пересекались 
    try: # таккая конструкция тут нужна, что бы не выдавал ошибку, когда не находит слово для удаления
      russ_words.remove(ident_w[i])
    except:
      print()

#print(ident_w)

flag = False
for i in ident_w: # проверка на то, нашли ли мы нужное слово
  if i == word2:
    flag = True
    print(f"{word1} == {word2}")
    break

chain = [word1]
while flag:
  for g in range(len(word1) - letter_mathcers(word1,word2) -1 ):
    print(f"Иттерация №{g}")
    for i in ident_w:
      #print(f"{compasion_words(chain[g],i)} and {letter_mathcers(i, word2)} > {letter_mathcers(chain[g], i)} {letter_mathcers(i, word2) > letter_mathcers(chain[g], i)} {i}")
      if compasion_words(chain[g], i) and (letter_mathcers(i, word2) >= letter_mathcers(chain[g], i)): # i отличается от слова из цепочки всего на 1 букву и содержит букву из последнего нужного слова
        chain.append(i)
        break
  break
chain+=word2
print(chain)

#chain = [word1]
#while flag:
#  for g in range(len(word1) - letter_mathcers(word1,word2) - 1):
#    for i in ident_w:
#      if compasion_words(chain[g], i) and compasion_words(i, )