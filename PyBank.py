# Import modules
import os 
import csv

#Create variables and integrating the cvs data
Budget_Data_csv = os.path.join("/Users/Will/Documents/Instructions/PyBank/Resources/budget_data.csv")
Total_Month = 0
Total_Profit_Losses = 0
Previous_Profit_Losses = 0
Profit_losses_Change = 0
Profit_Loss_Change_List = []
Month_Change = []
Greatest_Increase = 0
Greatest_Decrease = 999999999999999

#With Loop through the data
with open(Budget_Data_csv) as Profit_Loss_Data:
    reader = csv.DictReader(Profit_Loss_Data)
    index = 0
    #Start For loop through the cvs reader to hold values in variables
    for row in reader: 
        if(index == 0):
            Total_Month+= 1
            Total_Profit_Losses = Total_Profit_Losses + int(row["Profit/Losses"])
            Month_Change = Month_Change + [row["Date"]]
            index= index + 1
            continue
        Total_Month = Total_Month + 1
        Total_Profit_Losses = Total_Profit_Losses + int(row["Profit/Losses"])
        Profit_losses_change = int(row["Profit/Losses"]) - Previous_Profit_Losses
        Profit_Loss_Change_List.append(Profit_losses_change)
        Previous_Profit_Losses = int(row["Profit/Losses"])
        Month_Change = Month_Change + [row["Date"]]

    #Creating Variables to hold the Greatest Increase and Decrease Values based on Max & Min.
    Greatest_Decrease = min(Profit_Loss_Change_List)
    Greatest_Increase = max(Profit_Loss_Change_List)

   #Using and Index to grab the value we need for the final print.
    Greatest_Decrease_Month = Profit_Loss_Change_List.index(Greatest_Decrease) + 1
    Greatest_Increase_Month = Profit_Loss_Change_List.index(Greatest_Increase) + 1 
    # Final Print of Results 
    print("Financial Analysis")

    print("------------------------")

    print(f"Total Months: {Total_Month}\n")

    print(f"Total Profit/Losess: ${Total_Profit_Losses}\n")

    print(f"Average Change: ${(round(sum(Profit_Loss_Change_List)/len(Profit_Loss_Change_List), 2))}")

    print(f"Greatest increase in Profits: {Month_Change[Greatest_Increase_Month]}(${(str(Greatest_Increase))})")

    print(f"Greatest decrease in Profits: {Month_Change[Greatest_Decrease_Month]}(${(str(Greatest_Decrease))})")

#Output Files
output_file = ("/Users/Will/Documents/Instructions/PyBank/Resources/Banking_summary.txt")

with open(output_file, "w", encoding = 'utf-8') as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("------------------------")
    file.write("\n")
    file.write(f"Total Months: {Total_Month}")
    file.write("\n")
    file.write(f"Total Profit/Losess: ${Total_Profit_Losses}")
    file.write("\n")
    file.write(f"Average Change: ${(round(sum(Profit_Loss_Change_List)/len(Profit_Loss_Change_List), 2))}")
    file.write("\n")
    file.write(f"Greatest increase in Profits: {Month_Change[Greatest_Increase_Month]}(${(str(Greatest_Increase))})")
    file.write("\n")
    file.write(f"Greatest decrease in Profits: {Month_Change[Greatest_Decrease_Month]}(${(str(Greatest_Decrease))})")
    file.write("\n")
