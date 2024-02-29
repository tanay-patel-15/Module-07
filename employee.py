import csv
from datetime import datetime

class Employee():
  def  __init__(self, name, rateOfPay):
    self.name = name
    self.rateOfPay = rateOfPay
    self.next = None

  def process(self):
    with open('hours.csv', "r") as fromFile:
      reader = csv.reader(fromFile)
      for row in reader:
        current = self
        while current.name != row[0] and current != None:
          current = current.next
        if current != None:
          hours = float(row[1]) 
          if hours > 40:
            gross = current.rateOfPay * 1.5 * (40 - hours) +  current.rateOfPay * hours
          else:
            gross = current.rateOfPay * hours
          with open(f"{current.name}.txt", 'w') as toFile:
            toFile.write("\t\t\t\t\t" + str(datetime.today()) + "\n")
            toFile.write(f"Pay to the order of { current.name } \n")
            toFile.write(f"Amount: { gross } \n")
        
        else:
          print("We hit the null pointer, we're done.")


  def push(self):
    with open ("emp_data.csv", 'r') as fromFile:
      reader = csv.reader(fromFile)
      for row in reader:
        name = row[0]
        rateOfPay = row[1]
        emp = Employee(name, float(rateOfPay))
        current = self
        while (current.next!=None):
          current=current.next
        current.next = emp

  def __repr__(self):
    represent = ' '
    current = self
    while current != None:
      represent += f" { current.name } makes $ { current.rateOfPay } \n"
      current = current.next
    return represent


if  __name__ == "__main__":
  e = Employee("Boss", 0.00)
  e.push()
  print(e)
  e.process()