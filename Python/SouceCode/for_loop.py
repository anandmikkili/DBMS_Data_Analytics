shell = ['Andhra Pradesh','Bihar','Chattisgarh','karnataka','Delhi','Madhya Pradesh','Gujarat','Uttar Pradesh']
for item in shell:
    if(item=="karnataka"):
        shell.append("Karnataka")
        shell.remove("karnataka")
        break;
    print(item)

print(shell)
