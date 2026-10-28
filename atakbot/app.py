# 1. CARREGAR OS DADOS
import pandas as pd
dados = pd.read_csv("dados/visita_atak.csv")
#print(dados)

#print(dados.head)
#print(dados.head(3))
#print(dados.shape)
#print(dados.columns)

# 2. REMOVER DADOS PESSOAIS
colunas_privadas = [
    "Carimbo de data/hora",
    "Endereço de e-mail",
    "Nome Completo"
]

dados = dados.drop(
    columns=colunas_privadas,
    errors="ignore"
)

dados.columns = dados.columns.str.strip()
# 3. DEFINIR OS TEMAS
temas={
    "ramo":
    "Qual o principal ramo de atuação da ATAK?",

    "tecnologias":
    "Durante a visita, quais tecnologias ou áreas relacionadas "
    "à Inteligência Artificial foram apresentadas?",

    "aplicacoes":
    "Qual foi a principal aplicação de Inteligência Artificial "
    "que você observou ou conheceu durante a visita?",

    "contribuicoes":
    "Qual é uma das principais contribuições da Inteligência "
    "Artificial para as empresas?",

    "produtividade":
    "Se respondeu \"Sim\", explique qual a situação",

    "competencias":
    "Quais competências profissionais você percebeu que são "
    "importantes para trabalhar com tecnologia e Inteligência Artificial?",

    "ideias":
    "Após a visita, você consegue imaginar alguma aplicação de IA "
    "que poderia ser desenvolvida por você ou sua equipe?",

    "aprendizado":
    "O que você aprendeu durante a visita que não conhecia antes?",

    "profissoes":
    "A visita ajudou você a compreender melhor as possibilidades "
    "profissionais relacionadas à Inteligência Artificial?",

    "prompt":
    "Qual é a importância do conhecimento sobre Prompts/Engenharia "
    "de Prompt para um profissional que utiliza Inteligência Artificial?",
}
# 4. BUSCAR RESPOSTAS NO CSV

def buscar_respostas(coluna) :
    respostas = dados[coluna].dropna()
    respostas = respostas.drop_duplicates()
    return respostas.tolist()
#
#respostas=buscar_respostas(temas["competencias"])

# pergunta =input("Você: ")
# print("Você perguntou:", pergunta)
# pergunta=pergunta.lower()

# if "produtividade" in pergunta:
#     print("Você perguntou sobre produtividade.")

# elif "prompt" in pergunta:
#     print("Você perguntou sobre Engenharia de Prompt.")

# elif "competência" in pergunta:
#     print("Você perguntou sobre competências profissionais.")

# else:
#     print("Não consegui identificar o assunto.")

# 5. PALAVRAS-CHAVE DE CADA TEMA
palavras_por_tema = {
    "tecnologias": [
        "tecnologia",
        "tecnologias",
        "ferramenta",
        "ferramentas",
        "recurso"
    ],

    "produtividade": [
        "produtividade",
        "produção",
        "producao",
        "eficiência",
        "eficiencia"
    ],

    "competencias": [
        "competência",
        "competencia",
        "habilidade",
        "habilidades"
    ],

    "prompt":[
        "prompt",
        "prompts",
        "engenharia de prompt"
    ],

    "aprendizado": [
        "aprendeu",
        "aprendizado",
        "aprenderam"
    ],

    "profissoes": [
        "profissão",
        "profissao",
        "profissões",
        "profissoes",
        "carreira"
    ]
}
# 6. IDENTIFICAR O ASSUNTO
def identificar_tema(pergunta):

    pergunta = pergunta.lower()

    for tema, palavras in palavras_por_tema.items():

        for palavra in palavras:

            if palavra in pergunta:
                return tema
    return None
# def identificar_tema(pergunta):

#     pergunta = pergunta.lower()

#     if "produtividade" in pergunta:
#         return "produtividade"

#     elif "prompt" in pergunta:
#         return "prompt"

#     elif "competência" in pergunta or "competencia" in pergunta:
#         return "competencias"

#     elif "tecnologia" in pergunta:
#         return "tecnologias"

#     elif "aplicação" in pergunta or "aplicacao" in pergunta:
#         return "aplicacoes"

#     elif "profissão" in pergunta or "profissao" in pergunta:
#         return "profissoes"

#     elif "aprendeu" in pergunta or "aprendizado" in pergunta:
#         return "aprendizado"

#     elif "ideia" in pergunta:
#         return "ideias"

#     else:
#         return None

# pergunta = input("Você: ")

# tema = identificar_tema(pergunta)

# if tema is not None:
#     coluna = temas [tema]
#     respostas = buscar_respostas(coluna)

#     for resposta in respostas:

#         print("-", resposta)
# else:
#     print("ATAKbot: Não encontrei esse assunto.")

# 7. MOSTRAR RESPOSTAS
def mostrar_respostas(respostas, limite=5):

    for resposta in respostas[:limite]:
        print("-", resposta)
# MENU DE AJUDA
def mostrar_ajuda():
    print("\nATAKBot: Eu posso responder sobre:")
    print("- tecnologias e ferramentas")
    print("- produtividade")
    print("- competências")
    print("- prompts")
    print("- o que os alunos aprenderam")
    print("- profissões")
    print("- Digite 'quantos' e 'profissões' para ver a contagem")
    print("- Digite 'sair' para encerrar")
# 8. RESUMO COM CONTAGEM (ETAPA 21)
def resumo_profissoes():

    coluna = temas["profissoes"]

    contagem = dados[coluna].dropna().value_counts()

    print("\nATAKBot:")
    print("Resultado das respostas:")

    for resposta, quantidade in contagem.items():
        print(f"{resposta}: {quantidade}")

# 9. RESPONDER AO USUÁRIO
def responder(pergunta):
    texto = pergunta.lower()
    if texto == "ajuda":
        mostrar_ajuda()
        return
    if "quantos" in texto and "profiss" in texto:
        resumo_profissoes()
        return
    tema = identificar_tema(pergunta)

    if tema is None:
        print(
            "ATAKBot: Não encontrei informações "
            "suficientes no CSV para responder."
        )
        return

    coluna = temas[tema]

    if coluna not in dados.columns:
        print(
        "ATAKBot: A coluna necessária não foi "
        "encontrada no arquivo."
    )
        return

    respostas = buscar_respostas(coluna)

    print("\nATAKBot:")
    print("Encontrei estas informações:")

    mostrar_respostas(respostas)

# 10. PROGRAMA PRINCIPAL
while True:
    pergunta = input("\nVocê: ")

    if pergunta.lower() == "sair":
        print("ATAKBot: Até a próxima!")
        break
    responder(pergunta)