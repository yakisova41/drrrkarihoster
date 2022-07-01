def dictCompare(beforeDicts, afterDicts):
    compareData = {
        'added':{},
        'removed':{},
        'updated':{}
    }

    if len(beforeDicts) > len(afterDicts):
        for beforeDictKey in beforeDicts:
            if not beforeDictKey in afterDicts.keys():
                compareData['removed'][beforeDictKey] = beforeDicts[beforeDictKey]

    elif len(beforeDicts) < len(afterDicts):
        for afterDictKey in afterDicts:
            if not afterDictKey in beforeDicts.keys():
                compareData['added'][afterDictKey] = afterDicts[afterDictKey]

    for afterDictKey in afterDicts:
        if afterDictKey in beforeDicts.keys():
            if afterDicts[afterDictKey] != beforeDicts[afterDictKey]:
                compareData['updated'][afterDictKey] = afterDicts[afterDictKey]
        
    return compareData
