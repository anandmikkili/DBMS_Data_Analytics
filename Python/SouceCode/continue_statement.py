shell = ['Andhra','Bihar','Chattisgarh','karnataka','Delhi','Madhya','Gujarat','Uttar', 'Arunachal','Himachal', 'Tamilnadu', 'Kerala','Telangana']
print("Before: ", shell)
for item in shell:
    if((item=="Andhra") or (item=="Madhya") or (item=="Uttar") or (item=="Arunachal") or (item=="Himachal")):
        updated = item+" Pradesh"
        shell.append(updated)
        shell.remove(item)
        print("Changed")
    else:
        continue

print("After: ", shell)
