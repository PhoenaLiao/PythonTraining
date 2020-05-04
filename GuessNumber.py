#第一支程式
#猜數字

import random

print("遊戲規則: \n\
數字相同位置相同則為A，數字相同位置不同則為B，均不同則不顯示\n")
Answers = random.sample('123456789', 4)
print(Answers, len(Answers))

def input_num():
    isnum = False
    while not (isnum):
        try:
            Guess = int(input("請輸入4個數字: "))
            if Guess < 0:
                print("輸入的數字必需大於0，請重新輸入4個數字!")
            elif len(str(Guess)) > 4:
                print("輸入的數字超過4碼，請重新輸入!")
            else:
                isnum = True
        except:
            print("輸入的是字串，請重新輸入4個數字!")

    return list(str(Guess))

#填輸入的數值
ListGus = input_num()
#print("Gus: ", ListGus)

bingo = False
while (not bingo):
    a = 0
    b= 0
    print("Gus: ", ListGus)
    for Ans in range(len(Answers)):
        for Gus in range(len(ListGus)):
            #數字相同位置相同
            if ((Answers[Ans] == ListGus[Gus]) & (Ans == Gus)):
                a = a + 1
            #數字相同位置不同
            if ((Answers[Ans] == ListGus[Gus]) & (Ans != Gus)):
                b = b + 1

    if (a == len(Answers)):
        bingo = True
        print("恭喜你答對了!")
    else:
        print("提示: ", a, "A", b, "B")
        ListGus = input_num()
