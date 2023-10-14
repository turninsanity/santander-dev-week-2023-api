import csv

with open('exemplo.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    
    headers = next(csvreader)
    
    print(f"{headers[0]:<10} {headers[1]:<6} {headers[2]:<25} {headers[3]}")
    
    for row in csvreader:
        print(f"{row[0]:<10} {row[1]:<6} {row[2]:<25} {row[3]}")
