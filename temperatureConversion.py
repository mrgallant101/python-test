# this is a method that accept the value to be converted and unit
# the round function approximate the value to 2 d.p
def temperature_converter(tem_value, type):
    if type == "farhrenheit":
        return round(tem_value * (100/ 212), 2)
    elif type == "kelvin":
        return round(tem_value - 273.15, 2)
    else:
        print("You enter an invalid temperature unit\n NB:Check your spellings")


temp = float(input("Enter the value you want to convert: "))
unit = input("Enter the unit of the value you want to convert, choose 'farhrenheit' or 'kelvin' :").lower()
print(f"The temperature of {temp} in {unit} is {temperature_converter(temp, unit)} in Celcius")






