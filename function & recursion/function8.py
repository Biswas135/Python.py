# WAP to convert USD to NPR

def conv_usd(usd):
    npr = usd * 144.06
    return npr

usd = int(input("Enter the USD to convert to NPR: "))
result = conv_usd(usd)

print(f"{usd} USD = {result} NPR")
