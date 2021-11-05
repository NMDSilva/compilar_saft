import os
import xmltodict


class Compilar_SAFT():
    def __init__(self, pasta) -> None:
        self.pasta = pasta
        self.xml = None

    def substituir(self, texto):
        repl = "╢╟╡α╓Θσ╥"
        replc = "ÂÃÁÓÍÚÕÊ"
        for i in range(len(repl)):
            texto = texto.replace(repl[i], replc[i])
        return texto
    
    def todos_ficheiros(self):
        return [os.path.join(self.pasta, arquivo) for arquivo in os.listdir(self.pasta) if arquivo.lower().endswith(".xml")]

    def carregar_ficheiro(self, nomeFicheiro):
        ficheiro = open(nomeFicheiro, mode="r", encoding="cp437")
        daodosFicheiro = ficheiro.read()
        ficheiro.close()
        return xmltodict.parse(daodosFicheiro)

    def cliente_existe(self, idCliente):
        for cliente in self.xml["AuditFile"]["MasterFiles"]["Customer"]:
            if cliente["CustomerID"] == idCliente:
                return True
        return False
    
    def juntar_clientes(self, clientes):
        for cliente in clientes:
            if not self.cliente_existe(cliente["CustomerID"]):
                self.xml["AuditFile"]["MasterFiles"]["Customer"].append(cliente)
    
    def produto_existe(self, idProduto):
        for produto in self.xml["AuditFile"]["MasterFiles"]["Product"]:
            if produto["ProductCode"] == idProduto:
                return True
        return False
    
    def juntar_produtos(self, produtos):
        for produto in produtos:
            if not self.produto_existe(produto["ProductCode"]):
                self.xml["AuditFile"]["MasterFiles"]["Product"].append(produto)

    def juntar_vendas(self, vendas):
        for venda in vendas:
            self.xml["AuditFile"]["SourceDocuments"]["SalesInvoices"]["Invoice"].append(venda)

    def juntar_movimentos(self, movimentos):
        for movimento in movimentos:
            self.xml["AuditFile"]["SourceDocuments"]["MovementOfGoods"]["StockMovement"].append(movimento)

    def juntar_trabalhos(self, trabalhos):
        for trabalho in trabalhos:
            self.xml["AuditFile"]["SourceDocuments"]["WorkingDocuments"]["WorkDocument"].append(trabalho)
    
    def juntar_pagamentos(self, pagamentos):
        for pagamento in pagamentos:
            self.xml["AuditFile"]["SourceDocuments"]["Payments"]["Payment"].append(pagamento)

    def juntar_dados(self, objXML):
        if self.xml == None:
            self.xml = objXML
        else:
            self.juntar_clientes(objXML["AuditFile"]["MasterFiles"]["Customer"])
            self.juntar_produtos(objXML["AuditFile"]["MasterFiles"]["Product"])
            self.juntar_vendas(objXML["AuditFile"]["SourceDocuments"]["SalesInvoices"]["Invoice"])
            self.juntar_movimentos(objXML["AuditFile"]["SourceDocuments"]["MovementOfGoods"]["StockMovement"])
            
            if self.validar_existencia(objXML["AuditFile"]["SourceDocuments"]["WorkingDocuments"], "WorkDocument"):
                self.juntar_trabalhos(objXML["AuditFile"]["SourceDocuments"]["WorkingDocuments"]["WorkDocument"])
            self.juntar_pagamentos(objXML["AuditFile"]["SourceDocuments"]["Payments"]["Payment"])

    def validar_existencia(self, obj, campo):
        try:
            len(obj[campo])
            return True
        except:
            return False

    def exportar_ficheiro(self):
        ficheiro = open("todos.xml", mode = "w", encoding="utf8")
        ficheiro.write(self.substituir(xmltodict.unparse(self.xml, pretty = True)))
        ficheiro.close()

    def iniciar(self):
        ficheiros = self.todos_ficheiros()
        for ficheiro in ficheiros:
            objXML = self.carregar_ficheiro(ficheiro)
            self.juntar_dados(objXML)
        
        self.exportar_ficheiro()


safts = Compilar_SAFT("ficheiros")
safts.iniciar()
