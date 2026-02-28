class LogicGate:
    def __init__(self, nome_porta):
        self.nome = nome_porta
        self.output = None

    def getNome(self):
        return self.nome
    
    def getOutput(self):
        self.output = self.realiza_logica()
        return self.output
    
class BinaryGate(LogicGate):
    def __init__(self, nome_porta):
        super().__init__(nome_porta)
        self.pinoA = None
        self.pinoB = None

    def getPinoA(self):
        if self.pinoA == None:
            return self.setPinoA()

        return self.pinoA
    
    def getPinoB(self):
        if self.pinoB == None:
            return self.setPinoB()

        return self.pinoB
    
    def setPinoA(self):
        return int(input('Digite a entrada do Pino A (0 ou 1): '))
    
    def setPinoB(self):
        return int(input('Digite a entrada do Pino B (0 ou 1): '))
    
class UnaryGate(LogicGate):
    def __init__(self, nome_porta):
        super().__init__(nome_porta)
        self.pinoA = None

    def getPinoA(self):
        if self.pinoA == None:
            return self.setPinoA()

        return self.pinoA
    
    def setPinoA(self):
        return int(input('Digite a entrada do Pino A (0 ou 1): '))

class ANDGate(BinaryGate):
    def __init__(self, nome_porta):
        super().__init__(nome_porta)

    def realiza_logica(self):
        a = self.getPinoA()
        b = self.getPinoB()

        if a == 1 and b == 1:
            return 1
        else:
            return 0
        
class ORGate(BinaryGate):
    def __init__(self, nome_porta):
        super().__init__(nome_porta)

    def realiza_logica(self):
        a = self.getPinoA()
        b = self.getPinoB()

        if a == 1 or b == 1:
            return 1
        else:
            return 0
        
class NOTGate(UnaryGate):
    def __init__(self, nome_porta):
        super().__init__(nome_porta)

    def realiza_logica(self):
        a = self.getPinoA()

        if a == 1:
            return 0
        else:
            return 1
