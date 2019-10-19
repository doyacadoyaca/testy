def div(a, b):
    return (a + b)**2

#if div(3, 6) == 0.5:
    #print("PASSED")
#else:
    #raise Exception("FAILED")

assert div(2, 3) == 25, "FAILED"
print("PASSED")


assert div(3, 4) == 49, "FAILED"
print("PASSED")

assert div(4, 4) == 64, "FAILED"
print("PASSED")

#try:
    #div(5, 0)
#except:
    #print("PASSED")

#assert div(100, 0) == 10, "FAILED"
#print("PASSED")

print(div(2,1) + div(-4, 2))

#if __name__ == '__main__':
    #print(div(10,0))



def factorial(n):

    result = 1

    for i in range(1, n + 1):
        result *= i
    return result


assert factorial(0) == 1, "FAILED"
print("PASSED")




