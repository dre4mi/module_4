word = str(input("Введите слово: "))
reversword = word[::-1]
if word == reversword:
  print("True")
else:
  print("False")