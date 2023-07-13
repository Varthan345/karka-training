numbers=[1,100,445,300]
max=0

def largest(numbers,max):
    for number in numbers:
        if number>max:
            max=number        
    return max

print(largest(numbers,max))
    