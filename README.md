# CorpSystem Teste

Teste Backend

## Tecnologias Utilizadas

* **Python** -> 3.12
* **Django REST Framework**
* **MySQL**
* **PyTest**
* **Swagger**
* **Docker**


## Descrição

Projeto desenvolvido para mini ERP.

* **Cliente:** Usuário comprador do sistema.
* **Seller:** Usuário vendedor do sistema.
* **Product:** Produtos disponíveis para compra.
* **Sale:** Vendas realizadas.

## Tarefas

* [x] Criar endpoints CRUD para cada entidade.
* [x] Criar endpoint para exportar relatórios (.xlsx e .pdf)
* [x] Criar endpoint para importar dados de produtos (.xlsx)

# Regras de Negócio

* **Cliente:** Validar CPF do cliente.
* **Produto:** Validar se SKU do produto é único e se há quantidade disponível.
* **Venda:** Validar se o cliente existe e se há quantidade disponível do produto.
