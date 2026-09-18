#CERTIFICATION PROJECT 4: TOWER OF HANOI ALGORITHM

def hanoi_solver(num):
    rod1 = [i for i in range(num,0,-1)]
    rod2 = []
    rod3 = []

    def display_moves():
        return f"{rod1} {rod2} {rod3}\n"
    
    def move_disk(start,target):
        target.append(start.pop())
        return display_moves()
    
    def move_tower(start,target,aux,n):
        if n == 1:
            return move_disk(start,target)
        
        result = ""
        result+= move_tower(start,aux,target,n-1)
        result+=move_disk(start,target)
        result+=move_tower(aux,target,start,n-1)
        return result
    result = ""
    result+=display_moves()
    result+= move_tower(rod1,rod3,rod2,num)
    return result.rstrip("\n")

print(hanoi_solver(2))
