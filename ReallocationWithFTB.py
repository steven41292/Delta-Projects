# open files
resFile = open('qryRedistribution.csv', 'r')
writeTo = open('RedistributionResults.csv', 'w')

# dictionary of all item numbers
dicItems = {};
FTBItems = {};

# get all lines
for strLine in resFile.read().split():
	
	# get each item in its own array
        lstLine = strLine.split(',')
        
	# add item to dictonary if needed
        if lstLine[0] not in dicItems:
                dicItems[lstLine[0]] = []
                
        #Sets up dictionary for FTBs.
        if lstLine[4]!="MULTI":
                FTBItems[lstLine[0]]= lstLine[4]
	
	# add record to dic - city, need, priority
	try:
                dicItems[lstLine[0]].append([lstLine[1], int(lstLine[2]), int(lstLine[3])])
        except:
                print (lstLine[0])


# ----------------------------------------
# All Data has been put into the dictonary
# ----------------------------------------

# go though the dictonary
count2=0
for item in dicItems:
        count=-1
        ATLCount=-1
        for specItems in dicItems[item]:
                count+=1
                if specItems[0]=="ATL":
                        if ATLCount==-1:
                                ATLCount=count
                        else:
                                specItems[1]+=dicItems[item][ATLCount][1]
                                
                
