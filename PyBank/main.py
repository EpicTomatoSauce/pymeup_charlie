#import csv file
import os
import csv

dirname = os.path.dirname(__file__)
pybank_csv = os.path.join(dirname,"..", "Resources", "PyBank_Resources_budget_data.csv")

#define list variables    
month = []
pnl = []
#pnl_diff = [] not required as list is created again pnl list below

with open(pybank_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)

#generate lists
    for row in csvreader:
        month.append(row[0])
        pnl.append(row[1])

        #convert pnl list to integers
        pnl = [int(value) for value in pnl]
        #calculate differentials in the pnl list and create a new list
        pnl_diff = [pnl[n] - pnl[n-1] for n in range(1, len(pnl))]

        
    #Average annual change calculation
    pnl_avg_change = sum(pnl_diff)/len(pnl_diff)

#Find maximum and minimum indexes in pnl_diff list
    max_value = max(pnl_diff)
    max_value_index = pnl_diff.index(max_value)+1 #add one to index as differential calculation starts on row 1 of dataset
    min_value = min(pnl_diff)
    min_value_index = pnl_diff.index(min_value)+1 #add one to index as differential calculation starts on row 1 of dataset

#create callable result function
financial_analysis = f'Financial Analysis\n-------------------------------\
    \nTotal Months: {len(month)}\
    \nTotal: ${sum(pnl)}\
    \nAverage Change: ${round(pnl_avg_change,2)}\
    \nGreatest Increase in profits: {month[max_value_index]} (${max_value})\
    \nGreatest Decrease in profits: {month[min_value_index]} (${min_value})'

print(financial_analysis)


output_file = os.path.join(dirname, "financial_analysis.txt")

with open(output_file, "w") as f:
    f.write(financial_analysis)


    #Original solution
    # print("Financial Analysis")
    # print("---------------------------------")
    # print(f"Total Months: {len(month)}")
    # print(f"Total: ${sum(pnl)}")
    # print(f"Average Change: ${round(pnl_avg_change,2)}")
    # print(f"Greatest Increase in profits: {month[max_value_index]} (${max_value})")
    # print(f"Greatest Decrease in profits: {month[min_value_index]} (${min_value})")

    #Original solution
    # f.write("Financial Analysis")
    # f.write("\n")
    # f.write("---------------------------------")
    # f.write("\n")
    # f.write(f"Total Months: {len(month)}")
    # f.write("\n")
    # f.write(f"Total: ${sum(pnl)}")
    # f.write("\n")
    # f.write(f"Average Change: ${round(pnl_avg_change,2)}")
    # f.write("\n")
    # f.write(f"Greatest Increase in profits: {month[max_value_index]} (${max_value})")
    # f.write("\n")
    # f.write(f"Greatest Decrease in profits: {month[min_value_index]} (${min_value})")
    # f.close()

# print(month[max_value_index]) #prints correct maximum month of pnl differential list
# print(month[min_value_index]) #prints correct minimum month of pnl differential list
# print(pnl_avg_change) #prints the correct average in the pnl differential list
# print(len(month)) #prints the correct number of months in data
# print(sum(pnl)) #prints the correct sum of values in pnl column




