print("Hipster's Local Vinyl Records - Customer Order Details")

deliveryRatePerKm = 15
salesTaxRate = 0.14

cusName = input("Enter the customer's name: ")
totalKilometers = float(input("Enter the distance in kilometers for delivery: "))
recordCost = float(input("Enter the cost of the records purchased: "))

deliveryCost = totalKilometers * deliveryRatePerKm
taxOnRecords = recordCost * salesTaxRate
totalRecordCost = recordCost + taxOnRecords
totalCost = totalRecordCost + deliveryCost

print("Purchase summary for {}".format(cusName))
print("Delivery Cost: ${:.2f}".format(deliveryCost))
print("Purchase Cost: ${:.2f}".format(totalRecordCost))
print("Total Cost: ${:.2f}".format(totalCost))
