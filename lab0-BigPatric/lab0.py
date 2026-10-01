def myFunction():
    '''
    Write a Python function that return sum of even digits of your student ID
    - Example 1: 311552006 -> 2+0+0+6 = 8
    - Example 2: 312551164 -> 2+6+4 = 12

    # Your Student ID should be hard-coded into this function
    '''
    ID = '112550018' 
    sum = 0
    for i in ID:
        if(i%2==0):
            sum+=i;
    return sum

if __name__ == '__main__':
    print(f'sum of even digits = { myFunction() }')

