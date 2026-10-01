input("Left shift doubles, right shift halves. Press Enter")
print(" 3 << 1 = ", 3 << 1, " 12 >> 1 = ", 12 >> 1)
print(" 3 << 2 = ", 3 << 2, " 12 >> 2 = ", 12 >> 2)

n = int(input("Enter a no. - (Try 5 / 8)"))
Guess = input("What is " + str(n) + "  << 2 ?? ")
input("Left shift by 2 multiplies 4. Press Enter")
print(" ", n, "<< 2 =", n << 2, "\nYour Guess - ", Guess)