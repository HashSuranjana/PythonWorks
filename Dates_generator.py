import calendar
file = open("calendar.txt","w")
for i in range(1,13):
    file.write(calendar.month(2023,i))
    file.write("\n" "\n")
file.close()
