# File formats and using them in python

## XLSX
- excel proprietary format
- excel is good for data stroage

## CSV
- Simple plain text format
- Comma seperated values
- Each line in a CSV file represents a row of data
- Values in each row are seperated bo commas, with each value representign a colum in that row. 
- CSV files can be opened and editied in text editors or spreadsheet software
- Widely compatible across platforms and applications, supporting seamless data exchanges
- Example:
  - ```csv
    Name,Age,City
    Alice,28,New York,
    Bob,35,San Francisco
- Note: Saving a file as a CSV in Excel only saves on sheet at a time
- Saving an Excel file as a csv: figure it out im not writing this down.
  - Saving as a CSV won't save formatting and should not be used for storage of excel sheets

## Open and use it in python
```python
import csv

with open("file.csv", "r") as file_object:
    data_reader = csv.reader(file_object)
    for row in data_reader:
        print(row)
```
- in this example, data_reader is a special object
- The data isn't there until it is actually needed
  - However, you can also specify that you want everything at once.
  - See example 2 of `examples.py`
- Each row is a list of strings representing one line in the csv file
  - See example 1 of `examples.py` for examples on this

## Writing data to csv from python

```python
import csv

data = [
  ['name', 'age', 'city'],
  ['David', '31', 'Boston'],
  ['Eva', '29', 'Miami']
]

with open('new_data.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)
```
- See example 3 in `examples.py`
- Writes each inner list as a row in the file
- ```python
  row = ['columnData', 'columnData']
  data = [row, row, row]
- This is something
## What about DictReader?
- We haven't used it yet
- Despite it being a good tool, we can just ignore it (nice)

## Python's strengths in Data Processing
- Versatility
- Rich Ecosystem
- Ease of Use
- Automation Capabilities
- Data integration
- Enhanced Functionality 
- Workflow Automation
- Excel Automation
- Database Interactions

## Python and MS Access
- I don't even know anymore
- 