#Import module
from HEPAK_API import HEPAK

#Initialize Helium object
Helium = HEPAK()

#Example: Evaluate density in single state
T=5
p=1e5
rho = Helium.rho(T,p)

print(f'Helium rho(T = {T} K, p = {p} Pa) = {rho} kg/m3')
print()

#Example: Evaluate heat capacity at constant pressure for vector like argument

T = [5, 5.1, 5.2, 5.3, 5.4, 5.5]
p = [1e5, 1e5, 1e5, 1e5, 1e5, 1e5]
cp = Helium.cp(T,p)

print(f'Vector of cp is {cp}')
print()
