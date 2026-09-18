#LAB 9 : FIND ROOT OF A NUMBER USING BISECTION METHOD

def square_root_bisection(num,tolerance=0.01,maxiter=100):
    iterations = 0 
    if num<0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if num==0 or num==1:
        print(f"The square root of {num} is {num}")
        return 0 if num==0 else 1
    low = 0 
    high = max(1,num)
    while (high-low)>tolerance and iterations<maxiter:
        mid = (low+high)/2
        if mid*mid > num:
            high = mid 
        else:
            low = mid
        iterations+=1
    if high-low<tolerance:
        print(f"The square root of {num} is approximately {(low+high)/2}")
        return (low+high)/2
    else:
        print(f"Failed to converge within {maxiter} iterations")
        return None

