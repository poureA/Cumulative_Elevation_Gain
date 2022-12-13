def Cumulative_Elevation_Gain(start,Elevations)->int:
    '''function docstring'''
    pit = 0
    gain = int(Elevations[0][4:]) - start
    for i in Elevations[1:] :
        if i[0:4] == 'peak' :
            peak = int(i[4:])
            val = peak - pit
            gain += val
            pit = 0
        elif i[0:3] == 'pit' :
            pit = int(i[3:])
        else :
            return f'invalid value for Elevations , {i}'
    return gain
#test cases
print(Cumulative_Elevation_Gain(1800,['peak2100','pit1950','peak2240']))
print(Cumulative_Elevation_Gain(1500,['peak1850','pit1800','peak2100','pit1900','peak2400']))
#running function
lst = list()
while ask:=input('enter Altitude of peak or pit (for example peak2500 or pit1800) :') :
    lst.append(ask)
print(Cumulative_Elevation_Gain(int(input('enter Starting Altitude:')),lst))
exit = input('enter any key to exit :')
