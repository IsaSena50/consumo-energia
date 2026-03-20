nome_aparelho = input("Digite o nome do aparelho: ")
potencia = float(input(f"Digite a potência do(a) {nome_aparelho} em Watts (W): "))
horas_dia = float(input(f"Quantas horas por dia o(a) {nome_aparelho} fica ligado(a)? "))

# O cálculo precisa ser guardado em uma variável
consumo_mensal = (potencia * horas_dia * 30) / 1000

print(f"\nAparelho: {nome_aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")