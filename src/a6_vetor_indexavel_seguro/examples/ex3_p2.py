from src.a6_vetor_indexavel_seguro.src_file import remove, vtail
if __name__ == "__main__":
    vetor1 = ("a", "b", "c", "d")
    vetor2 = remove(vetor1)
    print(vetor2[2]) # certo!

    vetor3 = vtail(vetor1)
    print(vetor3[2]) # certo!

