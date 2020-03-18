# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
#cwb_filename = 'sample_input.csv'
cwb_filename = '106061246.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
stations = ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']
target_data = []
for s in stations:
    temp_data = list(filter(lambda item: item['station_id'] == s, data))
    n=0
    mean=0.0
    for i in range(len(temp_data)):
        if float(temp_data[i]['PRES']) > 0:
            n+=1
            mean+=float(temp_data[i]['PRES'])
    if n != 0:
        mean=mean/n
        target_data.append([s, mean])
    else:
        target_data.append([s, 'None'])
#=======================================

# Part. 4
#=======================================
# Print result
print(target_data)
#========================================