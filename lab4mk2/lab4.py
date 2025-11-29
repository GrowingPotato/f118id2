import csv
def GetDataFromCSV(filename):
    with open(filename, 'r', encoding='utf8') as file:
        data = file.read()
        data = data.split('\n')
    return data

def FormDataDict(Datalist):
    DataDict = {}
    if len(Datalist[0].split(',')) == 3:
        Datalist.pop()
        Datalist.pop()

        for i in range(1, len(Datalist)):
            b = Datalist[i].split(',')
            if b[0] in DataDict:
                DataDict[b[0]][b[1]] = b[2]
            else:
                DataDict[b[0]] = {b[1]:b[2]}
    elif len(Datalist[0].split(',')) == 2:
        DataDict = {}
        Datalist.pop()
        for i in range(1, len(Datalist)):
            b = Datalist[i].split(',')
            DataDict[b[0]] = b[1]
    
    return DataDict

def UniteData(Marks, Student):
    for i in Marks:
        Marks[i]['ФИО'] = Student[i]
    return Marks
# Student = FormDataDict(GetDataFromCSV('Student.csv'))
# Marks = FormDataDict(GetDataFromCSV('Marks.csv'))
# for i in Marks:
#         Marks[i]['ФИО'] = Student[i]
# FinalData = Marks

def average_by_subject(data, subject):
    grade_sum = 0
    average_grade = 0
    for i in data:
        grade_sum = grade_sum + int(data[i][subject])
    average_grade = grade_sum/len(data)
    return average_grade

def average_by_student(data, student):
    localdata = data
    grade_sum = 0
    items_count = len(localdata['1']) - 1
    average_grade = 0
    for i in localdata[student]:
        if i == 'ФИО':
            continue
        grade_sum = grade_sum + int(localdata[student][i])
    average_grade = grade_sum/items_count
    return average_grade

def best_student(data):
    a = []
    for i in range(1, len(data)):
        a.append(str(average_by_student(data, str(i))))
    Max = max(a)
    return Max
print(best_student(UniteData(FormDataDict(GetDataFromCSV('Marks.csv')),FormDataDict(GetDataFromCSV('Student.csv')))))