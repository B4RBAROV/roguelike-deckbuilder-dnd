# deck.py

import random

class Deck:
    """Gerencia os montes de Compra, Mão e Descarte do personagem."""
    def __init__(self, cartas_iniciais):
        self.monte_compra = []
        self.mao = []
        self.descarte = []
        
        # Popula e embaralha o monte inicial
        self.monte_compra.extend(cartas_iniciais)
        random.shuffle(self.monte_compra)
        
    def comprar_cartas(self, quantidade_necessaria=5):
        """Compra cartas até a mão atingir o limite ou o deck esgotar."""
        
        while len(self.mao) < quantidade_necessaria:
            
            # Condição de Re-shuffle (Deck com 2 ou menos cartas)
            if len(self.monte_compra) <= 2:
                self._embaralhar_descarte()
                
            # Se ainda houver cartas após o re-shuffle, ou se o monte era grande
            if self.monte_compra:
                carta_comprada = self.monte_compra.pop(0) # Pega a carta do topo
                self.mao.append(carta_comprada)
            else:
                # Não há mais cartas para comprar (mesmo após shuffle)
                break 

        print(f"📚 {len(self.mao)} cartas na Mão.")

    def descartar_carta(self, carta):
        """Move uma carta jogada/selecionada da Mão para o Descarte."""
        if carta in self.mao:
            self.mao.remove(carta)
            self.descarte.append(carta)

    def _embaralhar_descarte(self):
        """Lógica de re-shuffle: Descarte + 2 cartas remanescentes."""
        print("🌀 Monte de compra esgotando! Re-embaralhando descarte...")
        
        # Move as cartas remanescentes do monte de compra para o descarte
        self.descarte.extend(self.monte_compra)
        self.monte_compra = [] # Limpa o monte de compra

        # Embaralha e move o descarte para o monte de compra
        random.shuffle(self.descarte)
        self.monte_compra.extend(self.descarte)
        self.descarte = []
        
        print(f"✅ Novo Monte de Compra com {len(self.monte_compra)} cartas.")