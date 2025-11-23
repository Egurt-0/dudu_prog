import xml.etree.ElementTree as ET


dados = """<?xml version='1.0' encoding='utf-8'?>

<clientes>
    <cliente>
        <id>1</id>
        <nome>Rodrigo</nome>
        <idade>41</idade>
        <cidade>BH</cidade>
    </cliente>
    <cliente>
        <id>1</id>
        <nome>Rogersom</nome>
        <idade>35</idade>
        <cidade>Paris</cidade>
        </cliente>  
</clientes>
"""



caminho_arquivo = "dados/clientes.xml"

# 1 exportando dados para xml
with open(caminho_arquivo, "w", encoding="utf-8") as f:
    f.write(dados)

# lendo dados do xml
tree = ET.parse(caminho_arquivo)
root = tree.getroot()
for cliente in root.findall("cliente"):
    id_cliente = cliente.find("id").text
    nome_cliente = cliente.find("nome").text
    idade_cliente = cliente.find("idade").text
    cidade_cliente = cliente.find("cidade").text


    print(f"id: {id_cliente} - Nome: {nome_cliente} - idade: {idade_cliente} - cidade: {cidade_cliente}")


# adicionando cliente
novo_cliente = ET.Element("cliente")
id_novo = ET.SubElement(novo_cliente, "id")
id_novo.text = "5"
nome_novo = ET.SubElement(novo_cliente, "nome")
nome_novo.text = "larissa meneguel"
idade_novo = ET.SubElement(novo_cliente, "idade")
idade_novo.text = 312
cidade_novo = ET.SubElement(novo_cliente, "cidade")
cidade_novo.text = "federal"

root.append(novo_cliente)


# salvando no xml

tree.write(caminho_arquivo, encoding='utf-8', xml_declaration=True)

