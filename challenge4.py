import asyncio

async def db_read():
    print("reading from db")
    await asyncio.sleep(2)
    return {"data":100}

async def file_read():
    print("reading from the file server")
    await asyncio.sleep(2)
    print("reading from file been done")

async def task1(): 
    x=await db_read()
    print(x)

async def task2(): 
    await file_read()

async def main(): 
    x=asyncio.create_task(task1())
    y=asyncio.create_task(task2()) 
    
    # await x
    # print(x)
    # await y

asyncio.run(main())