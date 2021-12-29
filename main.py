import random
def shuffle(string):
  lis = list(string)
  random.shuffle(lis)
  return ''.join(lis)
ucl1=random.randint(65,90)
ucl2=random.randint(65,90)
lcl1=random.randint(97,122)
lcl2=random.randint(97,122)
n1=random.randint(48,57)
n2=random.randint(48,57)

pd1=random.randint(1,2)
if pd1 == 1:
  p1 = random.randint(33,64)
elif pd1 == 2:
  p1=random.randint(91,152)

pd2 = random.randint(1,2)
if pd2 == 1:
  p2 = random.randint(33,64)
elif pd2 == 2:
  p2=random.randint(91,152)

ucl1=chr(ucl1)
ucl2=chr(ucl2)
lcl1=chr(lcl1)
lcl2=chr(lcl2)
n1=chr(n1)
n2=chr(n2)
p1=chr(p1)
p2=chr(p2)
pwd = ucl1 + ucl2+lcl1+lcl2+n1+n2+p1+p2
pwd = shuffle(pwd)
user_word=input('Enter a word that is associated with your password: ')
user_word=user_word.capitalize()
location=random.randint(1,len(pwd))
b=pwd[:location]
e=pwd[location:]
pwd = b + user_word + e
print(pwd)
