# personagem.py

class Personagem:
    """Classe base para todos os combatentes."""
    # Adicionamos 'atributos=None' no __init__
    def __init__(self, nome, hp_max, dano_base, defesa_base, stamina_max=3, atributos=None):
        self.nome = nome
        self.hp_max = hp_max
        self.hp_atual = hp_max
        self.dano_base = dano_base
        self.defesa_base = defesa_base
        self.bloqueio_atual = 0  
        
        self.stamina_max = stamina_max
        self.stamina_atual = stamina_max 

        # 🆕 Integração dos Atributos e Modificadores
        self.atributos = atributos if atributos is not None else {}
        self.modificadores = self._calcular_modificadores()
        
        # 🆕 Rastreador de Status Effects:
        self.status_efeitos = {}

    def aplicar_status(self, status, duracao):
        """Adiciona ou atualiza a duração de um Status Effect."""
        if status in self.status_efeitos:
            self.status_efeitos[status] = max(self.status_efeitos[status], duracao)
            print(f"✨ {self.nome} teve o status '{status}' RENOVADO. Duração: {self.status_efeitos[status]}.")
        else:
            self.status_efeitos[status] = duracao
            print(f"💀 {self.nome} recebeu o status '{status}'. Duração inicial: {duracao}.")
            

    def processar_status(self):
        """
        Processa todos os Status Effects ativos:
        1. Aplica efeitos por turno (se houver).
        2. Decrementa a duração de cada status.
        3. Remove status cuja duração chegue a zero.
        """
        status_a_remover = []
        
        # 📝 Iteramos sobre uma cópia do dicionário para poder modificá-lo
        for status, duracao in list(self.status_efeitos.items()):
            
            # 1. Aplica Efeito (ex: Dano de Veneno, que faremos mais tarde)
            # Por enquanto, apenas reportamos que o status está ativo
            print(f"    [Status Ativo] ⏳ {self.nome} está sob efeito de '{status}' ({duracao} turnos restantes).")

            # 2. Decrementa a duração
            self.status_efeitos[status] -= 1
            
            # 3. Verifica se a duração chegou a zero
            if self.status_efeitos[status] <= 0:
                status_a_remover.append(status)

        # 4. Remove os status finalizados
        for status in status_a_remover:
            del self.status_efeitos[status]
            print(f"✅ Status '{status}' de {self.nome} expirou e foi removido.")

    def _calcular_modificadores(self):
        modificadores = {}
        
        for atributo, score in self.atributos.items():
            # 1. Cálculo: Usamos // para divisão inteira (ex: 6 // 2 = 3)
            mod = (score - 10) // 2 
            
            # 2. Armazenamento: Adicionamos o resultado ao dicionário
            modificadores[atributo] = mod
            
        return modificadores

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
        """Prepara o personagem para o início do seu turno (processa status e zera bloqueio)."""
        
        # 🆕 Processa Status Effects antes de qualquer ação ou restauração de recurso
        self.processar_status() 
        
        self.bloqueio_atual = 0
        self.stamina_atual = self.stamina_max 
        print(f"⚡ {self.nome} recupera {self.stamina_max} de Stamina.")

    def estado(self):
        """Retorna a situação atual do personagem."""
        return (f"[{self.nome}] HP: {self.hp_atual}/{self.hp_max} | "
                f"Defesa: {self.defesa_base} | Bloqueio: {self.bloqueio_atual} | "
                f"Stamina: {self.stamina_atual}/{self.stamina_max}")

    def esta_vivo(self):
        return self.hp_atual > 0