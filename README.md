# API de Registro de Atividades Físicas

## Descrição
Esta API RESTful permite registrar e consultar atividades físicas realizadas por funcionários.  
O projeto foi desenvolvido em **Python + Flask**, com foco em boas práticas: separação de camadas (`routes`, `services`, `utils`) e validação de dados.

## Como executar

### 1. Clonar o repositório

(bash)
git clone https://github.com/SEU_USUARIO/atividade_api.git

cd atividade_api

Criar ambiente virtual:
python -m venv venv

Linux / Mac :
source venv/bin/activate

Windowns:
venv\Scripts\activate

intalar dependencias:

pip install -r requirements.txt

Executar a aplicação:

python app.py
ou
python3 app.py

A API estará disponível em:

http://127.0.0.1:5000/atividades;

Estrutura de dados: 

atividade_api/

│── app.py

│── routes/

│   └── atividades_routes.py

│── services/

│   └── atividades_service.py

│── utils/

│   └── validators.py

│── requirements.txt

│── README.md

app.py → inicialização da aplicação Flask.

routes/ → definição das rotas/endpoints.

services/ → regras de negócio e manipulação dos dados.

utils/ → utilitários e validações.

**Endpoints disponíveis**
1. Registrar nova atividade

POST /atividades

Exemplo de requisição:

{

  "funcional": "123456",

  "dataHora": "2025-09-24T07:30:00",

  "codigoAtividade": "RUN",

  "descricaoAtividade": "Corrida de 5km"

}

Resposta de sucesso:

{

  "mensagem": "Atividade registrada com sucesso!",

  "atividade": {

    "funcional": "123456",

    "dataHora": "2025-09-24T07:30:00",

    "codigoAtividade": "RUN",

    "descricaoAtividade": "Corrida de 5km"
  }

}

2. Registrar várias atividades

POST /atividades

Exemplo de requisição:

[

  {
    "funcional": "111111",

    "dataHora": "2025-09-25T08:00:00",

    "codigoAtividade": "BIK",

    "descricaoAtividade": "Pedalada de 20km"

  },

  {

    "funcional": "222222",

    "dataHora": "2025-09-25T09:00:00",

    "codigoAtividade": "SWM",

    "descricaoAtividade": "Natação 1km"

  }

]

3. Listar todas as atividades

GET /atividades

Resposta:

[
  {

    "funcional": "123456",

    "dataHora": "2025-09-24T07:30:00",

    "codigoAtividade": "RUN",

    "descricaoAtividade": "Corrida de 5km"
  }
]

4. Listar atividades por funcional

GET /atividades/{funcional}

Exemplo:

GET /atividades/123456

Resposta:
{

  "funcional": "123456",

  "atividades": [

    {

      "codigoAtividade": "RUN",

      "dataHora": "2025-09-24T07:30:00",

      "descricaoAtividade": "Corrida de 5km"

    }

  ]
}

**Regra de Validacao**

funcional → deve conter exatamente 6 dígitos numéricos.

dataHora → deve estar no formato YYYY-MM-DDTHH:MM:SS.

codigoAtividade → deve conter 3 letras (ex: RUN, BIK, SWM).

descricaoAtividade → opcional, mas se presente deve ser texto (até 200 caracteres).

**Testes**

A API foi testada com Insomnia.

Recomenda-se rodar os seguintes cenários:

POST com dados válidos (atividade única).

POST com lista de atividades.

POST inválido (faltando campo obrigatório).

GET /atividades → deve retornar todas as registradas.

GET /atividades/{funcional} → deve retornar atividades específicas ou lista vazia.