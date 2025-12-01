# combatente.py

from personagem import Personagem
from deck import Deck
from cards.card_base import AtaqueMartelo, LevantarEscudo 

# --- Dicionários de Atributos ---
ATRIBUTOS_ANAO = {
    "FOR": 16, "DES": 14, "CON": 14,
    "INT": 8, "SAB": 12, "CAR": 10
}

# Atributos do Goblin: Fraco em CON, um pouco de DES.
ATRIBUTOS_GOBLIN = {
    "FOR": 12, "DES": 14, "CON": 10,
    "INT": 8, "SAB": 10, "CAR": 8
}

# --- 1. Definição do HERÓI ---
class Heroi(Personagem):
    """Herói: O Anão com Martelo e Escudo."""
    def __init__(self, nome="Anão Guerreiro"):
        super().__init__(
            nome=nome, 
            hp_max=50, 
            dano_base=0, 
            defesa_base=5, 
            stamina_max=3,
            atributos=ATRIBUTOS_ANAO # Passa os atributos
        )
        
        # Criação do Deck Inicial (12 cartas: 5 Ataque, 7 Defesa)
        cartas_iniciais = (
            [AtaqueMartelo() for _ in range(5)] +
            [LevantarEscudo() for _ in range(7)]
        )
        
        # Instancia o Deck e compra a mão inicial de 5 cartas
        self.deck = Deck(cartas_iniciais) 
        self.deck.comprar_cartas(5) 

# --- 2. Definição do INIMIGO ---
class Inimigo(Personagem):
    """Inimigo: O Goblin com Adaga."""
    def __init__(self, nome="Goblin Patife"):
        # O inimigo não precisa de Stamina e usa o dano base simples
        super().__init__(
            nome=nome, 
            hp_max=20, 
            dano_base=7, 
            defesa_base=2,
            stamina_max=0, # Inimigo não usa Stamina/Cartas
            atributos=ATRIBUTOS_GOBLIN # Passa os atributos
        )
        self.adaga_dano = 7 # Usaremos self.dano_base
        
    def acao_ia(self, alvo):
        """Define a lógica simples de IA do inimigo (sempre ataca)."""
        # Aqui o Goblin usa seu dano base, que definimos como 7
        self.atacar(alvo, self.dano_base)