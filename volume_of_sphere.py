def calculate_volume_of_sphere(radius):
  pi = 3.14
  volume = (4/3)*pi*(radius*radius*radius)
  return volume

radius = 30 
volume1 = calculate_volume_of_sphere(radius)
print(f"Volume of sphere with radius {radius} is {volume1}")

radius = 40 
volume2 = calculate_volume_of_sphere(radius)
print(f"Volume of sphere with radius {radius} is {volume}")

