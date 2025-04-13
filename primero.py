print("Hola!, este es el primer archivo del porgrama")

nums = []

while True:
    num = input("Introduce número (Enter para salir):\n")
    if len(num) > 0:
        try:
            num = int(num)
            if num not in nums:
                nums.append(num)
            else:
                print("Este número ya está en la lista.")
        except:
            print("Esto no es un número")
    else:
        break

nums.sort()
print("Números ordenados de menor a mayor")
print(nums)
