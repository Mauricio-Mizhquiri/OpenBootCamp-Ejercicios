paises = input('Ingrese una lista de paises separados por una ",": ')
cities = sorted((set(paises.split(","))))
paises = ','.join(cities)    
print(paises)

