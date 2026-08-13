"""
Não faz sentido olhar o estoque de um "Talvez Produto".
Temos que verificar se realmente é um produto válido, antes de procurar estoque
"""
from src.a1_phantom_types.src_file import *
if __name__ == "__main__":
    pedido_nao_validado = Pedido[NaoValidado]("frango", 2, "rua x")
    pedido_produto_ok = checar_produto(pedido_nao_validado)
    pedido_estoque_ok = checar_estoque(pedido_produto_ok)
