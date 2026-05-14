
def display_menuinicial():
    print("\n=== SISTEMA DE VENDAS ===")
    print("\n1 - Registrar venda"
          "\n2 - Ver resumo parcial"
          "\n3 - Encerrar sistema"
    )


def get_cont_vendas(vendas: int):
    global cont_vendas
    cont_vendas += vendas
    return cont_vendas


def get_acum_vlr_bruto(vlr_bruto: float):
    global acum_vlr_bruto
    acum_vlr_bruto += vlr_bruto
    return acum_vlr_bruto


def get_acum_vlr_desc(vlr_desc: float):
    global acum_vlr_desc
    acum_vlr_desc += vlr_desc
    return acum_vlr_desc


def get_acum_vlr_bruto_desc(vlr_bruto_desc: float):
    global acum_vlr_bruto_desc
    acum_vlr_bruto_desc += vlr_bruto_desc
    return acum_vlr_bruto_desc


def get_vlr_bruto(vlr_unit: float, vlr_qtd: int):
    return vlr_unit * vlr_qtd


def get_desc(vlr_bruto: float):
    if vlr_bruto < 100:
        return 0.00
    if vlr_bruto < 499.99:
        return 0.05
    if vlr_bruto <999.99:
        return 0.10
    return 0.15


def get_vlr_desc(desc: float, vlr_bruto: float):
    return desc * vlr_bruto


def get_vlr_bruto_desc(vlr_bruto: float, vlr_desc: float):
    return vlr_bruto - vlr_desc


def get_registrarvenda():
    vendas = 1
    nome_prod = str(input("\nNome do produto: "))
    vlr_unit = float(input("Valor unitário: "))
    vlr_qtd = int(input("Quantidade: "))
    vlr_bruto = get_vlr_bruto(vlr_unit, vlr_qtd)
    desc = get_desc(vlr_bruto)
    vlr_desc = get_vlr_desc(desc, vlr_bruto)
    vlr_bruto_desc = get_vlr_bruto_desc(vlr_bruto, vlr_desc)
    get_cont_vendas(vendas)
    get_acum_vlr_bruto(vlr_bruto)
    get_acum_vlr_desc(vlr_desc)
    get_acum_vlr_bruto_desc(vlr_bruto_desc)
    result1 = print(f"\nNome do produto: {nome_prod}"
                   f"\nValor unitário: R$ {vlr_unit:.2f}"
                   f"\nQuantidade: {vlr_qtd:.0f}"
                   f"\n\nValor Bruto da venda: R$ {vlr_bruto:.2f}"
                   f"\nDesconto aplicado: {(100*(desc)):.2f}%"
                   f"\nValor do desconto: R$ {vlr_desc:.2f}"
                   f"\nValor final da venda: R$ {vlr_bruto_desc:.2f}"
                   "\nVenda registrada com sucesso!"
                   )
    return result1


def get_resumoparcial():
    result2 = print("\n=== RESUMO PARCIAL ==="
                    f"\n\nTotal de vendas realizadas: R$ {cont_vendas:.0f}"
                    f"\nTotal bruto vendido: R$ {acum_vlr_bruto:.2f}"
                    f"\nTotal de descontos concedidos: R$ {acum_vlr_desc:.2f}"
                    f"\nTotal líquido vendido: R$ {acum_vlr_bruto_desc:.2f}"
                    )
    return result2


def get_resumofinal():
    result3 = print("\n=== RESUMO FINAL ==="
                    f"\n\nTotal de vendas realizadas: R$ {cont_vendas:.0f}"
                    f"\nTotal bruto vendido: R$ {acum_vlr_bruto:.2f}"
                    f"\nTotal de descontos concedidos: R$ {acum_vlr_desc:.2f}"
                    f"\nTotal líquido vendido: R$ {acum_vlr_bruto_desc:.2f}"
                    "\n\nSistema encerrado."
                    )
    return result3


def display_uxui():
    while True:
        try:
            display_menuinicial()
            opcao = int(input("\nEscolha uma opção: "))
            if opcao == 1:
                get_registrarvenda()
                continue
            if opcao == 2:
                get_resumoparcial()
                continue
            if opcao == 3:
                get_resumofinal()
                break
        except ValueError:
            print("Opção inválida. Tente novamente.")


cont_vendas = 0
acum_vlr_bruto = 0
acum_vlr_desc = 0
acum_vlr_bruto_desc = 0


display_uxui()
