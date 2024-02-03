"""Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes"""

cod = []
height = []
weight = []

tallest_customer = 0
lowest_customer = 0

fattest_customer = 0
thinner_client = 0

count = 0

while True:

    code = int(input("enter the client code(0 for exit): "))

    if code == 0:
        break

    cod.append(code)

    height.append(float(input("inform the customer's height: ")))

    if height[count] > height[tallest_customer]:
        tallest_customer = count

    if height[lowest_customer] == 0 or height[count] < height[lowest_customer]:
        lowest_customer = count 

    weight.append(float(input("inform the customer`s weight: ")))

    if weight[count] > weight[fattest_customer]:
        fattest_customer = count

    if weight[thinner_client] == 0 or weight[count] < weight[thinner_client]:
        thinner_client = count

    count += 1

print(f"\ntallest client:       cod {cod[tallest_customer]:.0f}      height {height[tallest_customer]:.2f}     weight  {weight[tallest_customer]:.2f}")
print(f"lowest client:       cod {cod[lowest_customer]:.0f}      height {height[lowest_customer]:.2f}     weight  {weight[lowest_customer]:.2f}")
print(f"fattest client:       cod {cod[fattest_customer]:.0f}      height {height[fattest_customer]:.2f}     weight  {weight[fattest_customer]:.2f}")
print(f"thinner client:       cod {cod[thinner_client]:.0f}      height {height[thinner_client]:.2f}     weight  {weight[thinner_client]:.2f}")
