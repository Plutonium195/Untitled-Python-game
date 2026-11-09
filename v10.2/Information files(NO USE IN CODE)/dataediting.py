# reads and saves the global inventory to local inventory
with open('data/inventory.txt','r') as file:
    f = file.read()
    inv = f.split(',')[:-1]


#reads and saves the local inventory to global inventory
with open('data/inventory.txt','w') as file:
    for i in inv:
        i += ','
        file.write(i)


#creates empty dict for playerdata and saves each line as a key/value pair
pdata = {}
with open('data/playerData.py','r') as file:
    for line in file:
        (key,val) = line.split('=')
        val = val[:-1]
        if val.isnumeric() == True:
            val = int(val)
        pdata[key] = val
    for key, value in pdata.items():
        globals()[key] = value

#This will update corresponding keys within the dict
pdata.update({"key 1": variable 1, "key 2": variable 2, etc...})

#creates key/value pairs and writes them to the playerData file
with open('data/playerData.py','w') as file:
    for key in pdata:
          val = pdata[key]
          file.write(f'{key}={val}\n')
