import asyncio

# async def send_email1():
#     print("sending email-1")
#     await asyncio.create_task(send_email2())
#     print("response from email-1")

async def send_email1():
    print("sending email-1")
    await asyncio.ensure_future(send_email2())
    print("response from email-1")

async def send_email2():
    print("sending email-2")
    await asyncio.sleep(2)
    print("getting response from email-2")
    

asyncio.run(send_email1())