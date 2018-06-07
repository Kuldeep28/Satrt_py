def loop_dict(trat):
    liste=list(trat.keys()) #keys fx will give list of all the values of keys of the dictionary
    print(liste)            #heere we are facing problem as we are geting a dict_key type object thats why we have to cast it
    liste.sort()
    for c in range(len(trat)):
        print(liste[c],trat[liste[c]])


tat={"ad":"vdnjv","ab":"dvbh","qqqc":"ii","pd":"op","e":"ajk"}




loop_dict(tat)