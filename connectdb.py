import csv
import sqlite3


# open the connection to the database
conn = sqlite3.connect('elecVehicle.db')
cur = conn.cursor()

# drop the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS VehicleRegistration')
print("table dropped successfully");

# create table again
conn.execute('CREATE TABLE VehicleRegistration (Vehicle_ID TEXT PRIMARY KEY,  Year INTEGER, Company TEXT, Model TEXT, Vehicle_Type TEXT)')
print("table created successfully");

# open the file to read it into the database
with open('ElectricVehical/ElectricVehiclePopulationData.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        print(row)

        Vehicle_ID = row[13]
        Year = int(row[5])
        Company = row[6]
        Model = row[7]
        Vehicle_Type = row[8]
        
        cur.execute('INSERT INTO VehicleRegistration VALUES (?,?,?,?,?)', (Vehicle_ID, Year, Company, Model, Vehicle_Type))
        conn.commit()


# drop the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS VehicleAddress')
print("table dropped successfully");

# create table again
conn.execute('CREATE TABLE VehicleAddress (Idnum INTEGER PRIMARY KEY AUTOINCREMENT,Vehicle_ID TEXT, County TEXT, City TEXT, State TEXT, PostalCode TEXT)')
print("table created successfully");

# open the file to read it into the database
with open('ElectricVehical/ElectricVehiclePopulationData.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        print(row)

        Vehicle_ID = row[13]
        County = row[1]
        City = row[2]
        State = row[3]
        PostalCode = row[4]
        
        cur.execute('INSERT INTO VehicleAddress VALUES (NULL,?,?,?,?,?)', (Vehicle_ID, County, City, State, PostalCode))
        conn.commit()

print("data parsed successfully");
conn.close()



        