"""import asyncio
import time

async def get_val(city):
    print(f"whether is searching {city}")
    await asyncio.sleep(3)
    return f"very hot in {city}..>>"

async def main():

    s=time.time()

    c=["chennai","atp","Gooty"]

 
    res=await asyncio.gather(*(get_val(i) for i in c))

    for result in res:
        print(result)

    print(f"time: {int(time.time()-s)} seconds")


asyncio.run(main())"""


import time
import asyncio


async def get_val(city):

    
    print(f"whether searching in {city}")
    await asyncio.sleep(3)
    return f"very cool in {city}"
"""
async def main():
    s=time.time()
    city_list=["baglore","chennai","hyd"]
     

    res=await asyncio.gather(*(
            get_val(each_city) for each_city in city_list
    ))
    
    print(res)
    for i in res:
        print(i)

    print(f"time : {int(time.time()-s)} seconds")

"""

async def main():
    s=time.time()
    t1=asyncio.create_task(get_val("hyd"))
    t2=asyncio.create_task(get_val("bang"))
    res1=await t1
    res2=await t2
    print(res1)
    print(res2)

    print(f"time : {int(time.time()-s)}seconds")
asyncio.run(main())
