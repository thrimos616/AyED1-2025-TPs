encabezado = ["nombre", "legajo", "fecha"]

empleados = [

    ["Juan Perez", "12345", "15/03/1990"]
    ["Maria Garcia", "54321", "22/07/1985"]
    ["Carlos Lopez", "67890", "10/11/1992"]
    ["Ana Martinez", "09876", "05/01/1988"]
    ["Luis Rodriguez", "11223", "30/09/1995"]

]

salida = [[par_de_datos for par_de_datos in zip(encabezado, empleado)] for empleado in empleados if int(empleado[1]) > 20000] 

