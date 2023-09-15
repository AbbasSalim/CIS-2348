# Abbas Salim
# 2026396

oil_change = 35
tire_ro = 19
car_wash = 7
car_wax = 12
print(f"Davy's auto shop services")
print(f'Oil change -- ${oil_change}')
print(f'Tire rotation -- ${tire_ro}')
print(f'Car wash -- ${car_wash}')
print(f'Car wax -- ${car_wax}\n')
first_service = input("Select first service:\n")
second_service = input("Select second service:\n\n")
print(f"Davy's auto shop invoice\n")
if first_service == 'Oil change':
    print(f'Service 1: {first_service}, ${oil_change}')
elif first_service == 'Tire rotation':
    print(f'Service 1: {first_service}, ${tire_ro}')
elif first_service == 'Car wash':
    print(f'Service 1: {first_service}, ${car_wash}')
elif first_service == 'Car wax':
    print(f'Service 1: {first_service}, ${car_wax}')
else:
    print(f'Service 1: No service')
if second_service == 'Oil change':
    print(f'Service 2: {second_service}, ${oil_change}\n')
elif second_service == 'Tire rotation':
    print(f'Service 2: {second_service}, ${tire_ro}\n')
elif second_service == 'Car wash':
    print(f'Service 2: {second_service}, ${car_wash}\n')
elif second_service == 'Car wax':
    print(f'Service 2: {second_service}, ${car_wax}\n')
else:
    print(f'Service 2: No service\n')
if first_service == 'Oil change' and second_service == 'Tire rotation':
    total = oil_change + tire_ro
elif first_service == 'Oil change' and second_service == 'Car wash':
    total = oil_change + car_wash
elif first_service == 'Oil change' and second_service == 'Car wax':
    total = oil_change + car_wax
elif first_service == 'Oil change' and second_service == '-':
    total = oil_change
elif first_service == 'Tire rotation' and second_service == 'Oil change':
    total = tire_ro + oil_change
elif first_service == 'Tire rotation' and second_service == 'Car wash':
    total = tire_ro + car_wash
elif first_service == 'Tire rotation' and second_service == 'Car wax':
    total = tire_ro + car_wax
elif first_service == 'Tire rotation' and second_service == '-':
    total = tire_ro
elif first_service == 'Car wash' and second_service == 'Oil change':
    total = car_wash + oil_change
elif first_service == 'Car wash' and second_service == 'Tire rotation':
    total = car_wash + tire_ro
elif first_service == 'Car wash' and second_service == 'Car wax':
    total = car_wash + car_wax
elif first_service == 'Car wash' and second_service == '-':
    total = car_wash
elif first_service == 'Car wax' and second_service == 'Oil change':
    total = car_wax + oil_change
elif first_service == 'Car wax' and second_service == 'Tire rotation':
    total = car_wax + tire_ro
elif first_service == 'Car wax' and second_service == 'Car wash':
    total = car_wax + car_wash
elif first_service == 'Car wax' and second_service == '-':
    total = car_wax
elif first_service == '-' and second_service == 'Car wax':
    total = car_wax
else:
    total = 0
print(f'Total: ${total}')
