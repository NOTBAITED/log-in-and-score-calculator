username = (input("please enter your username "))

while username != ("BAITED"):
    print("incorrect username") 
    username = (input("please enter your username "))
if username == ("BAITED"):
    password = (input("please enter your password "))
while password != ("YES"):
    print("incorrect password")
    password = (input("please enter your password "))
else:
    print("welcome back mr.",username)

print("let us get started with calculating the scores")

score1 = float(input("please enter your first score "))
score2 = float(input("please enter your second score "))

tottal_score = score1 + score2

if tottal_score > 15  :
    print("congratulations you have passed")
elif tottal_score < 15 and tottal_score > 10:
    print("retake")
elif tottal_score < 10:
    print("we are sorry to inform you that you have failed, better luck next time ")