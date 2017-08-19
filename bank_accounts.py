import sys

def feeOrUpfront(n, k, x, d, p):
    # Complete this function
    fee_sum = 0
    for i in range(n):
        percentage_amount = x/100 * p[i]
        if(percentage_amount>k):
            fee_sum+=percentage_amount
        else:
            fee_sum+=k
    if(fee_sum>d):
        return 'upfront'
    else:
        return 'fee'

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, k, x, d = input().strip().split(' ')
        n, k, x, d = [int(n), int(k), int(x), int(d)]
        p = list(map(int, input().strip().split(' ')))
        result = feeOrUpfront(n, k, x, d, p)
        print(result)