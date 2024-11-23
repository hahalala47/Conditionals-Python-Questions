weather_condition = input("please enter the condition of weather:\n-Sunny \n-Rainy \n-Snowy \n \n:")
weather_condition.lower()
weather_condition.upper()
weather_condition.strip()
weather = str(weather_condition)


if weather== "Sunny":
    activity = "Go for a walk"
elif weather == "Rainy":
    activity = "Read a book"
elif weather == "Snowy":
    activity = "Build a snowman"
else:
    activity = "Do whatever you want"
print(activity)
exit()

