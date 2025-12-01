# cards/card_base.py

import random

class Carta:
    """Classe base abstrata para todas as cartas."""
    def __init__(self, nome, custo_stamina, descricao, is_critico=False):
        self.nome = nome
        self.custo_stamina = custo_stamina # 1 para Bônus, 2 para Ação
        self.descricao = descricao
        self.is_critico = is_critico
    
    def pode_jogar(self, jogador):
        """Verifica se o jogador tem Stamina suficiente."""
        return jogador.stamina_atual >= self.custo_stamina

    def executar(self, jogador, alvo):
        """
        Método a ser sobrescrito pelas cartas filhas.
        Implementa o efeito da carta.
        """
        if not self.pode_jogar(jogador):
            print(f"❌ Stamina insuficiente para jogar {self.nome} (Custo: {self.custo_stamina}).")
            return False

        print(f"\n--- 🃏 {jogador.nome} JOGA: {self.nome} (Custo: {self.custo_stamina}) ---")
        
        # 1. Checagem de Crítico (d10)
        crit_ativado = False
        if self.is_critico:
            d10 = random.randint(1, 10)
            if d10 == 10:
                crit_ativado = True
                print(f"✨ ROLAGEM D10: 10! Efeito Crítico ATIVADO!")
            else:
                print(f"☁️ ROLAGEM D10: {d10}. Crítico não ativado.")

        # 2. Aplicação do Efeito Principal e Crítico
        self._aplicar_efeito(jogador, alvo, crit_ativado)

        # 3. Consumo de Stamina
        jogador.stamina_atual -= self.custo_stamina
        
        return True

    def _aplicar_efeito(self, jogador, alvo, crit_ativado):
        """Lógica do efeito da carta (deve ser implementada na subclasse)."""
        raise NotImplementedError("O método _aplicar_efeito deve ser implementado nas subclasses de Carta.")


# Exemplo de uma carta de Ataque (para teste)
class AtaqueMartelo(Carta):
    def __init__(self):
        super().__init__(
            nome="Ataque de Martelo", 
            custo_stamina=2, 
            descricao="Causa 10 de dano.", 
            is_critico=True # O martelo terá chance de crítico!
        )
        self.dano_base = 10
        self.dano_critico_extra = 5 # Efeito Crítico

    def _aplicar_efeito(self, jogador, alvo, crit_ativado):
        dano_total = self.dano_base
        if crit_ativado:
            dano_total += self.dano_critico_extra
            print(f"💥 Dano Crítico: +{self.dano_critico_extra} de Dano!")
        
        jogador.atacar(alvo, dano_total)
        
# Exemplo de uma carta de Defesa (para teste)
class LevantarEscudo(Carta):
    def __init__(self):
        super().__init__(
            nome="Levantar Escudo", 
            custo_stamina=1, 
            descricao="Ganha 8 de Bloqueio."
        )
        self.bloqueio_base = 8

    def _aplicar_efeito(self, jogador, alvo, crit_ativado):
        jogador.ganhar_bloqueio(self.bloqueio_base)