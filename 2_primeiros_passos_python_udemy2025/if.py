velocidade_permitida = 110
velocidade_verificada = 40

if velocidade_verificada <= 50:
	print("Aumente a velocidade")
elif velocidade_verificada <= velocidade_permitida:
	print("OK")
else:
	print("Diminua a velocidade")

######
	

funcionario_1 = {
  "nome": "Antonio",
  "idade": 30,
  "cidade": "São Paulo",
  "cargo": "Presidente",
  "salario": 100000.00,
  "endereco": {"rua": "Rua das Flores", "numero": 123,"bairro": "Centro","cep": "12345-678"}
} 
if funcionario_1["cargo"] == "Presidente" and funcionario_1["idade"] >= 30:
  funcionario_escalado = True
  print("Funcionario escalado para a reunião")
	