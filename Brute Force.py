import random
# -----------------------------------------------------------
OldPass = []
PPC = ""
MaxSum = 4
i = "1"
with open("symbol.txt") as file:
   S = file.read()
# -----------------------------------------------------------
print("Ваш пароль: ")
PMY = input()
# -----------------------------------------------------------
if len(PMY) > MaxSum:
   print("Пароль должен быть максимум 4 символа")
   exit()
# -----------------------------------------------------------
while i == "1":
   PPC += random.choice(S)
   if PPC not in OldPass:
      print(PPC)
      if PPC not in OldPass:
         if len(PPC) > 1:
            OldPass.append(PPC)
      if len(PPC) == MaxSum:
         PPC = ""
# -----------------------------------------------------------
while PPC == PMY:
   print(PPC + " - true")
   exit()
