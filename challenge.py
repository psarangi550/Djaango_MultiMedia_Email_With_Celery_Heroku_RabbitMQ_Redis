#code Challenge

import asyncio

async def t1():
    
    await t2()
    
    print ("t1 task1")
    
async def t2():
    
    print("t2 task2")
    
async def t3():
    
    await t1()
    
    print("t3 task3")

# asyncio.run(t3())

async def main():
    x=asyncio.create_task(t3())
    asyncio.gather(x)

asyncio.run(main())