walkedDays = input("Enter your walked days")
userSteps = input("Enter your steps walked")
oneMilePerSteps = 2000
oneMilePerCalories = 65
allMiles = walkedDays * (userSteps / oneMilePerSteps)
burnCalories = allMiles * oneMilePerCalories
print "User walked ", allMiles, " miles and the calories lost is ", burnCalories
