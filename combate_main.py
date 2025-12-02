# combate_main.py

from combatente import Heroi, Inimigo
from utils import pausa

def iniciar_combate(heroi, inimigo):
    print("--- ⚔️ INÍCIO DO COMBATE! ⚔️ ---")
    
    # Loop principal de turnos
    while heroi.esta_vivo() and inimigo.esta_vivo():
        print("\n" + "="*50)
        
        # --- TURNO DO HERÓI (ANÃO) ---
        print(f"🔥 TURNO DE **{heroi.nome}**")
        heroi.preparar_turno() 

        # A mão é comprada automaticamente no início do turno (Lógica no Deck)
        heroi.deck.comprar_cartas(5) 
        
        # Status
        print(f"  > {heroi.estado()}")
        print(f"  > {inimigo.estado()}")
        print(f"  > Deck: {len(heroi.deck.monte_compra)} | Descarte: {len(heroi.deck.descarte)}")
        exibir_hud_combate(heroi, inimigo)
        
        # --- Lógica de Escolha de Carta ---
        # Enquanto o herói tiver Stamina e cartas na mão:
        while heroi.stamina_atual > 0 and heroi.deck.mao:
            print("\n🃏 Cartas na Mão:")
            
            opcoes_validas = {}
            for i, carta in enumerate(heroi.deck.mao):
                indice_real = i + 1
                pode_jogar = "(PODE JOGAR)" if carta.pode_jogar(heroi) else "(CUSTO ALTO)"
                print(f"{indice_real}: {carta.nome} (Custo: {carta.custo_stamina}) - {pode_jogar}")
                opcoes_validas[str(indice_real)] = carta

            print(f"Sua Stamina atual: {heroi.stamina_atual}/{heroi.stamina_max}. Digite 'P' para Passar o Turno.")
            
            escolha = input("Sua escolha (número da carta ou P): ").upper()
            
            if escolha == 'P':
                print("➡️ Passando o turno.")
                heroi.stamina_atual = 0 # Zera Stamina para garantir o fim do loop
                break
            
            if escolha in opcoes_validas:
                carta_escolhida = opcoes_validas[escolha]
                
                if carta_escolhida.executar(heroi, inimigo):
                    # Se a execução foi bem sucedida (custo pago), move a carta para o descarte
                    heroi.deck.descartar_carta(carta_escolhida)
                    pausa(0.5)
            else:
                print("Opção inválida ou carta não disponível.")

        
        # Verifica se o inimigo morreu após as ações do herói
        if not inimigo.esta_vivo():
            break
        
        pausa(1)

        # --- TURNO DO INIMIGO (GOBLIN) ---
        print("\n👹 TURNO DO **GOBLIN**")
        inimigo.preparar_turno() 
        inimigo.acao_ia(heroi)
        
        pausa(1.5)


    # --- FIM DO COMBATE ---
    print("\n" + "="*50)
    print("--- 🏁 FIM DO COMBATE! 🏁 ---")
    
    if heroi.esta_vivo():
        print(f"🎉 **{heroi.nome}** VENCEU! Você explorou o poder de seus modificadores (+{heroi.modificadores.get('FOR')})!")
    else:
        print(f"💀 **{inimigo.nome}** VENCEU! O Goblin levou a melhor desta vez.")
        

def exibir_hud_combate(heroi, inimigo):
    # --- Formatação dos Dados do Heroi ---
    hp_heroi = f"{heroi.hp_atual}/{heroi.hp_max}"
    bloqueio_heroi = heroi.bloqueio_atual
    stamina_heroi = f"{heroi.stamina_atual}/{heroi.stamina_max}"
    
    # Exibe o modo de empunhadura do Anão
    modo_empunhadura = "1 MÃO (ESCUDO)" if heroi.modo_empunhadura == "1-Mao" else "2 MÃOS (D10)"
    
    # Lista os Status Effects do Heroi
    status_heroi = ", ".join(
        [f"{s} ({d})" for s, d in heroi.status_efeitos.items()]
    ) or "Nenhum"

    # --- Formatação dos Dados do Inimigo ---
    hp_inimigo = f"{inimigo.hp_atual}/{inimigo.hp_max}"
    bloqueio_inimigo = inimigo.bloqueio_atual
    
    # Lista os Status Effects do Inimigo
    status_inimigo = ", ".join(
        [f"{s} ({d})" for s, d in inimigo.status_efeitos.items()]
    ) or "Nenhum"

    # --- Montagem da Tela de Combate (HUD) ---
    print("\n" + "="*80)
    
    # Cabeçalho
    print(f"| {'ANÃO GUERREIRO':<35} | VS | {inimigo.nome.upper():<36} |")
    print("-" * 80)
    
    # Linha 1: HP
    print(f"| 💖 HP: {hp_heroi:<10} | {'':<2} | 💖 HP: {hp_inimigo:<10} |")

    # Linha 2: Bloqueio e Modo
    print(f"| 🛡️ BLOQUEIO: {bloqueio_heroi:<5} | {'':<2} | 🛡️ BLOQUEIO: {bloqueio_inimigo:<5} |")

    # Linha 3: Stamina / Status
    print(f"| ⚡ STAMINA: {stamina_heroi:<8} | {'':<2} | 💀 STATUS: {status_inimigo:<29} |")
    
    # Linha 4: Status do Heroi
    print(f"| ⚔️ MODO: {modo_empunhadura:<27} | {'':<2} | {'':<36} |")
    
    print("="*80)
    
    # Informação adicional do Deck (Movida para o HUD)
    print(f"📚 DECK: Compra: {len(heroi.deck.monte_compra)} | Descarte: {len(heroi.deck.descarte)}")

# --- 3. Execução do Combate ---
if __name__ == "__main__":
    # 1. Cria os combatentes
    anao = Heroi()
    goblin = Inimigo()
    
    # 2. Inicia o combate
    iniciar_combate(anao, goblin)