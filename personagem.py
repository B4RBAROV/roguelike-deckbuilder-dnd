# personagem.py

class Personagem:
    """Classe base para todos os combatentes."""
    def __init__(self, nome, hp_max, dano_base, defesa_base, stamina_max=3):
        self.nome = nome
        self.hp_max = hp_max
        self.hp_atual = hp_max
        self.dano_base = dano_base
        self.defesa_base = defesa_base
        self.bloqueio_atual = 0  
        
        # Mecânica de Stamina
        self.stamina_max = stamina_max
        self.stamina_atual = stamina_max 

    # --- Métodos de Combate (já definidos, sem alteração) ---
    def atacar(self, alvo, dano):
        # ... (código do método atacar) ...
        dano_efetivo = max(0, dano - alvo.bloqueio_atual)
        alvo.bloqueio_atual = max(0, alvo.bloqueio_atual - dano) 
        alvo.hp_atual -= dano_efetivo

        print(f"🗡️ **{self.nome}** ataca **{alvo.nome}** com {dano} de DANO!")
        
        if dano_efetivo > 0:
            print(f"  -> **{alvo.nome}** sofreu {dano_efetivo} de DANO.")
        else:
            print(f"  -> **{alvo.nome}** bloqueou completamente o ataque!")

    def ganhar_bloqueio(self, valor):
        self.bloqueio_atual += valor
        print(f"🛡️ **{self.nome}** ganha {valor} de BLOQUEIO (Total: {self.bloqueio_atual}).")

    # --- Métodos de Turno (Atualizados para Stamina) ---
    def preparar_turno(self):
        """Prepara o personagem para o início do seu turno."""
        self.bloqueio_atual = 0
        self.stamina_atual = self.stamina_max # Restaura a Stamina
        print(f"⚡ {self.nome} recupera {self.stamina_max} de Stamina.")

    def estado(self):
        """Retorna a situação atual do personagem."""
        return (f"[{self.nome}] HP: {self.hp_atual}/{self.hp_max} | "
                f"Defesa: {self.defesa_base} | Bloqueio: {self.bloqueio_atual} | "
                f"Stamina: {self.stamina_atual}/{self.stamina_max}")

    def esta_vivo(self):
        return self.hp_atual > 0