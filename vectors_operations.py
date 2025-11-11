import math

def adicionar_vetores(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vetores devem ter o mesmo tamanho para adição.")
    return [a + b for a, b in zip(v1, v2)]

def subtrair_vetores(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vetores devem ter o mesmo tamanho para subtração.")
    return [a - b for a, b in zip(v1, v2)]

def produto_interno(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vetores devem ter o mesmo tamanho para produto interno.")
    return sum(a * b for a, b in zip(v1, v2))

def norma_vetor(v):
    return math.sqrt(sum(x**2 for x in v))

def distancia_euclidiana(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vetores devem ter o mesmo tamanho para distância euclidiana.")
    vetor_subtraido = subtrair_vetores(v1, v2)
    return norma_vetor(vetor_subtraido)

def input_vetor(texto_prompt="Digite o vetor"):
    while True:
        try:
            entrada_usuario = input(f"{texto_prompt} (valores separados por vírgula, ex: 1,2,3): ")
            
            if not entrada_usuario.strip():
                print("Entrada vazia. Por favor, digite valores.")
                continue

            vetor = [float(x.strip()) for x in entrada_usuario.split(',')]
            return vetor
        except ValueError:
            print("Entrada inválida. Por favor, digite números separados por vírgulas.")

def main():
    v1 = input_vetor("Vetor v1")
    v2 = input_vetor("Vetor v2")
    
    print("\n--- Resultados ---")
    
    try:
        print(f"v1 + v2:     {adicionar_vetores(v1, v2)}")
        print(f"v1 - v2:     {subtrair_vetores(v1, v2)}")
        print(f"v1 . v2:     {produto_interno(v1, v2)}")
        print(f"Distância:   {distancia_euclidiana(v1, v2)}")
    except ValueError as e:
        print(f"Erro (v1, v2): {e}")
    
    print(f"Norma(v1):   {norma_vetor(v1)}")
    print(f"Norma(v2):   {norma_vetor(v2)}")

if __name__ == "__main__":
    main()