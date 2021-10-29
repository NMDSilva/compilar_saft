import os
import xml.etree.ElementTree as ET
from clientes import Cliente
from produtos import Produto
from tabela_iva import IVA

class Read_xml():
    def __init__(self, pasta) -> None:
        self.pasta = pasta
        self.clientes = []
        self.produtos = []
        self.tabela_iva = []

    @property
    def get_clientes(self):
        return self.clientes

    @property
    def get_produtos(self):
        return self.produtos

    @property
    def get_tabela_iva(self):
        return self.tabela_iva
    
    def todos_ficheiros(self):
        return [os.path.join(self.pasta, arquivo) for arquivo in os.listdir(self.pasta) if arquivo.lower().endswith(".xml")]

    def remover_espacos_fim(self, nomeFicheiro):
        file = open(nomeFicheiro, mode="r", encoding="cp437")
        replacement = ""
        for line in file:
            line = line.strip().replace("urn:OECD:StandardAuditFile-Tax:PT_1.04_01", "")
            replacement = replacement + line + "\n"
        file.close()
        newFile = open(nomeFicheiro, mode="w", encoding="cp437")
        newFile.write(replacement)
        newFile.close()
    
    def substituir(self, texto):
        repl = "╢╟╡α╓Θσ╥"
        replc = "ÂÃÁÓÍÚÕÊ"
        for i in range(len(repl)):
            texto = texto.replace(repl[i], replc[i])
        return texto

    def check_none(self, texto):
        if texto == None:
            return ""
        else:
            return self.substituir(texto.text.strip())
    
    def cliente_existe(self, idCliente):
        for cliente in self.clientes:
            if cliente.id == idCliente:
                return False
        return True

    def carregar_clientes(self, root):
        for cliente in root.findall("./MasterFiles/Customer"):
            idCliente = self.check_none(cliente.find("CustomerID"))
            if self.cliente_existe(idCliente):
                self.clientes.append(
                    Cliente(
                        self.check_none(cliente.find("CustomerID")),
                        self.check_none(cliente.find("CustomerTaxID")),
                        self.check_none(cliente.find("CompanyName")),
                        self.check_none(cliente.find("Contact")),
                        self.check_none(cliente.find("BillingAddress/AddressDetail")),
                        self.check_none(cliente.find("BillingAddress/City")),
                        self.check_none(cliente.find("BillingAddress/PostalCode")),
                        self.check_none(cliente.find("BillingAddress/Country"))
                    )
                )

    def produto_existe(self, idProduto):
        for produto in self.produtos:
            if produto.codigo == idProduto:
                return False
        return True
    
    def carregar_produtos(self, root):
        for produto in root.findall("./MasterFiles/Product"):
            idProduto = self.check_none(produto.find("ProductCode"))
            if self.produto_existe(idProduto):
                self.produtos.append(
                    Produto(
                        self.check_none(produto.find("ProductCode")),
                        self.check_none(produto.find("ProductType")),
                        self.check_none(produto.find("ProductDescription")),
                        self.check_none(produto.find("ProductNumberCode"))
                    )
                )

    def iva_existe(self, idIVA):
        for txIva in self.tabela_iva:
            if txIva.code == idIVA:
                return False
        return True
    
    def carregar_produtos(self, root):
        for regIVA in root.findall("./MasterFiles/TaxTable/TaxTableEntry"):
            txIva = self.check_none(regIVA.find("TaxCode"))
            if self.iva_existe(txIva):
                self.tabela_iva.append(
                    Produto(
                        self.check_none(regIVA.find("ProductCode")),
                        self.check_none(regIVA.find("ProductType")),
                        self.check_none(regIVA.find("ProductDescription")),
                        self.check_none(regIVA.find("ProductNumberCode"))
                    )
                )

    def carregar_dados(self, nomeFicheiro):
        file = open(nomeFicheiro, mode="r", encoding="cp437")
        root = ET.ElementTree(ET.fromstring(file.read())).getroot()
        self.carregar_clientes(root)
        self.carregar_produtos(root)

    def iniciar(self):
        ficheiros = self.todos_ficheiros()
        for ficheiro in ficheiros:
            self.remover_espacos_fim(ficheiro)
            self.carregar_dados(ficheiro)



# nomeFicheiro = "207028478_20200101_20200131.XML"

# file = open(os.path.join(pasta, nomeFicheiro), mode="r", encoding="cp437")
# root = ET.ElementTree(ET.fromstring(file.read())).getroot()

# for parent in root.findall("./MasterFiles/Customer"):
#     print(parent.find("CustomerID").text)
    # child = parent.iter("{urn:OECD:StandardAuditFile-Tax:PT_1.04_01}Customer", ns)
    # for costumer in child:
    #     Clientes.append(
    #         {
    #             'CustomerID': costumer.find("{urn:OECD:StandardAuditFile-Tax:PT_1.04_01}CustomerID").text,
    #             'AccountID': costumer.find("{urn:OECD:StandardAuditFile-Tax:PT_1.04_01}AccountID").text,
    #             'CustomerTaxID': costumer.find("{urn:OECD:StandardAuditFile-Tax:PT_1.04_01}CustomerTaxID").text,
    #             'CompanyName': costumer.find("{urn:OECD:StandardAuditFile-Tax:PT_1.04_01}CompanyName").text,
    #             'Contact': costumer.find("{urn:OECD:StandardAuditFile-Tax:PT_1.04_01}Contact").text,
    #             'SelfBillingIndicator': costumer.find("{urn:OECD:StandardAuditFile-Tax:PT_1.04_01}SelfBillingIndicator").text,
    #             'AddressDetail': costumer.find("{urn:OECD:StandardAuditFile-Tax:PT_1.04_01}BillingAddress/{urn:OECD:StandardAuditFile-Tax:PT_1.04_01}AddressDetail").text                
    #         }
    #     )
        
        #     if costumer is not None:


# print(Clientes)