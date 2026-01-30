def classify_email(text: str) -> str:
    text = text.lower()

    productive_keywords = [
        "erro",
        "problema",
        "suporte",
        "status",
        "solicitação",
        "pedido",
        "dúvida",
        "atualização",
        "requerimento",
        "acesso"
    ]

    for word in productive_keywords:
        if word in text:
            return "Produtivo"

    return "Improdutivo"
