import requests
from utils.ConsultaEstoca import rodarAPIEstoca  # sua função que retorna os SKUs e estoque
from utils.AtualizaOmie import consultar_produto_omie, atualizar_estoque_omie, atualizar_estoque_kit ,SKUS_KITS


def atualizar_todos_estoques():
    # 1. Consulta a Estoca e pega os SKUs
    skus_disponiveis = rodarAPIEstoca()
    print(f"Total de produtos recebidos: {len(skus_disponiveis)}")

    #2. Puxa lista de SKUs kits

    for produto in skus_disponiveis:

        sku = produto['sku']
        available = produto['available']

        # 3. Consulta Omie para pegar codigo_produto
        codigo_produto = consultar_produto_omie(sku)
        if not codigo_produto:
            print(f"SKU {sku} não encontrado no Omie. Pulando...")
            continue

        #if sku in SKUS_KITS:
            print("SKU pertence a um KIT, executando chamada de Kit")
            atualizar_estoque_kit(codigo_produto,available,sku)
        else:
            # 4. Atualiza estoque
            print("SKU é de PA")
            atualizar_estoque_omie(codigo_produto, available,sku)

if __name__ == "__main__":
    atualizar_todos_estoques()