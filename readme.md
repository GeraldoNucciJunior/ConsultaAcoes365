# 📈 Consulta Ações 365

Aplicação em Python que consulta a cotação de uma ação da bolsa, calcula a **média dos últimos 365 dias** e exibe um **gráfico** com a evolução do preço.

Projeto criado para praticar Python aplicado ao mercado financeiro, unindo mais de 20 anos de experiência em sistemas financeiros (Front/Back-Office, Tesouraria e Fundos) com análise de dados.

---

## ✨ Funcionalidades

- Consulta de cotações em tempo real via Yahoo Finance
- Cálculo da média de fechamento dos últimos 5 pregões
- Gráfico simples com a variação dos preços
- Uso direto pelo terminal: basta digitar o código da ação

## 🛠️ Tecnologias

- [Python 3](https://www.python.org/)
- [yfinance](https://pypi.org/project/yfinance/): dados do mercado financeiro
- [matplotlib](https://matplotlib.org/): geração de gráficos

## 📂 Estrutura do projeto

```
ConsultaAcoes365/
├── app.py            # código principal
├── requirements.txt  # dependências
├── README.md         # documentação
└── prints/           # imagens do resultado
```

## 🚀 Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/ConsultaAcoes365.git
cd ConsultaAcoes365
```

### 2. Crie e ative o ambiente virtual

No Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

No Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute

```bash
python app.py
```

## 💡 Exemplo de uso

```
Digite o código da ação (ex: PETR4.SA): PETR4.SA

Média dos últimos 5 dias de PETR4.SA: R$ 38.45
```

Em seguida, uma janela com o gráfico dos últimos 5 dias é exibida.

> **Dica:** para ações da B3, use o sufixo `.SA` (exemplos: `VALE3.SA`, `ITUB4.SA`, `BBAS3.SA`).

![Resultado do projeto](prints/resultado.png)

## 🔭 Próximos passos

- [ ] Interface web com Streamlit
- [ ] Comparar o desempenho de várias ações ao mesmo tempo
- [ ] Comparador dos 365 maiores fundos de investimento de diferentes instituições
- [ ] Salvar o histórico das consultas em banco de dados (SQLite)
- [ ] Testes automatizados

## 👤 Autor

**Geraldo Nucci Junior**
Desenvolvedor e Tech Lead em sistemas financeiros

- LinkedIn: www.linkedin.com/in/geraldo-nucci-junior-3533a297
- GitHub: https://github.com/GeraldoNucciJunior/ConsultaAcoes365.git
## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usar e adaptar.
