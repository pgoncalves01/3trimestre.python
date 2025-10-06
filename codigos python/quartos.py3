class Quarto:
    def __init__(self, quarto_id, departamento_id, numero, tipo, capacidade, status, valor_diaria):
        self.quarto_id = quarto_id
        self.departamento_id = departamento_id
        self.numero = numero
        self.tipo = tipo
        self.capacidade = capacidade
        self.status = status
        self.valor_diaria = valor_diaria
    
    def exibir_info(self):
        print(f"\n=== INFORMAÇÕES DO QUARTO ===")
        print(f"ID do Quarto: {self.quarto_id}")
        print(f"ID do Departamento: {self.departamento_id}")
        print(f"Número: {self.numero}")
        print(f"Tipo: {self.tipo}")
        print(f"Capacidade: {self.capacidade} pacientes")
        print(f"Status: {self.status}")
        print(f"Valor Diária: R$ {self.valor_diaria:.2f}")

def validar_tipo_quarto(tipo):
    """Valida tipo de quarto"""
    tipos_validos = ['Standard', 'Luxo', 'UTI', 'Enfermaria', 'Apartamento']
    return tipo in tipos_validos

def validar_status_quarto(status):
    """Valida status do quarto"""
    status_validos = ['Disponível', 'Ocupado', 'Manutenção', 'Limpeza']
    return status in status_validos

if __name__ == "__main__":
    print("=== CADASTRO DE QUARTO ===")
    
    quarto_id = int(input("Digite o ID do quarto: "))
    departamento_id = int(input("Digite o ID do departamento: "))
    
    numero = input("Digite o número do quarto (máx 10 caracteres): ")
    while len(numero) > 10:
        print("Número muito longo! Máximo 10 caracteres.")
        numero = input("Digite o número do quarto: ")
    
    print("Tipos disponíveis: Standard, Luxo, UTI, Enfermaria, Apartamento")
    tipo = input("Digite o tipo do quarto: ")
    while not validar_tipo_quarto(tipo):
        print("Tipo inválido! Escolha entre: Standard, Luxo, UTI, Enfermaria, Apartamento")
        tipo = input("Digite o tipo do quarto: ")
    
    capacidade = int(input("Digite a capacidade (1-6): "))
    while capacidade < 1 or capacidade > 6:
        print("Capacidade deve ser entre 1 e 6 pacientes!")
        capacidade = int(input("Digite a capacidade: "))
    
    print("Status disponíveis: Disponível, Ocupado, Manutenção, Limpeza")
    status = input("Digite o status: ")
    while not validar_status_quarto(status):
        print("Status inválido! Escolha entre: Disponível, Ocupado, Manutenção, Limpeza")
        status = input("Digite o status: ")
    
    valor_diaria = float(input("Digite o valor da diária: R$ "))
    while valor_diaria < 0:
        print("Valor não pode ser negativo!")
        valor_diaria = float(input("Digite o valor da diária: R$ "))
    
    quarto = Quarto(quarto_id, departamento_id, numero, tipo, capacidade, status, valor_diaria)
    
    quarto.exibir_info()
