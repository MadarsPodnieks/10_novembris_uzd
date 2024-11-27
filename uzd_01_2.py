# Izveidot programmu, kura prasa lietotâjam ievadît cilindra râdiusu un tâ augstumu, tiek aprçíinâts cilindra laukums un tilpums. Rezultâts tiek parâdîts konsolç.
# tilpums = 3.14 * râdiuss * râdiuss * augstums
# laukums = 2 * (3.14 * râdiuss * râdiuss) + augstums * (2 * 3.14 * râdiuss)
import math
pi=math.pi
radius=int(input("ievadi cilindra rādiusu:"))
h=int(input("ievadi cilindra augstumu:"))
tilpums= pi*radius *h
laukums=2* pi*radius**2 +h *2*pi *radius
print(f"Cilindra laukums ir {laukums:.3f}, bet tilpums ir {tilpums:.3f}")




