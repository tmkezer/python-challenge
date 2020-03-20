import os
import csv

count = 0
total = 0

values = []
date = []

with open("PyBank_data.csv", 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    for row in csvreader:
        #print(row)
        count = count + 1
        total = total + float(row[1])
        values.append(float(row[1]))
        date.append(row[0])

changes = [0] # adding first value to align dates and profit/loss changes (no change on first occurence)
total_changes = 0
for i in range(len(values) - 1):
    diff = values[int(i)+ 1] - values[int(i)]
    changes.append(diff)
    #print(diff)
    total_changes = total_changes + diff

    max_profit_date = str(date[changes.index(max(changes))])
    max_loss_date = str(date[changes.index(min(changes))])


print("Financial Analysis")
print("---------------------------")
print(f'Total Months: {count}')
print(f'Total Profit/Loss: ${total}')
print(f'Avg Monthly Profit/Loss Change: ${round(total_changes/(count -1),2)}')
print(f'Greatest Increase in Profits: {max_profit_date} (${max(changes)})')
print(f'Greatest Decrease in Profits: {max_loss_date} (${min(changes)})')


with open("Financial_Analysis.txt", "w") as f:
    print('Financial Analysis', file=f)
    print('--------------------------', file=f)
    print(f'Total Months: {count}', file=f)
    print(f'Total Profit/Loss: ${total}', file=f)
    print(f'Avg Monthly Profit/Loss Change: ${round(total_changes/(count -1),2)}', file=f)
    print(f'Greatest Increase in Profits: {max_profit_date} (${max(changes)})', file=f)
    print(f'Greatest Decrease in Profits: {max_loss_date} (${min(changes)})', file=f)
