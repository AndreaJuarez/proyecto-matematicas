numerouno = float(input('Ingrese el primer número:'));
numerodos = float(input('Ingrese el segundo número:'));

multiplicacion = numerouno * numerodos;

resultado = print('El resultado de la multiplicación es: ' + str(multiplicacion));

# archivo-entrada.py
print('Abriendo banner con nuestros datos:')
f = open ('banner.txt','r')
mensaje = f.read()
print(mensaje)

"""
                     _                       _                            __  __    
     /\             | |                     | |                          |  \/  |   
    /  \   _ __   __| |_ __ ___  __ _       | |_   _  __ _ _ __ ___ ____ | \  / |   
   / /\ \ | '_ \ / _` | '__/ _ \/ _` |  _   | | | | |/ _` | '__/ _ \_  / | |\/| |   
  / ____ \| | | | (_| | | |  __/ (_| | | |__| | |_| | (_| | | |  __// /  | |  | |_  
 /_/    \_\_| |_|\__,_|_|  \___|\__,_|  \____/ \__,_|\__,_|_|  \___/___| |_|  |_(_) 
  __ ______ __  ___  __ __  ___ ____   ___  _  _                                    
 /_ |____  /_ |/ _ \/_ /_ |/ _ \___ \ / _ \| || |                                   
  | |   / / | | (_) || || | | | |__) | (_) | || |_                                  
  | |  / /  | |> _ < | || | | | |__ < \__, |__   _|                                 
  | | / /   | | (_) || || | |_| |__) |  / /   | |                                   
  |_|/_/    |_|\___/ |_||_|\___/____/  /_/    |_|                                   

"""