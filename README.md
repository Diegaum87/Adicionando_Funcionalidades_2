# Adicionando_Funcionalidades

🧩 Tarefa 2 | Adicionando Funcionalidades
Tópicos do conteúdo
Introdução
Essa é uma parte do projeto semanal. Não será necessário entregar parte a parte, mas sim o projeto inteiro ao fim da semana. Leia atentamente aos requerimentos e desenvolva o que é pedido.

Leia o enunciado até o final antes de começar, assim terá uma visão macro sobre tudo que deve ser feito!

Quando concluir a tarefa, adicione as alterações e faça um commit, seguindo o seguinte padrão:

feat: tarefa x finalizada

Adições
Nessa tarefa, iremos desenvolver uma função para adicionar produtos ao menu e também uma função para cálculo de comandas.

Adicionando add_product
Essa função deve ser desenvolvida no módulo product_handler.

Considere que as informações do produto a ser adicionado sempre estarão corretas.

Parâmetro(s):
Variável menu, uma lista representando o menu em questão para o produto ser adicionado.
Quantidade indefinida de argumentos nomeados, representando o produto a ser adicionado.
Procedimento(s):
Você deverá gerar um novo id único para o produto adicionado. O novo id único deve ser armazenado na chave "_id" do novo produto, e deve ser referente ao maior id de produto do menu, somado com 1. Caso não haja produtos no menu, o id gerado deve ser 1.
Após o id ser gerado e anexado ao produto, você deve adicioná-lo ao menu e retornar apenas o produto adicionado com o id gerado.
Adicionando calculate_tab
Inicialmente, você deve criar um módulo tab_handler no pacote management. Sua função calculate_tab deve estar nesse novo módulo.

Para fins didáticos, você pode assumir que nunca uma mesa com ids de produtos inválidos será passada.

Parâmetro(s):
Uma lista de dicionários representando os consumos de uma mesa. Cada um do(s) dicionário(s) conterá a identificação ("_id") do produto consumido e a quantidade (amount) do produto que foi consumida.
Procedimento(s):
Você deverá calcular o subtotal do consumo das mesas e retornar um dicionário no formato especificado, com a chave "subtotal" sendo uma string e o valor sendo um float com arredondamento de duas casas decimais no máximo.
Exemplos
Utilize o arquivo main.py para verificar através de prints se as funcionalidades correspondem aos exemplos. Não se atente a indentação dos retornos, deixamos de uma forma que fosse mais simples de se ler.


