prime_list = []
combined_list=[]
def get_prime(x):
    for integer in range(3,x):
        if is_prime(integer)==True:
            prime_list.append(integer)
    return prime_list



def is_prime(y):
    count=0
    for divisor in range(2,y//2+1):
        if y % divisor == 0:
            count = count + 1
    return count==0

def combine_prime(prime_list):
    for q in prime_list:
        for w in prime_list:
            for e in prime_list:
                for r in prime_list:
                    for t in prime_list:
                        combined_list.append([q,w,e,r,t])

def get_solution(combined_list):
    for m in combined_list:
        if verify(m)==True:
            return m
def verify(s):
    return s[0]*s[0]*s[0]+s[1]*s[1]*s[1]+s[2]*s[2]*s[2]+s[3]*s[3]*s[3]+s[4]*s[4]*s[4]+8==53353
