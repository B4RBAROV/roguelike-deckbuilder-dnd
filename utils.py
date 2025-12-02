# utils.py

import random
import time # 🆕 Importação necessária para pausas

def pausa(segundos=1):
    """Pausa a execução do programa por um número de segundos para melhorar a leitura do log de combate."""
    time.sleep(segundos)
    

def rolar_dado(lados, rolls=1, vantagem=False, desvantagem=False):
    """
    Rola um dado de 'lados' faces, com suporte a Vantagem/Desvantagem (d20 style).
    - lados: O número de faces do dado (ex: 8, 10, 20).
    - rolls: O número de dados a rolar (padrão 1).
    - vantagem/desvantagem: Booleanos para forçar a rolagem dupla.
    
    Retorna a soma dos resultados.
    """
    
    resultados = []
    
    # Se houver Vantagem ou Desvantagem, rola 2 vezes (ou 1 se for rolagem base)
    num_rolagens = 2 if (vantagem or desvantagem) else 1 
    
    for _ in range(num_rolagens):
        resultados.append(random.randint(1, lados))

    if vantagem:
        return max(resultados)
    elif desvantagem:
        return min(resultados)
    else:
        # Se for rolagem simples (d8, d10, ou d20 sem V/D)
        return sum(resultados)
    
# Em utils.py

# ... (função rolar_dado) ...
    
def teste_atributo(atacante, alvo, atributo_nome):
    """
    Simula uma disputa de rolagem de dados (d20) entre atacante e alvo.
    - Retorna True se o alvo falhar (roll_alvo < roll_atacante).
    """
    
    # 1. Obter Modificadores
    mod_atacante = atacante.modificadores.get(atributo_nome, 0)
    mod_alvo = alvo.modificadores.get(atributo_nome, 0)
    
    # 2. Verificar Status Effects do alvo para Vantagem/Desvantagem
    # Nota: Prostrado está dando VANTAGEM ao ATACANTE (aqui, é DESVANTAGEM ao ALVO no save)
    desvantagem = "Desorientação" in alvo.status_efeitos or "Prostrado" in atacante.status_efeitos
    vantagem = "Vantagem" in alvo.status_efeitos # Adicione outros status de vantagem aqui se necessário

    # 3. Realizar as Rolagens (d20)
    roll_atacante = rolar_dado(20) + mod_atacante
    
    # O alvo rola com V/D/Normal
    roll_alvo = rolar_dado(20, vantagem=vantagem, desvantagem=desvantagem) + mod_alvo

    print(f"🎲 Teste de {atributo_nome}: {atacante.nome} ({roll_atacante}) vs. {alvo.nome} ({roll_alvo})")

    # 4. Determinar o Resultado
    if roll_alvo < roll_atacante:
        print(f"❌ {alvo.nome} FALHOU no Teste de {atributo_nome}!")
        return True # Alvo falhou no teste
    
    print(f"✅ {alvo.nome} OBTEVE SUCESSO no Teste de {atributo_nome}!")
    return False # Alvo obteve sucesso