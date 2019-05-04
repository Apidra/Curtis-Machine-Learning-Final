i = {
    'fixed': 0, 
    'volatile' : 1,
    'citric' : 2,
    'residual' : 3,
    'chlorides' : 4, 
    'freeSulfur' : 5,
    'totalSulfur' : 6,
    'density' : 7,
    'ph' : 8,
    'sulfates' : 9,
    'alcohol' : 10,
    'quality' : 11,
}

def main():
    driverStandings = open('wine.csv', 'r')
    
    outFileX = open('wine_X.csv', 'w')
    outFileY = open('wine_Y.csv', 'w')
    
    #seperate quality from features, put features into wine_X, quality into wine_Y
    firstLine = True
    for line in driverStandings:
        if not firstLine:
            tokens = line.split(',')
            
            fixed = tokens[i['fixed']].strip()
            volatile = tokens[i['volatile']].strip()
            citric = tokens[i['citric']].strip()
            residual = tokens[i['residual']].strip()
            chlorides = tokens[i['chlorides']].strip()
            freeSulfur = tokens[i['freeSulfur']].strip()
            totalSulfur = tokens[i['totalSulfur']].strip()
            density = tokens[i['density']].strip()
            ph = tokens[i['ph']].strip()
            sulfates = tokens[i['sulfates']].strip()
            alcohol = tokens[i['alcohol']].strip()
            quality = tokens[i['quality']].strip()
            
            outFileX.write('{},{},{},{},{},{},{},{},{},{},{}\n'.format(fixed,volatile,citric,residual,chlorides,freeSulfur,totalSulfur,density,ph,sulfates,alcohol))
            outFileY.write('{}\n'.format(quality))
            
        firstLine = False
        
    outFileX.close()
    outFileY.close()
            
main()