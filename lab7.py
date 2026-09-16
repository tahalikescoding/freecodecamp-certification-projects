#LUHNS ALGORITHM

def verify_card_number(n:str):
    trans = {"-":""," ":""}
    table = str.maketrans(trans)
    n = n.translate(table)
    num = int(n)
    digit = []
    num,last = divmod(num,10)
    digit.append(last)
    pos = 0
    while num>0:
        num,last = divmod(num,10)
        if pos%2==0:
            if last*2>9:
                last = last*2
                s = 0 
                while last>0:
                    last , new_last = divmod(last , 10)
                    s+=new_last
                if s>9:
                    digit.append(s-9)
                digit.append(s)
            else:
                digit.append(last*2)
        else:
            digit.append(last)
        pos+=1
    if sum(digit)%10 == 0 :
        return "VALID!"
    else:
        return "INVALID!"




