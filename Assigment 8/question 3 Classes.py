class Temperature:
    def __init__(self,temp):
        self.temp=temp

    def tocelsius(self,frah):
        x=(frah-32)*(5/9)
        print("Celsius : ",x)

    def toFahrenheit(self,cel):
        x=(cel*(9/5))+32
        print("Fahrenheit : ",x)

my_temp=Temperature(60)
my_temp.tocelsius(60)
my_temp.toFahrenheit(15.55)
