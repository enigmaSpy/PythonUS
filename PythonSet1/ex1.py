from datetime import datetime

def addItemsToArray(x:int):
    dt=datetime.now()
    table =[]
    index:int = 0
    while True:
        if index >= x:
            break
        index+=1
        table.append(index)
    dt2=datetime.now();
    print(f"Adding {x} items took {(dt2-dt).total_seconds()}s")

itemsToAdd:int=int(input("How many items to add?\n"))
addItemsToArray(itemsToAdd)
