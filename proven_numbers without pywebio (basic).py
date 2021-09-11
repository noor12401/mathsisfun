import time

def prove_numbers():
    solution_1 = "Let's take an equation \n" \
                 "X\u00b2 - Y\u00b2 = X\u00b2 - Y\u00b2 \n" \
                 "L.H.S = R.H.S \n" \
                 "So, Applying formula: (a\u00b2 - b\u00b2) = (a + b)(a - b) , we get\n" \
                 "L.H.S = (X + Y)(X - Y)\n" \
                 "Let's assume X = Y \n" \
                 "Since X is equal to Y, we can replace Y with X and we get, \n" \
                 "L.H.S = (X + X)(X - X) ----------------(1) \n" \
                 "and R.H.S = (X\u00b2 - Y\u00b2) = (X\u00b2 - X\u00b2) \n" \
                 "After taking X as common, we get\n" \
                 "R.H.S = (X\u00b2 - X\u00b2) = X(X - X) ----------(2) \n" \
                 "Now comparing L.H.S = R.H.S, we get \n" \
                 "(X + X)(X - X) = X(X - X) ---from (1) & (2) \n" \
                 "(X - X) gets cancel out from both the sides, so we are left with \n" \
                 "(X + X) = X \n" \
                 "2X = X \n" \
                 "X gets cancel out from both the sides, so we are left with \n" \
                 "2 = 1 which is also equal to \n" \
                 "1 = 2 ------(4)"
    solution_2 = "Adding '1' on both the sides of the above equation, we get \n" \
                 "1+1 = {}+1 \n" \
                 "2 = {} \n" \
                 "Since (1 = 2) & (2 = {}), so we get \n" \
                 "1 = {} ---------- ({})"
    print("Hey folks, Mathematically you can prove 1 to be equal to any number! \n"
             "Type any smaller number first to understand the mathematical twist!")
    user = int(input("I want to prove 1 = "))
    print('Proving 1 = {}. Please wait.....'.format(user))
    time.sleep(3)
    if user > 2:
        print(solution_1)
        for i in range(2, user):
            print(solution_2.format(i, i + 1, i + 1, i + 1, i + 3))
        return "Hurray! We have proved 1 = {}".format(user)
    elif user == 2:
        print(solution_1)
        return "Hurray! We have proved 1 = {}".format(user)
    elif user == 1:
        return "1 is already equal to 1"
    else:
        return "Just reverse the process and start subtracting and you can prove 1 = {}".format(user)

print(prove_numbers())