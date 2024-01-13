import math

while True:
    user = input("Введіть дію, яку хочете зробити (+, -, *, /, !, %, синус, косинус, тангенс, котангенс, корінь) ")

    if user not in ['+', '-', '*', '/', '!', '%', 'синус', 'косинус', 'тангенс', 'котангенс', 'корінь']:
        print("Ви ввели невірну дію. Будь ласка, введіть вірну дію.")
    else:
        if user == '!':
            num = int(input("Введіть число для визначення факторіалу: "))
            def Fact_of_Num(num):
                return math.factorial(num)
            result = Fact_of_Num(num)
            print(result)
        
        elif user == '%':
            num = int(input("Введіть число : "))
            percentage = int(input("Введіть відсоток : "))
            result = (percentage / 100) * num
            print(result)

        elif user == 'синус':
            num = int(input("Введіть число для знаходження його синуса : "))
            def Sin_of_Num(num):
                return math.sin(num)
            result = Sin_of_Num(num)
            result1 = round(result, 3)
            print(result1)
        
        elif user == 'косинус':
            num = int(input("Введіть число для знаходження його косинуса : "))
            def Cos_of_Num(num):
                return math.cos(num)
            result = Cos_of_Num(num)
            result1 = round(result, 3)
            print(result1)

        elif user == 'тангенс':
            num = int(input("Введіть число для знаходження його тангенса : "))
            def Tan_of_Num(num):
                return math.tan(num)
            result = Tan_of_Num(num)
            result1 = round(result, 3)
            print(result1)

        elif user == 'котангенс':
            num = int(input("Введіть число для знаходження його котангенса : "))
            def Cotn_of_Num(num):
                return 1 / math.sin(num)
            result = Cotn_of_Num(num)
            result1 = round(result, 3)
            print(result1)
        
        elif user == 'корінь':
            num = int(input("Введіть число для визначення квадратного кореня : "))
            def Sqrt_of_Num(num):
                return math.sqrt(num)
            result = Sqrt_of_Num(num)
            print(result)

        elif user in ['+', '-', '*', '/']:
            num_list = [int(i) for i in input("Введіть числа через пробіл: ").split()]

            def Operation_of_Num(*num):
                if user == '+':
                    result = sum(num)
                elif user == '-':
                    result = num[0] - sum(num[1:])
                elif user == '*':
                    result = 1
                    for j in num:
                        result *= j
                elif user == '/':
                    result = num[0]
                    for j in num[1:]:
                        result /= j

                print(result)
                
            Operation_of_Num(*num_list)
                
        break