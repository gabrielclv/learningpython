#strings= toda série de caracteres que estiver entre aspas

name = "ada lovelace"
print(name.title()) #. (variável + title()) = início das letras em Maiúsculo
# title() é um MÉTODO (ação que python pode executar em um dado) e o ponto(.) indica que método deve ser executado naquele variável
# todo método é seguido de parênteses pois comumente é necessário de informações adicionais
print(name.upper()) # todas as letras em maiúsculo
print(name.lower()) # todas as letras em minúsculo

# combinando strings!
FirstName = "gabriel" 
SecondName= "cauã"

FullName = FirstName + " " + SecondName #Concatenação: combinar os valores de duas variáveis para ser o valor de uma outra variável
saudação = "hello, " + FullName.title() + "!" #saúdando o user!
print(saudação)

#tabulação(\t + string), pulo de linha(\n + string)
print("o \n\tde \n\t\tbaixo\n\t\t\té\n\t\t\t\tgay")

# Método strip -> retira os espaços extras de uma string (.strip() retira de todos os lados / .rstrip() (apenas espaços extras de uma string do lado direito) / .lstrip() (apenas espaços extras de uma string do lado esquerdo) )
blabla = "             meu nome é douglas          "
blabla = blabla.strip().title()
print(blabla)