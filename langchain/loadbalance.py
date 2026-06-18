arry_data=[1,1,1,2,3,4,5,4,3,4,6,43,3,3]
val_data={} 

for i in arry_data:

    if i in val_data:
        val_data[i]+=1
    else:
        val_data[i]=1

print(val_data)
"""
val=[]
for i,num_d in val_data.items():
    val.append(num_d)

for j,num in val_data.items():
    if max(val) == num:
        print(j)"""

list_a=max(list(val_data.values()))
for i,num in val_data.items():
    if list_a == num:
        print(i)


 