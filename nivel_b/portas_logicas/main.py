from portas_logicas import *

porta_and = ANDGate("Porta 1")
print(f'Saída AND: {porta_and.getOutput()}\n')

porta_or = ORGate("Porta 2")
print(f'Saída OR: {porta_or.getOutput()}\n')

porta_not = NOTGate("Porta 3")
print(f'Saída NOT: {porta_not.getOutput()}')