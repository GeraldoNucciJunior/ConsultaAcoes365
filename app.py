import yfinance as yf
import matplotlib.pyplot as plt

def media_ultimos_dias(codigo, dias=365):
    dados = yf.Ticker(codigo).history(period="1mo")["Close"].tail(dias)
    return dados, dados.mean()

if __name__ == "__main__":
    codigo = input("Digite o código da ação (ex: PETR4.SA): ").upper()
    dados, media = media_ultimos_dias(codigo)
    print(f"\nMédia dos últimos 365 dias de {codigo}: R$ {media:.2f}")

    dados.plot(title=f"{codigo} - últimos 365 dias", marker="o")
    plt.ylabel("Preço (R$)")
    plt.show()