print("Введите минимальную сумму вложения в стартап?")
x=int(input())
print("Майкл, сколько Вы готовы вложить в стартап?")
Mic_fund=int(input())
print("Иван, а Вы сколько готовы вложить в стартап?")
Ivan_fund=int(input())

if Mic_fund>=x and Ivan_fund>=x:
    print("2")
elif Mic_fund>=x and Ivan_fund<x:
    print("Mike")
elif Mic_fund<x and Ivan_fund>=x:
    print("Ivan")
elif (Mic_fund+Ivan_fund)>=x:
    print("1")
else:
    print("0")


