# you can change these values to test your program with different values
pbot = 0.01
p8_bot = 0.9
p8_human = 0.9

def bot8(pbot, p8_bot, p8_human):
    p8_dig = p8_bot * pbot + p8_human * (1-pbot)
    pbot = (p8_bot * pbot) / p8_dig
    print(pbot)

bot8(pbot, p8_bot, p8_human)
