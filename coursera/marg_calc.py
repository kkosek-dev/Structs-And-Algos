def calc(total):
    total = int(total)
    teq=round((5/16)*total,2)
    ts=round((5/48)*total,2)
    li=round((1/4)*total,2)
    lim=round((1/12)*total,2)
    ag=round((1/12)*total,2)
    ss=round((1/6)*total,2)
    return f"Marg Specs\nTequila: {teq}oz\nTriple Sec: {ts}oz\nLime: {li}oz\nLimeade: {lim}oz\nAgave: {ag}oz\nSimple Syrup: {ss}oz\n"

if __name__ == '__main__':
    total = input("Enter Total oz of Drink: ")
    print('----------------------------------------')
    print(calc(total))