writeTo.write("PARTNUMBER, FROMSTATION, QUANTITY, DESTINATION \n")
for strKey, lstItem in dicItems.iteritems():
	
	# prioritize the current values per key
        dicPriority = {}
        dicExcess = {}
	
	# go though each item in dic
        for lstAirport in lstItem:
		
		# skip if airport is good
                if lstAirport[1] == 0:
                        continue
			
		# save excess qty for each airport
                elif lstAirport[1] > 0:
                        dicExcess[lstAirport[0]] = lstAirport[1]
		
		# figure out priority
                else:
			
			# save excess qty for each airport
                        if lstAirport[2] not in dicPriority:
                                dicPriority[lstAirport[2]] = {}
			
			# save the city and the need in the dic
                        dicPriority[lstAirport[2]][lstAirport[0]] = lstAirport[1] * -1
	
	#print dicExcess
	#print dicPriority
	
	# put the cities in order
        lstNeedCitys = []
        for intPriority in range(1, 12):
                if intPriority in dicPriority:
                        for strNeedAirport, intNeed in dicPriority[intPriority].iteritems():
                                lstNeedCitys.append([intNeed, strNeedAirport])
	
	# count airport currently at
        intAirportCount = 0
	# see where to send surplus
        for strExcessAirport, intExcess in dicExcess.iteritems():

                #Checks all FTBs, one at a time.
                if (FTBItems.get(strKey)=="MD88" or FTBItems.get(strKey)=="M88"):
                        ans= 0
                        for item in lstNeedCitys:
                        
                                if "ATL" in item:
                                
                                        ans=lstNeedCitys.index(item)
                                        break
                
                        if ans:
                                
                                while(lstNeedCitys[ans][0]>0 and intExcess>0):
                                
                                        if lstNeedCitys[ans][0] >= intExcess:
                                        
                                                writeTo.write( strKey + ',' + strExcessAirport + ',' + str(intExcess) + ',' + "ATL" + '\n')
                                        
                                                lstNeedCitys[ans][0] -= intExcess
                                                intExcess = 0
                                
                                        else:
                                                writeTo.write( strKey + ',' + strExcessAirport + ',' + str(lstNeedCitys[ans][0]) + ',' + 'ATL' + '\n')
                                        
                                                intExcess -= lstNeedCitys[ans][0]
                                                lstNeedCitys[ans][0]=0
                                        # check if airport is even
                                        if lstNeedCitys[ans][0] == 0:
                                                del lstNeedCitys[ans]
                                                break
                if FTBItems.get(strKey)=="DC9":
                        ans= 0
                        for item in lstNeedCitys:
                        
                                if "DTWA" in item:
                                
                                        ans=lstNeedCitys.index(item)
                                        break
                
                        if ans:
                                
                                while(lstNeedCitys[ans][0]>0 and intExcess>0):
                                
                                        if lstNeedCitys[ans][0] >= intExcess:
                                        
                                                writeTo.write( strKey + ',' + strExcessAirport + ',' + str(intExcess) + ',' + "DTWA" + '\n')
                                        
                                                lstNeedCitys[ans][0] -= intExcess
                                                intExcess = 0
                                
                                        else:
                                                writeTo.write( strKey + ',' + strExcessAirport + ',' + str(lstNeedCitys[ans][0]) + ',' + 'DTWA' + '\n')
                                        
                                                intExcess -= lstNeedCitys[ans][0]
                                                lstNeedCitys[ans][0]=0
                                        # check if airport is even
                                        if lstNeedCitys[ans][0] == 0:
                                                del lstNeedCitys[ans]
                                                break

                if (FTBItems.get(strKey)=="M90" or FTBItems.get(strKey)=="MD90"):
                        ans= 0
                        for item in lstNeedCitys:
                        
                                if "MSPD" in item:
                                
                                        ans=lstNeedCitys.index(item)
                                        break
                
                        if ans:
                                
                                while(lstNeedCitys[ans][0]>0 and intExcess>0):
                                
                                        if lstNeedCitys[ans][0] >= intExcess:
                                        
                                                writeTo.write( strKey + ',' + strExcessAirport + ',' + str(intExcess) + ',' + "MSPD" + '\n')
                                        
                                                lstNeedCitys[ans][0] -= intExcess
                                                intExcess = 0
                                
                                        else:
                                                writeTo.write( strKey + ',' + strExcessAirport + ',' + str(lstNeedCitys[ans][0]) + ',' + 'MSPD' + '\n')
                                        
                                                intExcess -= lstNeedCitys[ans][0]
                                                lstNeedCitys[ans][0]=0
                                        # check if airport is even
                                        if lstNeedCitys[ans][0] == 0:
                                                del lstNeedCitys[ans]
                                                break

                if (FTBItems.get(strKey)=="B737" or FTBItems.get(strKey)=="737"):
                        ans= 0
                        for item in lstNeedCitys:
                        
                                if "DTW" in item:
                                
                                        ans=lstNeedCitys.index(item)
                                        break
                
                        if ans:
                                
                                while(lstNeedCitys[ans][0]>0 and intExcess>0):
                                
                                        if lstNeedCitys[ans][0] >= intExcess:
                                        
                                                writeTo.write( strKey + ',' + strExcessAirport + ',' + str(intExcess) + ',' + "DTW" + '\n')
                                        
                                                lstNeedCitys[ans][0] -= intExcess
                                                intExcess = 0
                                
                                        else:
                                                writeTo.write( strKey + ',' + strExcessAirport + ',' + str(lstNeedCitys[ans][0]) + ',' + 'DTW' + '\n')
                                        
                                                intExcess -= lstNeedCitys[ans][0]
                                                lstNeedCitys[ans][0]=0
                                        # check if airport is even
                                        if lstNeedCitys[ans][0] == 0:
                                                del lstNeedCitys[ans]
                                                break
                        if intExcess>0:
                                ans= 0
                                for item in lstNeedCitys:
                        
                                        if "CVG" in item:
                                
                                                ans=lstNeedCitys.index(item)
                                                break
                
                                if ans:
                        
                                        while(lstNeedCitys[ans][0]>0 and intExcess>0):
                                
                                                if lstNeedCitys[ans][0] >= intExcess:
                                        
                                                        writeTo.write( strKey + ',' + strExcessAirport + ',' + str(intExcess) + ',' + "CVG" + '\n')
                                        
                                                        lstNeedCitys[ans][0] -= intExcess
                                                        intExcess = 0
                                
                                                else:
                                                        writeTo.write( strKey + ',' + strExcessAirport + ',' + str(lstNeedCitys[ans][0]) + ',' + 'CVG' + '\n')
                                        
                                                        intExcess -= lstNeedCitys[ans][0]
                                                        lstNeedCitys[ans][0]=0
                                                # check if airport is even
                                                if lstNeedCitys[ans][0] == 0:
                                                        del lstNeedCitys[ans]
                                                        break

                if (FTBItems.get(strKey)=="B757" or FTBItems.get(strKey)=="757"):
                        ans= 0
                        for item in lstNeedCitys:
                        
                                if "MCO" in item:
                                
                                        ans=lstNeedCitys.index(item)
                                        break
                
                        if ans:
                                
                                while(lstNeedCitys[ans][0]>0 and intExcess>0):
                                
                                        if lstNeedCitys[ans][0] >= intExcess:
                                        
                                                writeTo.write( strKey + ',' + strExcessAirport + ',' + str(intExcess) + ',' + "MCO" + '\n')
                                        
                                                lstNeedCitys[ans][0] -= intExcess
                                                intExcess = 0
                                
                                        else:
                                                writeTo.write( strKey + ',' + strExcessAirport + ',' + str(lstNeedCitys[ans][0]) + ',' + 'MCO' + '\n')
                                        
                                                intExcess -= lstNeedCitys[ans][0]
                                                lstNeedCitys[ans][0]=0
                                        # check if airport is even
                                        if lstNeedCitys[ans][0] == 0:
                                                del lstNeedCitys[ans]
                                                break
                        if intExcess>0:
                                ans= 0
                                for item in lstNeedCitys:
                        
                                        if "SEA" in item:
                                
                                                ans=lstNeedCitys.index(item)
                                                break
                
                                if ans:
                                        
                                        while(lstNeedCitys[ans][0]>0 and intExcess>0):
                                
                                                if lstNeedCitys[ans][0] >= intExcess:
                                        
                                                        writeTo.write( strKey + ',' + strExcessAirport + ',' + str(intExcess) + ',' + "SEA" + '\n')
                                        
                                                        lstNeedCitys[ans][0] -= intExcess
                                                        intExcess = 0
                                
                                                else:
                                                        writeTo.write( strKey + ',' + strExcessAirport + ',' + str(lstNeedCitys[ans][0]) + ',' + 'SEA' + '\n')
                                        
                                                        intExcess -= lstNeedCitys[ans][0]
                                                        lstNeedCitys[ans][0]=0
                                                # check if airport is even
                                                if lstNeedCitys[ans][0] == 0:
                                                        del lstNeedCitys[ans]
                                                        break
                                
                                

                if FTBItems.get(strKey)=="A319" or FTBItems.get(strKey)=="A320":
                        ans= 0
                        for item in lstNeedCitys:
                        
                                if "BOS" in item:
                                
                                        ans=lstNeedCitys.index(item)
                                        break
                
                        if ans:

                                
                                while(lstNeedCitys[ans][0]>0 and intExcess>0):
                                        
                                        if lstNeedCitys[ans][0] >= intExcess:
                                        
                                                writeTo.write( strKey + ',' + strExcessAirport + ',' + str(intExcess) + ',' + "BOS" + '\n')
                                        
                                                lstNeedCitys[ans][0] -= intExcess
                                                intExcess = 0
                                
                                        else:
                                                writeTo.write( strKey + ',' + strExcessAirport + ',' + str(lstNeedCitys[ans][0]) + ',' + 'BOS' + '\n')
                                        
                                                intExcess -= lstNeedCitys[ans][0]
                                                lstNeedCitys[ans][0]=0
                                        # check if airport is even
                                        if lstNeedCitys[ans][0] == 0:
                                                del lstNeedCitys[ans]
                                                break
                                                
                        if intExcess>0:
                                ans= 0
                                for item in lstNeedCitys:
                        
                                        if "SLC" in item:
                                
                                                ans=lstNeedCitys.index(item)
                                                break
                
                                if ans:
                                        

                                        while(lstNeedCitys[ans][0]>0 and intExcess>0):
                                
                                                if lstNeedCitys[ans][0] >= intExcess:
                                        
                                                        writeTo.write( strKey + ',' + strExcessAirport + ',' + str(intExcess) + ',' + "SLC" + '\n')
                                        
                                                        lstNeedCitys[ans][0] -= intExcess
                                                        intExcess = 0
                                
                                                else:
                                                        writeTo.write( strKey + ',' + strExcessAirport + ',' + str(lstNeedCitys[ans][0]) + ',' + 'SLC' + '\n')
                                        
                                                        intExcess -= lstNeedCitys[ans][0]
                                                        lstNeedCitys[ans][0]=0
                                                # check if airport is even
                                                if lstNeedCitys[ans][0] == 0:
                                                        del lstNeedCitys[ans]
                                                        break


                                
                while intExcess > 0 and intAirportCount < len(lstNeedCitys):
                           
                        # allocate items
                        if lstNeedCitys[intAirportCount][0] >= intExcess:
                                writeTo.write( strKey + ',' + strExcessAirport + ',' + str(intExcess) + ',' + lstNeedCitys[intAirportCount][1] + '\n')
                                lstNeedCitys[intAirportCount][0] -= intExcess
                                intExcess = 0
                                
                        else:
                                writeTo.write( strKey + ',' + strExcessAirport + ',' + str(lstNeedCitys[intAirportCount][0]) + ',' + lstNeedCitys[intAirportCount][1] + '\n')
                                intExcess -= lstNeedCitys[intAirportCount][0]
                                lstNeedCitys[intAirportCount][0] = 0
                                
                        # check if airport is even
                        if lstNeedCitys[intAirportCount][0] == 0:
                                intAirportCount += 1

# close file
print("File written.")
resFile.close()
writeTo.close()

