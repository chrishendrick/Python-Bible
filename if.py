# ==
# !=
# >
# <
# >=
# <=


num1 = input('Num1? ')
num2 = input('Num2? ')

if num1 > num2:
    print(str(num1)+' is bigger than '+str(num2))
    print('Num1 wins!')
elif num2 > num1:
    print(str(num2)+' is bigger than '+str(num1))
    print('Num2 wins!')
else:
    print(str(num1)+' equals '+str(num2))
    print('It\'s a tie!')

