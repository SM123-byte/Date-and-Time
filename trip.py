def hotel_cost(nights):
    return 150*nights

def plane_ride(city):
    if "London" == city: 
        return 340
    elif "Tokyo" == city:
        return 500
    elif "LA" == city:
        return 410
    elif "New Delhi" == city:
        return 300

def rental_car(days):
    if days >= 7:
        return 40 * days - 50
    elif days >= 3:
        return 40 * days - 20
    else:
        return 40 * days
    
def trip_cost(city, days, spending_money):
    return rental_car(days) + plane_ride(city) + hotel_cost(days) + spending_money

print(f"Cost of car rental: {rental_car(10)}")
print(f"Cost of plane ride: {plane_ride("Tokyo")}")
print(f"Cost of hotel: {hotel_cost(10)}")

print("Total cost: ", trip_cost("LA", 7, 6000))