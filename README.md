#SOBRE O PROJETO
Esse projeto é desenvolvido utilizando o Framework Django, do Python, e consiste em uma aplicação para agendamentos de consulta de uma clínica. Além de toda a parte de interface, utilizando HTML e CSS, também foi desenvolvido todo um back-end para que os cadastros fiquem salvos
e possam ser consultados.

#FUNCIONAMENTO
Para o funcionamento do código primeiramente foi criado suas URLs e end-points, e logo após isso foi criado as funções para cada URL, na aba de VIEWS tem todas as funções criadas, principalmente a conexão com o HTML e as requisições HTTP. https://github.com/tallesd12/crud-ceub/blob/main/myapp/views.py
Depois de criado a url e seus funcionamentos, criei a parte dos Models da aplicação, uma classe Pessoa foi criada, com os atributos de nome, cpf, data da consulta e especialidade da consulta. Esses models foram importados para a área administrativa do Django, possibilitando
a criação de agendamentos baseado nesse Model Pessoa.

#INTERFACES
Eu criei 2 interfaces, a primeira de cadastro, onde tem todos os inputs para o usuário agendar sua consulta e com seus dados. E a segunda é uma página de confirmação de cadastro que é mostrada após o usuário finalizar seu agendamento, com um botão com a opção de retorno para a página de agendamento.

#MODELS
Todos os usuários cadastrados são armazenados na área administrativa do Django com o CPF como identificador único, possibilitando sua exclusão. Os dados que são cadastrados nessa área administrativa são encaminhados para uma página onde retorna-os em formato JSON.

Para realizar o funcionamento da aplicação é necessário ativar um servidor local, utilizando o comando 'python manage.py runserver' e logo em seguida colocar os end-points de cada interface.

#TECNOLOGIAS UTILIZADAS
-Python
-Django
-HTML
-CSS
