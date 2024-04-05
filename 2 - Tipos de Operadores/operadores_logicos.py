saldo = 1000
saque= 200
limite = 100

# (and) Operador 'e'
saldo >= saque and saque <= limite

# (or) Operador 'ou'
saldo >= saque or saque <= limite

# (not) Operador 'negação'
# Porque 'not contatos_emergencia' é true?
# R:'contatos_emergencia = []' é uma lista. Lista vazia em python é falso
contatos_emergencia = []
not 1000 > 1500
not contatos_emergencia
not "saque 1500;"
not ""

# PARENTESES
# Coloquei 'P' no final das variaveis para facilitar
# entendimento e englobar tudo na mesma pagina sem divergir
# resultados das explicações 
saldoP = 1000
saqueP = 250
limiteP = 1000
conta_especial = True

saldoP >= saqueP and saqueP <= limite or conta_especial and saldoP >= saque
(saldoP >= saqueP and saqueP <= limite) or (conta_especial and saldoP >= saque)