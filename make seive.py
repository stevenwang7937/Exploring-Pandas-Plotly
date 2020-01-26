def makeSeive(limit): #seive of erastothenes
    nums = {0: False, 1: False}
    for i in range(2, limit+1):
        if i not in nums:
            nums[i] = True
            for k in range(2, (limit+1) % i):
                nums[i*k] = False
    return nums
def findPrimes(num):
    seive = makeSeive(num)
    for i in range(2, (num // 2) + 1):
        if seive[i] and seive[num-i]:
            return (i, num-i)
    return None
def eratosthenes(n):
    IsPrime = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if IsPrime[i]:
            for j in range(i * i, n + 1, i):
                IsPrime[j] = False
    return [x for x in range(2, n + 1) if IsPrime[x]]
