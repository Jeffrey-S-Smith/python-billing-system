# module name: main 
import read
import purchase
import write

again = "Y"

while again.upper() == "Y":
    a = read.read_file()
    b = purchase.purchase(a)
    write.over_write(a,b)
    again = input("\n Is there any new customers waiting to buy product? ")
print("\nThank you for shopping from Pi on the Wall!")
print ("Please check ")