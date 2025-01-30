#FutureTime.py
#Name: Kyle Fayram
#Date: 1/30/25
#Assignment: lab2

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 6)
  currentMinute = now.minute
  
  #TODO:
  #Ask user for hours
  moreHour = int(input("How many hours in the future would you like to go? "))
  #Ask user for minutes
  moreMinute = int(input("How many minutes in the future would you like to go? "))
  #Calculate the time after the user-supplied time has passed.
  futureHours = (currentHour + moreHour) % 24
  futureMins = (currentMinute + moreMinute) % 60
  extraHour = (currentMinute + moreMinute) // 60

  print("Current time is: ")
  print(currentHour, currentMinute)
  print("Future time will be:")
  print(futureHours + extraHour, futureMins)

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()
