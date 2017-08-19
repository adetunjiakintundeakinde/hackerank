import operator
import sys

def buyMaximumProducts(n,k,a):
    dict = {}
    for i in range(n):
        dict[i+1] = a[i]
    sorted_dic = sorted(dict.items(), key=operator.itemgetter(1))
    no_of_stocks = 0
    last_value_k = 0
    length_sorted_dic = len(sorted_dic)
    price_of_stock_day =0
    for i in range(n):
        price_of_stock_day = sorted_dic[i][1]
        k = k - price_of_stock_day*sorted_dic[i][0]
        if k < 0:
            break
        else:
            last_value_k = k
            no_of_stocks+=sorted_dic[i][0]
    if k < 0:
        no_of_stocks+=last_value_k//price_of_stock_day
    return no_of_stocks


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    k = int(input().strip())
    result = buyMaximumProducts(n, k, arr)
    print(result)