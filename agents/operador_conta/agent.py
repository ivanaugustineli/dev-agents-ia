from google.adk.agents.llm_agent import LlmAgent

FATURAS = [
  {
    "id": "FAT-2023-001",
    "cliente_id": "1001",
    "cliente": "Empresa Alfa Ltda",
    "cnpj_cpf": "12.345.678/0001-90",
    "data_emissao": "2023-10-01",
    "data_vencimento": "2023-10-15",
    "valor": 1500.00,
    "moeda": "BRL",
    "status": "pago",
    "descricao": "Serviços de consultoria em TI"
  },
  {
    "id": "FAT-2023-002",
    "cliente_id": "1001",
    "cliente": "Empresa Alfa Ltda",
    "cnpj_cpf": "123.456.789-00",
    "data_emissao": "2023-10-05",
    "data_vencimento": "2023-10-20",
    "valor": 350.50,
    "moeda": "BRL",
    "status": "pago",
    "descricao": "Assinatura mensal de software SaaS"
  },
  {
    "id": "FAT-2023-003",
    "cliente_id": "1002",
    "cliente": "Beta Tecnologia S.A.",
    "cnpj_cpf": "98.765.432/0001-10",
    "data_emissao": "2023-10-10",
    "data_vencimento": "2023-11-10",
    "valor": 5200.00,
    "moeda": "BRL",
    "status": "pendente",
    "descricao": "Desenvolvimento de plataforma web - Parcela 1/3"
  },
  {
    "id": "FAT-2023-004",
    "cliente_id": "1003",
    "cliente": "Beta Tecnologia S.A.",
    "cnpj_cpf": "987.654.321-11",
    "data_emissao": "2023-10-12",
    "data_vencimento": "2023-10-25",
    "valor": 120.00,
    "moeda": "BRL",
    "status": "atrasado",
    "descricao": "Suporte técnico remoto avulso"
  },
  {
    "id": "FAT-2023-005",
    "cliente_id": "1003",
    "cliente": "Beta Tecnologia S.A.",
    "cnpj_cpf": "45.678.901/0001-22",
    "data_emissao": "2023-10-15",
    "data_vencimento": "2023-11-15",
    "valor": 2800.00,
    "moeda": "BRL",
    "status": "pendente",
    "descricao": "Campanha de Marketing Digital - Outubro"
  }
]

def listar_faturas(cliente_id: str):
    """
    Retorna as faturas de um cliente específico.
 
    Args:
        cliente_id (str): ID do cliente.
        
    Returns:
        dict: Dicionário contendo as faturas do cliente.
    """
    faturas_cliente = [fatura for fatura in FATURAS if fatura["cliente_id"] == cliente_id]
    return faturas_cliente

root_agent = LlmAgent(
    name="operador_conta",
    description="Agente Operador de Contas.",
    instruction="""
      Você é o atendente de conta interativo das Lojas Acme.
      Você é responsável por:
        - Informar ao cliente sobre sua assinatura: o plano, status, renovação.
        - Tirar dúvidas sobre as faturas do cliente.
        - Cancelar a assinatura do cliente, se solicitado.
      O usuário precisa fornecer o ID do cliente para que você possa buscar as informações corretas.
      Seja cordial e direto.
    """,
    model="gemini-3.5-flash-lite",
    tools=[listar_faturas]
)

