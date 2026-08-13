"""
Exemplo 1:
não faz sentido checar estoque para um produto sem validar qual é produto antes
"""
from src.a1_phantom_types.src_file import *
if __name__ == "__main__":
    pedido_nao_validado = receber_pedido()
    pedido_estoque_ok = checar_estoque(pedido_nao_validado)