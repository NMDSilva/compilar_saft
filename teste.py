import os
import xmltodict

def substituir(texto):
    repl = "╢╟╡α╓Θσ╥"
    replc = "ÂÃÁÓÍÚÕÊ"
    for i in range(len(repl)):
        texto = texto.replace(repl[i], replc[i])
    return texto

def check_none(texto):
    if texto == None:
        return ""
    else:
        return substituir(texto.strip())



file = open(os.path.join("ficheiros", "207028478_20200201_20200228.XML"), mode="r", encoding="cp437")
root = xmltodict.parse(file.read())



out = substituir(xmltodict.unparse(root, pretty = True))

# print(out)
fileW = open(os.path.join("ficheiros", "temp_207028478_20200201_20200228.XML"), mode = "w", encoding="utf8")

fileW.write(out)

fileW.close()

# for cliente in root["AuditFile"]["MasterFiles"]["Customer"]:
#     print(cliente["CompanyName"])

# print(root)
# xsd = xmlschema.XMLSchema(os.path.join("ficheiros", "saftpt1.04_01.xsd"))


# validate(os.path.join("ficheiros", "207028478_20200101_20200131.XML"), os.path.join("ficheiros", "saftpt1.04_01.xsd"))

