
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

base = int(input("Type the base num: "))
pow = int(input("Type the power num: "))

print(raise_to_power(base,pow))
    
