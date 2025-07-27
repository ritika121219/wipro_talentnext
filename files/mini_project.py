#project1. create apython program that asks the user how far they want to travel.if they want to travel less than three miles tell them to ride bicycle. if they want to travel more than three miles,but less than three hundred miles, tell them to ride Motor-cycle . if they want to travel three hudred miles or more tell them to driver super-car.

distance = float(input("How far do you want to travel (in miles)? "))

if distance < 3:
    print("You should ride a bicycle.")
elif distance < 300:
    print("You should ride a motorcycle.")
else:
    print("You should drive a super-car.")

#project2. Lets assume you are planning to use your python skills to build a PBLApp for mobile .you decide to host your application on servers running in the cloud . you pick a hosting provider that charges $0.51 per hour. you will launch your service using one server and want to know how much it will cost to operate per day,per week ,per month.
#WAP that display the ans. to following.
#how much does it cost to operate one server per day?
#how much does it cost to operate one server per week?
#how much does it cost to operate one server per month?
#how much does it cost to operate one server with $918?

cost_per_hour = 0.51
cost_per_day = cost_per_hour * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30
budget = 918
hours_affordable = budget / cost_per_hour


print("Cost to operate one server:")
print(f"Per day   : ${cost_per_day:.2f}")
print(f"Per week  : ${cost_per_week:.2f}")
print(f"Per month : ${cost_per_month:.2f}")
print(f"With $918, you can run the server for {hours_affordable:.2f} hours.")
