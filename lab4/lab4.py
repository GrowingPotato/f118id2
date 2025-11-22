import csv
def FormDataList(csvfile:str):
    Datalist = []
    with open(csvfile, 'r', encoding='utf-8') as CSVData:
        Data = CSVData.read().splitlines()
    for i in range(0, len(Data)):
        Datalist.append(Data[i].split(','))
    Datalist.pop(-1)
    return Datalist

def FormDictList(DataList):
    StudDictList = []
    x = 2
    for i in range(1, len(DataList)):
        a = None
        StudDict = {a: 2 for DataList[0][i] in range(0, len(DataList[0]))}
        StudDictList.append(StudDict)
    return StudDictList


#Stud = FormDictList(FormDataList('Student.csv'))
#Marks = FormDictList(FormDataList('Marks.csv'))
#print(FormDictList(FormDataList('Marks.csv')))#
print(FormDictList(FormDataList('Marks.csv')))