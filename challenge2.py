import asyncio

async def fetch_data():
    await asyncio.sleep(2)
    return {"data":100}

async def countdwn_num():
    for i in range(10,0,-1):
        print(i)
        await asyncio.sleep(2)
        # if i ==5:
        #     x=await fetch_data()
        #     print(x)
        # else:
        #     continue
        

# async def data():
#     x=await fetch_data()
#     print(x)
    
# async def count():
#     await countdwn_num()
           
async def main():
    x1=asyncio.create_task(fetch_data())
    y1=asyncio.create_task(countdwn_num())
    
    asyncio.gather(x1,y1)
    # data=await x1
    
    # print(data)
    
    # await y1
    
    # await y1
    # await x1

asyncio.run(main())

# countdwn_num()
