"""
SMART ENERGY COLONY
Sistema inteligente de gestão de energia de uma colônia.

Projeto acadêmico: estruturas de dados, lógica de decisão,
regressão linear simples e análise de geração/consumo.
"""

# ============================================================
# 1. ESTRUTURAÇÃO DOS DADOS
# ============================================================

def criar_dados_colonia():
    """Cria e organiza os dados da colônia em dicionários e listas."""
    return {
        "energia": {
            "geracao": 45,
            "consumo": 60,
            "reserva": 15
        },
        "clima": {
            "condicao": "ensolarado",
            "vento": 10
        },
        "sistemas": {
            "energetico": {
                "solar": {"ativo": True},
                "eolico": {"ativo": True}
            },
            "essenciais": {
                "suporte_a_vida": {"ativo": True},
                "comunicacao": {"ativo": True}
            },
            "nao_essenciais": {
                "iluminacao_externa": {"ativo": True},
                "entretenimento": {"ativo": True}
            }
        },
        "historico_vento": [8, 10, 12],
        "historico_energia": [20, 25, 30]
    }


# ============================================================
# 2. LÓGICA DE DECISÃO
# ============================================================

def tomar_decisao(dados):
    """
    Analisa geração, consumo e reserva.
    Prioriza os sistemas essenciais e recomenda ações.
    """
    energia = dados["energia"]
    geracao = energia["geracao"]
    consumo = energia["consumo"]
    reserva = energia["reserva"]

    decisoes = []

    # Regra de prioridade: suporte à vida nunca deve ser desligado.
    dados["sistemas"]["essenciais"]["suporte_a_vida"]["ativo"] = True
    decisoes.append("Prioridade: manter o suporte à vida ligado.")

    # Regras de decisão sobre geração e consumo.
    if consumo > geracao:
        decisoes.append("ALERTA: o consumo está maior que a geração.")
        decisoes.append("AÇÃO: reduzir o consumo e ativar o modo economia.")

        # Desliga apenas sistemas não essenciais.
        for sistema in dados["sistemas"]["nao_essenciais"].values():
            sistema["ativo"] = False

    elif geracao > consumo:
        excedente = geracao - consumo
        decisoes.append("SUGESTÃO: existe energia excedente.")
        decisoes.append(
            f"AÇÃO: armazenar aproximadamente {excedente} unidades de energia."
        )

    else:
        decisoes.append("SITUAÇÃO: geração e consumo estão equilibrados.")

    # Regra adicional para nível baixo de energia.
    if geracao < 50:
        decisoes.append(
            "ATENÇÃO: geração abaixo de 50 unidades. Reduzir o consumo."
        )

    if reserva <= 0:
        decisoes.append("ALERTA: não há energia disponível na reserva.")

    return decisoes


# ============================================================
# 3. MODELAGEM E PREVISÃO - REGRESSÃO LINEAR SIMPLES
# ============================================================

def calcular_regressao(valores_x, valores_y):
    """
    Calcula os coeficientes de uma reta: y = a*x + b.
    Não utiliza bibliotecas externas.
    """
    if len(valores_x) != len(valores_y):
        raise ValueError("As listas precisam ter o mesmo tamanho.")

    if len(valores_x) < 2:
        raise ValueError("São necessários pelo menos dois pontos.")

    quantidade = len(valores_x)
    media_x = sum(valores_x) / quantidade
    media_y = sum(valores_y) / quantidade

    numerador = sum(
        (x - media_x) * (y - media_y)
        for x, y in zip(valores_x, valores_y)
    )
    denominador = sum((x - media_x) ** 2 for x in valores_x)

    if denominador == 0:
        raise ValueError("Os valores de vento não podem ser todos iguais.")

    inclinacao = numerador / denominador
    intercepto = media_y - inclinacao * media_x

    return inclinacao, intercepto


def prever_energia(vento, historico_vento, historico_energia):
    """Estima a geração de energia com base na velocidade do vento."""
    inclinacao, intercepto = calcular_regressao(
        historico_vento, historico_energia
    )
    previsao = inclinacao * vento + intercepto
    return max(0, previsao)


