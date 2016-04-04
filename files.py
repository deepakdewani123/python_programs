introName = ["keywords","identifiers","variables","datatypes","io","operator"]
arrayName = ["single-dimensional-array","multi-dimensional-array","array-and-functions"]
stringName = ["strings","string-functions"]
decisionName = ["if","if-else","if-else-if","switch"]
loopName= ["for","while","do-while"]
functionName = ["library-functions","user-defines-functions"]
structureName = ["syntax","declaration","accessing-functions"]
pointerName= ["pointers","pointer-and-arrays","pointer-and-functions"]
filesName= ["file-operations","working","opening","closing"]
miscellaneousName= ['enumerations', 'preprocessors', 'library-functions', 'algorithm', 'flowchart', 'pseudocode']

fileName = ["Description","Syntax","Example","Output"]
newFileName = []
arrayInArray = []

for file in miscellaneousName:
    for name in fileName:
        completeName = file+name+'.txt'
        newFileName.append(completeName)
    arrayInArray.append(newFileName)
    newFileName = []

        

print(arrayInArray)
