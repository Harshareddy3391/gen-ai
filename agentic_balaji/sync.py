import time

def get_w(city):

    print(f"whether wait {city}")
    time.sleep(2)
    return  f"{city}is cool......"


s=time.time()
a=["bang","punr","hyd"]

for i in a:

    res=get_w(i)
    print(res)

e=time.time()

print(f"time: {round(e-s)} seconds")