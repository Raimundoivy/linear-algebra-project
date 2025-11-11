import numpy as np
from numpy.linalg import eig, det, inv

def obter_dados_proprios(m):
    m_np = np.array(m)
    try:
        autovalores, autovetores = eig(m_np)
        return autovalores, autovetores
    except np.linalg.LinAlgError as e:
        raise ValueError(f"Erro ao calcular autovalores/autovetores: {str(e)}")
    except Exception:
        raise ValueError("Erro: A matriz deve ser quadrada para esta operação.")

def determinante_matriz(m):
    m_np = np.array(m)
    try:
        return det(m_np)
    except np.linalg.LinAlgError as e:
        raise ValueError(f"Erro ao calcular determinante: {str(e)}")
    except Exception:
        raise ValueError("Erro: A matriz deve ser quadrada para esta operação.")

def inversa_matriz(m):
    m_np = np.array(m)
    try:
        return inv(m_np)
    except np.linalg.LinAlgError:
        raise ValueError("Erro: A matriz é singular (não invertível) ou não é quadrada")
    except Exception as e:
        raise ValueError(f"Erro ao calcular inversa: {str(e)}")

def adicionar_matrizes(m1, m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        raise ValueError("Matrizes devem ter as mesmas dimensões para adição.")
    
    return [[c1 + c2 for c1, c2 in zip(linha1, linha2)] for linha1, linha2 in zip(m1, m2)]

def subtrair_matrizes(m1, m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        raise ValueError("Matrizes devem ter as mesmas dimensões para subtração.")
    
    return [[c1 - c2 for c1, c2 in zip(linha1, linha2)] for linha1, linha2 in zip(m1, m2)]

def multiplicar_matrizes(m1, m2):
    linhas_m1 = len(m1)
    cols_m1 = len(m1[0]) if linhas_m1 > 0 else 0
    linhas_m2 = len(m2)
    cols_m2 = len(m2[0]) if linhas_m2 > 0 else 0

    if cols_m1 != linhas_m2:
        raise ValueError(f"Número de colunas de m1 ({cols_m1}) deve ser igual ao número de linhas de m2 ({linhas_m2}).")

    m2_transposta = list(zip(*m2))
    
    return [
        [sum(elem_m1 * elem_m2 for elem_m1, elem_m2 in zip(linha_m1, col_m2)) for col_m2 in m2_transposta]
        for linha_m1 in m1
    ]


def input_matriz(texto_prompt="Digite a matriz"):
    print(f"\n{texto_prompt}")
    while True:
        try:
            linhas_count = int(input("  Número de linhas: "))
            colunas_count = int(input("  Número de colunas: "))
            
            if linhas_count <= 0 or colunas_count <= 0:
                print("Erro: Dimensões devem ser positivas. Tente novamente.")
                continue
            
            matriz = []
            i = 0
            while i < linhas_count:
                entrada_linha = input(f"  Linha {i+1} ({colunas_count} valores separados por vírgula): ")
                
                try:
                    if not entrada_linha.strip():
                         print("Entrada da linha está vazia. Tente esta linha novamente.")
                         continue

                    linha = [float(x.strip()) for x in entrada_linha.split(',')]
                    
                    if len(linha) != colunas_count:
                        print(f"Erro: Esperava {colunas_count} valores, obteve {len(linha)}. Tente esta linha novamente.")
                        continue
                    
                    matriz.append(linha)
                    i += 1
                
                except ValueError:
                    print("Entrada inválida. Por favor, digite números. Tente esta linha novamente.")
                    continue
            
            return matriz

        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para as dimensões.")

def main():
    m1 = input_matriz("Matriz m1")
    m2 = input_matriz("Matriz m2")
        
    try:
        print(f"m1 + m2:\n{np.array(adicionar_matrizes(m1, m2))}")
        print(f"\nm1 - m2:\n{np.array(subtrair_matrizes(m1, m2))}")
        print(f"\nm1 * m2:\n{np.array(multiplicar_matrizes(m1, m2))}")
    except (ValueError, np.linalg.LinAlgError) as e:
        print(f"Erro nas operações binárias (dimensões incompatíveis?): {e}")

    try:
        print(f"Determinante(m1): {determinante_matriz(m1)}")
        
        m1_autovalores, m1_autovetores = obter_dados_proprios(m1)
        print(f"\nAutovalores(m1):\n{m1_autovalores}")
        
        try:
            print(f"\nInversa(m1):\n{inversa_matriz(m1)}")
        except (ValueError, np.linalg.LinAlgError) as e:
            print(f"Erro (inversa m1): {e}")
            
    except (ValueError, np.linalg.LinAlgError) as e:
        print(f"Erro na análise de m1 (pode não ser quadrada): {e}")
    
    try:
        print(f"Determinante(m2): {determinante_matriz(m2)}")
        
        m2_autovalores, m2_autovetores = obter_dados_proprios(m2)
        print(f"\nAutovalores(m2):\n{m2_autovalores}")

        try:
            print(f"\nInversa(m2):\n{inversa_matriz(m2)}")
        except (ValueError, np.linalg.LinAlgError) as e:
            print(f"Erro (inversa m2): {e}")

    except (ValueError, np.linalg.LinAlgError) as e:
        print(f"Erro na análise de m2 (pode não ser quadrada): {e}")


if __name__ == "__main__":
    main()