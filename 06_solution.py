distance = 5

if distance < 3:
     transport = "Walk"
elif distance <= 15:
     transport = "Bike"
else:
     transport = "Car"
     
print("AI recommmends you the transport of:", transport)