# 7) WAP to enter time in minutes and print it in hours and minutes.
minutes = int(input("Enter time in minutes: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print("Hours =", hours)
print("Minutes =", remaining_minutes)