def analisar_triangulo():
    """Função principal para análise de triângulos."""
    
    while True:
        print("\n" + "="*50)
        print("ANALISADOR DE TRIÂNGULOS")
        print("="*50)
        
        try:
            # Entrada
            a = float(input("Lado A: "))
            b = float(input("Lado B: "))
            c = float(input("Lado C: "))
            
            # Validação de positividade
            if a <= 0 or b <= 0 or c <= 0:
                print("❌ Todos os lados devem ser positivos!")
                continue
            
            # Condição de existência
            if a + b > c and a + c > b and b + c > a:
                print("\n✅ TRIÂNGULO VÁLIDO")
                
                # Classificação
                if a == b == c:
                    tipo = "EQUILÁTERO"
                    desc = "três lados iguais"
                elif a == b or a == c or b == c:
                    tipo = "ISÓSCELES"
                    desc = "dois lados iguais"
                else:
                    tipo = "ESCALENO"
                    desc = "três lados diferentes"
                
                print(f"📐 Tipo: {tipo} ({desc})")
                
                # Exibe os lados em ordem
                lados_ordenados = sorted([a, b, c])
                print(f"Lados em ordem crescente: {lados_ordenados[0]} < {lados_ordenados[1]} < {lados_ordenados[2]}")
                
                # Verifica triângulo retângulo (Teorema de Pitágoras)
                if abs(lados_ordenados[0]**2 + lados_ordenados[1]**2 - lados_ordenados[2]**2) < 0.0001:
                    print("📐 É um triângulo RETÂNGULO!")
                
            else:
                print("\n❌ TRIÂNGULO INVÁLIDO")
                print("A soma de dois lados deve ser maior que o terceiro.")
            
            # Pergunta se deseja continuar
            resp = input("\nDeseja analisar outro triângulo? (s/n): ").lower()
            if resp != 's':
                print("\nPrograma encerrado. Até mais!")
                break
                
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números.")

# Executar
analisar_triangulo()