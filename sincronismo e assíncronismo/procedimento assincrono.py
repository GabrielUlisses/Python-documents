import time
import asyncio

async def ola():
    pass

def consecutive_numbers_needed(A):
    A.sort()

    numbers_to_add = []
    for idx, a in enumerate(A):
        if idx < len(A)-1 and A[idx+1] != a+1:
            for x in range(a+1,A[idx+1]):
                numbers_to_add.append(x)

    return numbers_to_add

async def quantity_consecutive_needed(numbers_to_add, n):
    print("Calling consecutive numbers needed...", n)
    await asyncio.sleep(0.01)
    
    amount_numbers_needed = len(consecutive_numbers_needed(numbers_to_add))
    print(amount_numbers_needed)

    return amount_numbers_needed


async def main():
    await asyncio.wait([
        quantity_consecutive_needed([6,2,2,2,2,2,3,8,8], 1)
        quantity_consecutive_needed([10,2,30,8,12], 2)
        quantity_consecutive_needed([5,3,10,18,30], 3)
    ])

t0 = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
t1 = time.time()

print("Time %.2f ms"%(1000*(t1-t0)))
"""
import asyncio

async def say(what, when):
    await asyncio.sleep(when)
    print(what)
    if when == 5:
       loop = asyncio.get_event_loop()
       loop.stop()

loop =  asyncio.new_event_loop()
for i in range(5, -1, -1):
    loop.create_task(say(f'hello world {i}', i))
    print(f"co-rotina {i} criada")
loop.run_forever()
loop.close()
"""
