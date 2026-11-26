bill = [3, 10, 2, 9]
k = 1                         
b = 7                               


def bonAppetit(bill, k, b):
    anna_share = (sum(bill) - bill[k]) // 2

    if anna_share == b:
        print("Bon Appetit")
    else:
        print(b - anna_share)


bonAppetit(bill, k, b)
