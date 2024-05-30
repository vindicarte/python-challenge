import os
import csv

#open file
budget_data_csv = os.path.join('Resources/PyBank/Resources', 'budget_data.csv')
outputbank_txt = os.path.join('Resources/PyBank/Resources', 'outputbank.txt')

#/Users/michaelsanchez/Documents/Data Analytics Courses/Week 3 Files - Python/Challenge Files/Resources/PyBank/Resources
totalmonths = 0
monthofchange = []
netchangelist = []
greatestincrease = ["",0]
greatestdecrease = ["", 9999999999]
totalnet = 0

#determine the total of profits and losses
with open(budget_data_csv) as fin:
    csv_reader = csv.reader(fin, delimiter=",")

    headerline = next(csv_reader)

    firstrow = next(csv_reader)
    #Getting total months
    totalmonths += 1
    totalnet = int(firstrow[1])
    previousnet = int(firstrow[1])

    for row in csv_reader:
        totalmonths += 1
        totalnet += int(row[1])
        netchange = int(row[1]) - previousnet

        previousnet = int(row[1])
        netchangelist += [netchange]
        monthofchange += [row[0]]

        
        if netchange > greatestincrease[1]:
            greatestincrease[0] = row[0]
            greatestincrease[1] = netchange
            
        if netchange < greatestdecrease[1]:
            greatestdecrease[0] = row[0]
            greatestdecrease[1] = netchange

netmonthlyaverage = sum(netchangelist) / len(netchangelist)

output = (
    f"Financial Analysis\n"
    f"-------------------\n"
    f"Total Months: {totalmonths}\n"
    f"Total Net: {totalnet}\n"
    f"Net Monthly Average: {netmonthlyaverage}\n"
    f"Greatest Increase: {greatestincrease[0]} (${greatestincrease[1]}) \n"
    f"Greatest Decrease: {greatestdecrease[0]} (${greatestdecrease[1]}) \n"

) 
print(output)

with open(outputbank_txt, 'w') as txt_file:
    txt_file.write(output)
