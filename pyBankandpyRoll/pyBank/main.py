""""Analyzing financial records
"""
## PyBank main.py
#This little python script is for analyzing the financial records of your company.
#Unfortuneately, we have been supposedly restricted to not using pandas so google is not helpful today.  
#Setting up:
import os
import csv
""""
The dataset is composed of two columns: 
`Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards 
#for accounting so the records are simple.). Yay. Much rejoicing and little clean-up.
"""
#Data path is to financial data called [budget_data.csv](PyBank/Resources/budget_data.csv).

trade_csv = os.path.join('budget_data.csv')
#Setup for reader of csv file and start a list of cell values for c1, the date column
with open(trade_csv, "r") as csv_file:
    c1 = []
#Split the data on commas since that is your delimiter
    csvreader = csv.reader(csv_file, delimiter=',')
#Reset
    total = 0
    months = 0
#File has column headers to skip and not included. Use the next row data.
    header = next(csvreader)
#Use a For Loop to go down along rows
    for row in csv.reader(csv_file):
#Append to list
        c1.append(row[1])
#Calculate total profit/loss 
        total = total + (int(row[1]))
#and how many months included in dataset.
        months = months + 1
        #alternative way to find total months:
            #months=len(list(csv.reader(open('budget_data.csv'))))-1
            
#Setup for reader of csv file and start a list of cell values for c2, the profit/loss column. Repeated for clarity.
with open(trade_csv, "r") as csv_file:
#Split the data on commas since that is your delimiter
    csvreader = csv.reader(csv_file, delimiter=',')
#File has column headers to skip and not included. Use the next row data.
    header = next(csvreader)
#Start a new list for cell values in second column   
    c2 = []
#Zip 
    for x, y in zip(c1, c1[1:]):
#File has column headers to skip and not included. Use the next row data.
        header = next(csvreader)
#Append the integers in the list
        c2.append(int(x) - int(y))
#Calculate the average from the total divided by the number of months previously calculated in c1 list
        total_change = sum(c2)
        average = total_change / months
#The greatest increase or decrease in profits (date and amount) over the entire period
greatest_increase = max(c2)
greatest_decrease = min(c2)

##Test print of maths
print("Financial Analysis")
print("------------------------")
print("Total months: " + str(months))
print("Total volume: " + str(total))
#The average change in "Profit/Losses" between months over the entire period
print("Average monthly change: "+ str(average))
#The greatest increase in profits (date and amount) over the entire period
print("Greatest increase: " + str(greatest_increase))
#The greatest decrease in losses (date and amount) over the entire period
print("Greatest decrease: " + str(greatest_decrease))

##Output to text file
text_file = open("PYBankFinancials.txt", "w")
text_file.write("Financial Analysis\n")
text_file.write("------------------------\n")
text_file.write("Total months: " + str(months) + "\n")
text_file.write("Total volume: " + str(total) + "\n")
text_file.write("Average monthly change: " + str(average) + "\n")
text_file.write("Greatest increase: " + str(greatest_increase) + "\n")
text_file.write("Greatest decrease: " + str(greatest_decrease) + "\n")
text_file.close()


