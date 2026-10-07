from google.adk.agents.llm_agent import LlmAgent

root_agent = LlmAgent(
    name="meu_agente2",
    description="Agente 2 especialista em Python.",
    instruction="""
        Escreva um códigho Python que imprima 'Olá, Mundo!' usando a função print().
        Certifique-se de que o código seja simples e fácil de entender.
    """,
   model="gemini-3.5-flash-lite"
)

