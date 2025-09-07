# Gestão Financeira

Aplicativo simples com FastAPI para gerenciar contas, categorias e transações financeiras, permitindo separar despesas pessoais e empresariais.

## Requisitos

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Executando testes

```bash
pytest
```

## Deploy no Vercel

O repositório está preparado para ser publicado no [Vercel](https://vercel.com/).
Há uma função em `api/index.py` que expõe a aplicação FastAPI e um arquivo
`vercel.json` com a configuração básica. Após instalar a CLI do Vercel, faça o
deploy com:

```bash
vercel deploy
```
