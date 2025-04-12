c = 299792458

def main ():
     mass_in_kg = float(input("Enter kilos of mass: "))
     energy = mass_in_kg *(c**2)
     print("e = m * C^2...")
     print("m = " + str(mass_in_kg) + " kg")
     print("C = " + str(c) + " m/s")
     print(str(energy) + " joules of energy!")

if __name__ == '__main__':
  main()