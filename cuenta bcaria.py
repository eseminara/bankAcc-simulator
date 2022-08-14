class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
    

class Cliente(Persona):
    def __init__(self,nombre,apellido,numero_cuenta,balance = 0):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
    
    def __str__(self):
        return f'--Datos Cliente--:\n Nombre: {self.nombre}\n Apellido: {self.apellido}\n Nro Cuenta: {self.numero_cuenta}\n Balance:{self.balance}'.upper()
    
    def depositar (self,deposito):
        self.deposito = deposito
        self.balance+= deposito
        return f'Has depositado {self.deposito} en tu cuenta.\nEl balance de tu cuenta es: {self.balance}'

    def retirar (self,retiro):
        self.retiro = retiro
        self.balance-= retiro
        if retiro > self.balance:
            self.balance+= retiro
            print ('La cantidad es incorrecta')
        else:
            return f'Has retirado {self.retiro} de tu cuenta'
    
        
        
def crear_cliente():
    nombre_cl = input ('Nombre: ')
    apellido_cl = input ('Apellido: ')
    nro_cuenta = input ('Cta: ')
    cliente = Cliente(nombre_cl,apellido_cl,nro_cuenta)
    
    return cliente
    

    
def inicio():
    print(f'Bienvenido')
    mi_cliente = crear_cliente()
    print(mi_cliente)
    
    while True:
        print('Que operacion desea realizar?:')
        print('1-Depositar\n2-Retirar\n3-Consultar balance\n4-Salir')
        eleccion = input('>: ')
        if eleccion == '1':
            deposito = int(input('Ingrese el monto que desea depositar: '))
            mi_cliente.depositar(deposito)
            print('Balance de cuenta es,',mi_cliente.balance)
        elif eleccion == '2':
            retiro = int(input('Ingrese el monto que desea retirar: '))
            mi_cliente.retirar(retiro)
            print('Balance de cuenta es,',mi_cliente.balance)
        elif eleccion == '3':
            print('Balance de su cuenta: ',mi_cliente.balance)
        elif eleccion == '4':
            print('---HASTA LUEGO---')
            break
        else:
            print('Opciones incorrecta')
            
            
inicio()