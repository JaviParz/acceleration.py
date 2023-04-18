initial_speed = float(input("Введите начальную скорость в км/ч: "))
final_speed = float(input("Введите конечную скорость в км/ч: "))
time = float(input("Введите время движения в секундах: "))

initial_speed_mps = initial_speed / 3.6
final_speed_mps = final_speed / 3.6

acceleration = (final_speed_mps - initial_speed_mps) / time

print("Ускорение: {:.2f} м/с^2".format(acceleration))
