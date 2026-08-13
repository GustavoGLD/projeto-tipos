from src.a1_phantom_types.src_file import *
if __name__ == "__main__":
    pedido_nao_validado = Pedido[NaoValidado]("frango", 2, "rua x")
    pedido_produto_ok = checar_produto(pedido_nao_validado)
    if pedido_produto_ok:
        pedido_estoque_ok = checar_estoque(pedido_produto_ok)