def apartment_selection(blocks,requirments) :
    blockLen = len(blocks)
    minDistance = {req : [float('inf')] * blockLen for req in requirments}
    for req in requirments : 
        closest = float('inf')
        for i in range(blockLen) :
            if blocks[i][req] :
                closest = i
            if closest != float('inf') :
                minDistance[req][i] = abs(i - closest)
        closest = float('inf')
        for i in reversed(range(blockLen)) :
            if blocks[i][req] :
                closest = i
            if closest != float('inf') :
                minDistance[req][i] = min(minDistance[req][i], abs(i - closest))
    maxDistance = [0] * blockLen
    for i in range(blockLen) :
        maxDistance[i] = max(minDistance[req][i] for req in requirments)
    bestBlock = maxDistance.index(min(maxDistance))
    return print(f"Best block = {bestBlock}")
blocks = [
    {
     "gym" : False,
     "school" : True,
     "store" : True
    },
    {
     "gym" : True,
     "school" : False,
     "store" : False
    },
    {
     "gym" : True,
     "school" : True,
     "store" : True
    },
    {
     "gym" : False,
     "school" : True,
     "store" : False
    },
    {"gym" : False,
     "school" : True,
     "store" : False
    }
    ]
reqs = ["gym","school","store"]
print(apartment_selection(blocks,reqs))