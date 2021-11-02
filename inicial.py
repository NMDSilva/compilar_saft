import os
from ler_ficheiros import Read_xml
import csv

xml = Read_xml("ficheiros")
xml.iniciar()


if __name__ == '__main__':
    folder = "export"
    filename = 'clientes.csv'
    try:
        with open(os.path.join(folder, filename), 'w', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(["ID", "NIF", "Nome", "Contacto", "Endereço", "Cidade", "Código Postal", "País"])
            for cliente in xml.get_clientes:
                writer.writerow([cliente.id, cliente.nif, cliente.nome, cliente.contacto, cliente.endereco, cliente.cidade, cliente.cod_postal, cliente.pais])
    except BaseException as e:
        print('Erro no ficheiro: ', filename)
        print(e)
    else:
        print(filename, 'Ficheiro exportado com sucesso!')

    filename = 'produtos.csv'
    try:
        with open(os.path.join(folder, filename), 'w', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(["Código", "Tipo", "Descrição", "Número"])
            for produto in xml.get_produtos:
                writer.writerow([produto.codigo, produto.tipo, produto.descricao, produto.numero])
    except BaseException as e:
        print('Erro no ficheiro: ', filename)
        print(e)
    else:
        print(filename, 'Ficheiro exportado com sucesso!')