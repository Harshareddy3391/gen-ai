import time
def sy_fun(city):

    print(f"wait whether searching in {city}")
    time.sleep(2)
    return f"is cool in {city}"
start=time.time()

li=["banglore","chennai"]
for i in li:
    res=sy_fun(i)
    print(res)

print(f"time :{round(time.time()-start,2)}")