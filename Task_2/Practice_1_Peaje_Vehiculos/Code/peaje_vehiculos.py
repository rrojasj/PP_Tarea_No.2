from ph_functions import *

cant_vehics = int(input("\nIngrese la cantidad de vehículos:\n"))

total_avg = 0
total_earn = 0
i = 0

while i < cant_vehics:
      vehic_line = int(input("\nSeleccione el carril de vehículo:\n1. Automovil  - ₡75.00\n2. Taxi/Bus   - ₡100.00\n3. Camión     - ₡200.00\n"))
      
      if vehic_line == 1:
          print("\n- Carril de Automóviles")
          amount_vehic = 75
          
      elif vehic_line == 2:
          print("\n- Carril de Buses & Taxis")
          amount_vehic = 100
    
      elif vehic_line == 3:
          print("\n- Carril de Camiones")
          amount_vehic = 200

      peak_hr = int(input("\nEs hora pico?\n1. Si   2. No\n"))

      if peak_hr == 1:
           disc = 20
           amount_vehic = calc_disc_amount(amount_vehic, disc)

      else:
            volunteer = int(input("\nDesea ingresar al carril voluntario?:\n1. Si   2. No\n"))
            if volunteer == 1:
                disc = 15
                amount_vehic = calc_volunt_amount(amount_vehic, disc)
      
      print(f"Este vehículo paga de peaje: ₡{amount_vehic}\n")

      total_earn = calc_total(total_earn, amount_vehic)

      i += 1

total_avg = calc_avg(total_earn, i)

print(f'El total de ingresos es de: {total_earn}\n')
print(f'El promedio total es de: {total_avg}\n')
print(f'Gracias por utilizar el sistema de peajes.\n')


            
