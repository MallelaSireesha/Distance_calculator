
def calculate_distance(speed, time):
    return speed * time

speed = float(input("Enter speed"))
time = float(input("Enter Time"))

distance = calculate_distance(speed, time)
print(distance)