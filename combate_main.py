# combate_main.py

from combatente import Heroi, Inimigo

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
            else:
                print("Opção inválida ou carta não disponível.")

        
        # Verifica se o inimigo morreu após as ações do herói
        if not inimigo.esta_vivo():
            break

        # --- TURNO DO INIMIGO (GOBLIN) ---
        print("\n👹 TURNO DO **GOBLIN**")
        inimigo.preparar_turno() 
        inimigo.acao_ia(heroi)


    # --- FIM DO COMBATE ---
    print("\n" + "="*50)
    print("--- 🏁 FIM DO COMBATE! 🏁 ---")
    
    if heroi.esta_vivo():
        print(f"🎉 **{heroi.nome}** VENCEU! Você explorou o poder de seus modificadores (+{heroi.modificadores.get('FOR')})!")
    else:
        print(f"💀 **{inimigo.nome}** VENCEU! O Goblin levou a melhor desta vez.")

# --- 3. Execução do Combate ---
if __name__ == "__main__":
    # 1. Cria os combatentes
    anao = Heroi()
    goblin = Inimigo()
    
    # 2. Inicia o combate
    iniciar_combate(anao, goblin)