full_dot = '●'
empty_dot = '○'
def create_character(cname , s , i , c):
    while True: 
        c = 0 
        if cname.replace(" " , "").isalpha():
            c = 1
        if c ==0:
            print("The character name should be a string.")
            continue
        if len(cname) == 0 : 
            print("The character should have a name.")
            continue 
        if len(cname)>10:
            print("The character name is too long.")
            continue 
        f = 0 
        for i in cname: 
            if i == " ":
                f= 1 
        if f==1:
            print("The character name should not contain spaces.")
            continue 
        else:
            break
    while True:
        l = []
        l.insert(0 , s)
        l.insert(1 , i) 
        l.insert(2 , c)
        for j in l:
            j = str(j)
            if j.isdigit() == False:
                print("All stats should be integers")
                continue
        for j in l:
            if int(j) > 4:
                print("All stats should be no more than 4")
                continue    
        if int(s) + int(i) + int(c) != 7:
            print("The sum of all stats should be 7")
            continue
        else:
            break
    slist = []
    for j in range(10):
        slist.append(empty_dot)
    for j in range(int(s)):
        slist[j] = full_dot
    sstr = "".join(slist)

    ilist = []
    for j in range(10):
        ilist.append(empty_dot)
    for j in range(int(i)):
        ilist[j] = full_dot
    istr = "".join(ilist)

    clist = []
    for j in range(10):
        clist.append(empty_dot)
    for j in range(int(c)):
        clist[j] = full_dot
    cstr = "".join(clist0)

    p = f"{cname}\nSTR {sstr}\n INT {istr}\nCHA {cstr}"
    return p 



    

print(create_character("taha" , 3 , 2 , 2))

