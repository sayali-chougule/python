a = int(input("Enter a grade: "))

# 90+ A, 75+ B, 60+ C, 40+ D, else F.
if a >= 90:
  print("A")
elif a >= 75:
  print("B")
elif a >= 60:
  print("C")
elif a >= 40:
  print("D")
else:
  print("F")