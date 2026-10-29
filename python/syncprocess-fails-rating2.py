import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import PatternFill
from openpyxl.utils.dataframe import dataframe_to_rows

# File paths for the two CSV files
failed_file = "Report-2oct_10oct-Failed.csv"
all_operations_file = "Report-2oct_10oct-all_operations_status.csv"

# Read the data from the CSV files
df_failed = pd.read_csv(failed_file, delimiter=',')
df_all = pd.read_csv(all_operations_file, delimiter=',')

# Merge the dataframes based on the "OPERATION_NAME" column
merged_df = df_all.merge(df_failed, on="OPERATION_NAME", how="left", suffixes=("_all", "_failed"))

# Fill missing values in the "OPERATION_COUNT_failed" column with 0
merged_df["OPERATION_COUNT_failed"] = merged_df["OPERATION_COUNT_failed"].fillna(0)

# Calculate the percentage of failing for each operation
merged_df["Failure Percentage"] = (merged_df["OPERATION_COUNT_failed"] / merged_df["OPERATION_COUNT_all"]) * 100

# Create a new Excel workbook and add a worksheet
wb = Workbook()
ws = wb.active

# Write the data to the Excel worksheet
for r in dataframe_to_rows(merged_df, index=False, header=False):
    ws.append(r)

# Pre-define style objects to save memory and time
green_fill = PatternFill(start_color="00FF00", end_color="00FF00", fill_type="solid")
orange_fill = PatternFill(start_color="FFA500", end_color="FFA500", fill_type="solid")
red_fill = PatternFill(start_color="FF0000", end_color="FF0000", fill_type="solid")

# Apply conditional formatting based on the "Failure Percentage" column
for row in ws.iter_rows(min_row=1, max_row=ws.max_row, min_col=3, max_col=3):
    for cell in row:
        percentage = cell.value
        if percentage > 33:
            cell.fill = red_fill
        elif percentage > 10:
            cell.fill = orange_fill
        else:
            cell.fill = green_fill

# Save the Excel workbook with the provided file name
output_file = "Syncprocess_health_report_edited.xlsx"
wb.save(output_file)

