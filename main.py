
def display_menuinicial():
    print("\n=== SISTEMA DE VENDAS ===")
    print("\n1 - Registrar venda"
      "\n2 - Ver resumo parcial"
      "\n3 - Encerrar sistema"
    )


def cont_vendas(vendas: int):
    vendas = vendas + 1
    return vendas


def get_acum_vlr_bruto(vlr_bruto: float):
    acum_vlr_bruto += vlr_bruto
    return acum_vlr_bruto


def get_acum_vlr_desc(vlr_desc: float):
    acum_vlr_desc += vlr_desc
    return acum_vlr_desc


def get_acum_vlr_bruto_desc(vlr_bruto_desc: float):
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
    nome_prod = str(input("\nNome do produto: "))
    vlr_unit = float(input("Valor unitário: "))
    vlr_qtd = int(input("Quantidade: "))
    vlr_bruto = get_vlr_bruto(vlr_unit, vlr_qtd)
    desc = get_desc(vlr_bruto)
    vlr_desc = get_vlr_desc(desc, vlr_bruto)
    vlr_bruto_desc = get_vlr_bruto_desc(vlr_bruto, vlr_desc)
    cont_vendas()
    get_acum_vlr_bruto(vlr_bruto)
    get_acum_vlr_desc(vlr_desc)
    get_acum_vlr_bruto_desc(vlr_bruto_desc)
    result = print(f"\nNome do produto: {nome_prod}"
                   f"\nValor unitário: R$ {vlr_unit:.2f}"
                   f"\nQuantidade: {vlr_qtd:.0f}"
                   f"\n\nValor Bruto da venda: R$ {vlr_bruto:.2f}"
                   f"\nDesconto aplicado: {(100*(desc)):.2f}%"
                   f"\nValor do desconto: R$ {vlr_desc:.2f}"
                   f"\nValor final da venda: R$ {vlr_bruto_desc:.2f}"
                   "\nVenda registrada com sucesso!"
                   )
    return result


def get_resumoparcial():
    print("\n=== RESUMO PARCIAL ===")


def get_resumofinal():
    print("\n=== RESUMO FINAL ===")

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
            print("Opção Inválida! Por favor digite um número conforme as opções válidas.")


vendas = 0
acum_vlr_bruto = 0
acum_vlr_desc = 0
acum_vlr_bruto_desc = 0

display_uxui()