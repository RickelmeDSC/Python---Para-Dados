def calcular_combustivel():
    """Função principal para cálculo de combustível."""
    
    # Preços fixos
    PRECOS = {
        'E': 1.70,  # Etanol
        'D': 2.00   # Diesel
    }
    
    # Descontos por tipo e quantidade
    DESCONTOS = {
        'E': {  # Etanol
            'ate_15': 0.02,  # 2% até 15 litros
            'acima_15': 0.04  # 4% acima de 15 litros
        },
        'D': {  # Diesel
            'ate_15': 0.03,   # 3% até 15 litros
            'acima_15': 0.05   # 5% acima de 15 litros
        }
    }
    
    print("╔" + "═"*50 + "╗")
    print("║         CÁLCULO DE COMBUSTÍVEL          ║")
    print("╚" + "═"*50 + "╝\n")
    
    try:
        # Entrada da quantidade
        litros = float(input("Quantidade de litros: "))
        if litros <= 0:
            print("❌ A quantidade deve ser maior que zero!")
            return
        
        # Entrada do tipo de combustível
        tipo = input("Tipo (E - Etanol / D - Diesel): ").upper().strip()
        
        # Validação do tipo
        if tipo not in PRECOS:
            print("\n❌ Tipo de combustível inválido!")
            print("Opções válidas: E (Etanol) ou D (Diesel)")
            return
        
        # Determina o desconto baseado na quantidade
        if litros <= 15:
            desconto = DESCONTOS[tipo]['ate_15']
            faixa = f"até 15 litros ({desconto*100:.0f}%)"
        else:
            desconto = DESCONTOS[tipo]['acima_15']
            faixa = f"acima de 15 litros ({desconto*100:.0f}%)"
        
        # Nome do combustível
        nome_combustivel = "Etanol" if tipo == 'E' else "Diesel"
        
        # Cálculos
        preco_litro = PRECOS[tipo]
        valor_bruto = preco_litro * litros
        valor_desconto = valor_bruto * desconto
        valor_final = valor_bruto - valor_desconto
        
        # Exibição dos resultados
        print(f"\n{'═'*50}")
        print(f"📋 RESUMO DA COMPRA")
        print(f"{'═'*50}")
        print(f"⛽ Combustível: {nome_combustivel}")
        print(f"📊 Quantidade: {litros:.2f} L")
        print(f"💰 Preço por litro: R$ {preco_litro:.2f}")
        print(f"📏 Faixa de desconto: {faixa}")
        print(f"{'─'*50}")
        print(f"💵 Valor bruto: R$ {valor_bruto:.2f}")
        print(f"🏷️ Desconto: {desconto*100:.0f}%")
        print(f"💸 Valor do desconto: R$ {valor_desconto:.2f}")
        print(f"{'═'*50}")
        print(f"💲 VALOR FINAL: R$ {valor_final:.2f}")
        print(f"{'═'*50}")
        
        # Cálculo do preço por litro com desconto
        preco_com_desconto = valor_final / litros
        print(f"💰 Preço médio por litro (com desconto): R$ {preco_com_desconto:.2f}")
        print(f"💲 Economia por litro: R$ {(preco_litro - preco_com_desconto):.2f}")
        
    except ValueError:
        print("❌ Erro: Digite um valor numérico válido para a quantidade!")

# Executa o programa
calcular_combustivel()