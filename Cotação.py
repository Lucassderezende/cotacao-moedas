import requests
import sys

def menu():
    print("\n---- Escolha a moeda que deseja consultar ----")
    print("USDBRL - Dólar para Real")
    print("EURBRL - Euro para Real")
    print("BTCBRL - Bitcoin para Real")
    print("Digite FINALIZAR para sair do programa.")

def usd_brl(dados):
    print(f"\nValor da cotação USD para BRL = {dados['USDBRL']['bid']}")

def eur_brl(dados):
    print(f"\nValor da cotação EUR para BRL = {dados['EURBRL']['bid']}")

def btc_brl(dados):
    print(f"\nValor da cotação BTC para BRL= {dados['BTCBRL']['bid']}")

def buscar_cotacoes():
    try:
        requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
        requisicao.raise_for_status()
        return requisicao.json()
    except requests.RequestException:
        print("\nErro ao buscar cotações. Tente novamente mais tarde.")
        sys.exit()

def escolher_moeda(dados):
    moeda = input("Digite uma moeda que deseja consultar:(USDBRL, EURBRL, BTCBRL)").upper()
    if moeda == "FINALIZAR":
        print("Programa finalizado!")
        sys.exit()
    funcoes_moeda.get(moeda, lambda dic: print("\nOpção inválida!"))(dados)

funcoes_moeda = {
    "USDBRL": usd_brl,
    "EURBRL": eur_brl,
    "BTCBRL": btc_brl
}

menu()

while True:
    dados = buscar_cotacoes()
    escolher_moeda(dados)

    continuar = input("\nDeseja consultar uma nova moeda?(SIM para continuar e qualquer outra coisa para sair)").upper()
    if continuar != "SIM":
        sys.exit()
    else:
        menu()






















