## Automação para Agendamento de Quadras, na plataforma da Prefeitura de Americana


Este projeto automatiza o processo de agendamento de quadras esportivas no site da Prefeitura de Americana (SP), utilizando **Python**, **Selenium** e dados extraídos de uma planilha Excel.

##  Objetivo

O objetivo deste sistema é agilizar o agendamento de horários esportivos para múltiplos usuários previamente cadastrados em uma planilha, evitando a necessidade de repetir manualmente o processo para cada pessoa, especialmente em momentos de alta demanda no site.

## Tecnologias utilizadas

- Python 3.9+
- Selenium WebDriver
- openpyxl (manipulação de arquivos `.xlsx`)
- Navegador Google Chrome

## Estrutura de pastas

agendamento/ 

		├── main.py # Ponto de entrada do sistema (modo terminal) 
            ├── menu.py # Interface de seleção via terminal 
            ├── agendamento.py # Coordena o processo de agendamento por usuário 
            ├── utils.py # Funções auxiliares e lógica com Selenium 
            └── planilha.xlsx # Planilha com dados dos usuários (CPF, Nome, E-mail, Telefone)


**Importante**: a planilha deve estar na mesma pasta que o código.

## Como usar

1. Certifique-se de ter o Chrome instalado.
2. Instale as dependências:

		pip install selenium openpyxl
3. Execute o script principal:

		python main.py
4. Siga as instruções no terminal para escolher local, horário e horário de início da automação.
5. O sistema acessará o site automaticamente para realizar o agendamento, ao chegar no momento de validar o captcha o programa executará um som de aviso.
