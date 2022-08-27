
Hours = input("Enter Hours: ")
Rate = input("Enter Rate: ")

if int(Hours) <= 40:
  def computePay(Hours, Rate):
    Wages = int(Hours) * int(Rate)
    return Wages
  cont = computePay(Hours, Rate)
  print("Pay: " + str(cont))

else:
  overhours = int(Hours) - 40
  def computepay(overhours, Rate):
    Wages = (int(overhours) * int(Rate) * 1.5) + (40 * int(Rate))
    return Wages
  cont = computepay(overhours, Rate)
  print("Pay: " + str(cont))
