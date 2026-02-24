def calculadora_completa():
    """Calculadora com classificação e opção de continuar."""
    
    historico = []
    
    print("╔" + "═"*50 + "╗")
    print("║     CALCULADORA INTELIGENTE v1.0     ║")
    print("╚" + "═"*50 + "╝\n")
    
    while True:
        try:
            print("\n" + "─" * 50)
            a = float(input("Primeiro número: "))
            b = float(input("Segundo número: "))
            
            print("\nOperações:")
            print("  [1] +    [2] -    [3] *    [4] /")
            print("  [5] //   [6] %     [7] **   [0] SAIR")
            
            op = input("\nEscolha: ")
            
            if op == "0":
                break
            
            # Mapeamento de operações
            if op == "1":
                res = a + b
                nome = "+"
            elif op == "2":
                res = a - b
                nome = "-"
            elif op == "3":
                res = a * b
                nome = "*"
            elif op == "4":
                if b == 0:
                    print("❌ Erro: Divisão por zero!")
                    continue
                res = a / b
                nome = "/"
            elif op == "5":
                if b == 0:
                    print("❌ Erro: Divisão por zero!")
                    continue
                res = a // b
                nome = "//"
            elif op == "6":
                if b == 0:
                    print("❌ Erro: Divisão por zero!")
                    continue
                res = a % b
                nome = "%"
            elif op == "7":
                res = a ** b
                nome = "**"
            else:
                print("❌ Operação inválida!")
                continue
            
            # Mostra resultado e classifica
            print(f"\n📝 {a} {nome} {b} = {res}")
            
            # Classificação
            print("\n📊 CLASSIFICAÇÃO:")
            
            # Par ou ímpar
            if res.is_integer():
                pi = "PAR" if int(res) % 2 == 0 else "ÍMPAR"
                print(f"  • Par/Ímpar: {pi}")
            else:
                print(f"  • Par/Ímpar: Não se aplica")
            
            # Positivo/negativo
            if res > 0:
                print(f"  • Sinal: POSITIVO")
            elif res < 0:
                print(f"  • Sinal: NEGATIVO")
            else:
                print(f"  • Sinal: ZERO")
            
            # Inteiro/decimal
            if res.is_integer():
                print(f"  • Tipo: INTEIRO (valor: {int(res)})")
            else:
                print(f"  • Tipo: DECIMAL")
                print(f"    - Parte inteira: {int(res)}")
                print(f"    - Parte decimal: {abs(res - int(res)):.4f}".rstrip('0'))
            
            # Salva no histórico
            historico.append(f"{a} {nome} {b} = {res}")
            
        except ValueError:
            print("❌ Erro: Digite números válidos!")
        except OverflowError:
            print("❌ Erro: Resultado muito grande!")
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
    
    # Mostra histórico
    if historico:
        print("\n" + "═" * 50)
        print("HISTÓRICO DE OPERAÇÕES:")
        for i, item in enumerate(historico, 1):
            print(f"{i}. {item}")
    
    print("\nPrograma encerrado. Até mais!")

# Executa
calculadora_completa()