# ============================================================
# 4. ANÁLISE DO USO DE ENERGIA
# ============================================================

def analisar_energia(dados):
    """Compara geração, consumo e reserva e apresenta um diagnóstico."""
    energia = dados["energia"]
    geracao = energia["geracao"]
    consumo = energia["consumo"]
    reserva = energia["reserva"]

    saldo = geracao - consumo

    print("\n========== ANÁLISE DE ENERGIA ==========")
    print(f"Geração: {geracao} unidades")
    print(f"Consumo: {consumo} unidades")
    print(f"Reserva: {reserva} unidades")
    print(f"Saldo (geração - consumo): {saldo} unidades")

    if consumo > geracao:
        print("Resultado: ALERTA — consumo maior que geração.")
    elif geracao > consumo:
        print("Resultado: excedente de energia.")
    else:
        print("Resultado: geração e consumo equilibrados.")

    print("\nDecisões do sistema:")
    for decisao in tomar_decisao(dados):
        print(f"- {decisao}")

    print("\nEstado dos sistemas:")
    for grupo, sistemas in dados["sistemas"].items():
        print(f"{grupo.upper()}:")
        for nome, informacoes in sistemas.items():
            estado = "LIGADO" if informacoes["ativo"] else "DESLIGADO"
            print(f"  - {nome.replace('_', ' ').title()}: {estado}")


# ============================================================
# 5. ENTRADA DE DADOS PELO USUÁRIO
# ============================================================

def ler_numero(mensagem, valor_padrao):
    """Lê um número inteiro; se ficar vazio, usa o valor padrão."""
    while True:
        entrada = input(f"{mensagem} [{valor_padrao}]: ").strip()
        if entrada == "":
            return valor_padrao
        try:
            numero = int(entrada)
            if numero < 0:
                print("Digite um valor igual ou maior que zero.")
                continue
            return numero
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def atualizar_dados(dados):
    """Permite informar novos valores de geração, consumo e reserva."""
    print("\nDigite os dados atuais da colônia.")
    dados["energia"]["geracao"] = ler_numero(
        "Geração de energia", dados["energia"]["geracao"]
    )
    dados["energia"]["consumo"] = ler_numero(
        "Consumo de energia", dados["energia"]["consumo"]
    )
    dados["energia"]["reserva"] = ler_numero(
        "Reserva de energia", dados["energia"]["reserva"]
    )
    dados["clima"]["vento"] = ler_numero(
        "Velocidade do vento", dados["clima"]["vento"]
    )


# ============================================================
# 6. MENU PRINCIPAL
# ============================================================

def exibir_menu():
    print("\n" + "=" * 48)
    print("       SMART ENERGY COLONY")
    print(" Sistema Inteligente de Gestão de Energia")
    print("=" * 48)
    print("1 - Analisar dados atuais da colônia")
    print("2 - Informar novos dados")
    print("3 - Prever geração de energia pelo vento")
    print("4 - Exibir estrutura dos dados")
    print("0 - Encerrar")
    print("=" * 48)


def exibir_estrutura(dados):
    """Mostra os principais dados organizados pelo sistema."""
    print("\n========== ESTRUTURA DOS DADOS ==========")
    print("Energia:", dados["energia"])
    print("Clima:", dados["clima"])
    print("Sistemas:", dados["sistemas"])
    print("Histórico de vento:", dados["historico_vento"])
    print("Histórico de energia:", dados["historico_energia"])


def executar():
    """Controla a execução do programa."""
    dados = criar_dados_colonia()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            analisar_energia(dados)

        elif opcao == "2":
            atualizar_dados(dados)
            print("\nDados atualizados com sucesso!")

        elif opcao == "3":
            vento = ler_numero(
                "Informe a velocidade do vento",
                11
            )
            previsao = prever_energia(
                vento,
                dados["historico_vento"],
                dados["historico_energia"]
            )
            print(
                f"\nPrevisão de geração para vento = {vento}: "
                f"{previsao:.2f} unidades de energia."
            )

        elif opcao == "4":
            exibir_estrutura(dados)

        elif opcao == "0":
            print("\nSistema encerrado. Obrigado por utilizar!")
            break

        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    executar()
