import time

def consecutive_numbers_needed(A):
    A.sort()

    numbers_to_add = []
    for idx, a in enumerate(A):
        if idx < len(A)-1 and A[idx+1] != a+1:
            for x in range(a+1,A[idx+1]):
                numbers_to_add.append(x)

    return numbers_to_add

def quantity_consecutive_needed(numbers_to_add, n):
    print("Calling consecutive numbers needed...", n)

    time.sleep(0.01)
    amount_numbers_needed = len(consecutive_numbers_needed(numbers_to_add))
    print(amount_numbers_needed)

    return amount_numbers_needed


def main():
    quantity_consecutive_needed([6,2,2,2,2,2,3,8,8], 1)
    quantity_consecutive_needed([10,2,30,8,12], 2)
    quantity_consecutive_needed([5,3,10,18,30], 3)

t0 = time.time()
main()
t1 = time.time()

print("Time %.2f ms"%(1000*(t1-t0)))

