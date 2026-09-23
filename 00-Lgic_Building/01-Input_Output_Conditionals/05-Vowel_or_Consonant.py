a = input("Enter a letter: ")

if len(a) != 1 or not a.isalpha():
  print("Enter a single letter")
elif a.lower() in ['a', 'e', 'i', 'o', 'u']:
  print("Vowel")
else:
  print("Consonant")