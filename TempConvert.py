#TempConvert.py
#Name: Jacob Oetken
#Date: 2/8/25
#Assignment: TEMPERATURE CONVERSION LAB 3


def main():
  #ask for input
  tempF = float(input("Please enter a temperature in Farenheit: ")) #used float to allow partial degrees
  #convert input
  tempC = (tempF - 32) * 5 / 9 #f-c = (32°F − 32) × 5/9 = 0°C
  #round to .1
  tempC = round(tempC, 1)
  #display output showing f is c
  print(f"{tempF} degrees Fahrenheit is {tempC} degrees Celsius.") #fstring is easier to add 2 or more variables


if __name__ == '__main__':
  main()
