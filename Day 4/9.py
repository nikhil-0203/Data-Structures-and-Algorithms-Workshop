f1=open("monkey-d-luffy-red-5120x2880-24473.png","rb")
f2=open("luffy.png","wb")
data = f1.read()
f2.write(data)
print("New image is available with the name:")
import csv
f = open("myfile.csv", "a",newline="")
a = csv.writer(f)
a.writerow(["Student_id","Name","Roll_no"])
a.writerow([1,"Nikhil",7])
a.writerow([2,"Harshad",8])
a.writerow([3,"Utkarsh",9])
a.writerow([4,"Atharv",10])
a.writerow([5,"Ganesh",11])
a.writerow([6,"Sakharam",12])
f.close 

