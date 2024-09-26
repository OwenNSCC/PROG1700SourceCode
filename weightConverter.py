print("Imperial To Metric Conversion")

Tons = int(input("Enter the number of tons: "))
Stone = int(input("Enter the number of stone: "))
Pounds = int(input("Enter the number of pounds: "))
Ounces = float(input("Enter the number of ounces: "))

totalOunces = (35840 * Tons) + (224 * Stone) + (16 * Pounds) + Ounces
totalKilos = totalOunces / 35.274
metricTons = int(totalKilos/1000)

remainingKilos = totalKilos - (metricTons * 1000)
grams = (remainingKilos - int(remainingKilos)) * 1000



print(f"The metric weight is: {metricTons} metric tons, {int(remainingKilos)} kilograms, and {grams:.1f} grams.")