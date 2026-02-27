class ContoBancario:
    def __init__(self,saldo):
        self._saldo=saldo
    def deposita(self,importo):
        if importo > 0:
            self._saldo+=importo
    def preleva(self,importo):
        if 0 < importo <self._saldo:
            self._saldo-=importo
    def mostra_saldo(self):
        return self._saldo
conto_di_ciccio = ContoBancario(1000)
conto_di_ciccio.deposita(100)
print(conto_di_ciccio._saldo)

conto_di_ciccio.preleva(300)
print(conto_di_ciccio._saldo)
print(conto_di_ciccio.mostra_saldo())
print(conto_di_ciccio.mostra_saldo())