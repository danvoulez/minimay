def parse_text_to_logline(text: str) -> dict:
    parts = text.split(',')
    logline = {
        'who': parts[0].strip() if len(parts) > 0 else 'unknown',
        'did': parts[1].strip() if len(parts) > 1 else 'reported',
        'this': parts[2].strip() if len(parts) > 2 else text,
        'when': parts[3].strip() if len(parts) > 3 else '',
        'confirmed_by': parts[4].strip() if len(parts) > 4 else '',
        'if_ok': parts[5].strip() if len(parts) > 5 else '',
        'if_doubt': parts[6].strip() if len(parts) > 6 else '',
        'if_not': parts[7].strip() if len(parts) > 7 else '',
        'status': parts[8].strip() if len(parts) > 8 else 'pending'
    }
    return logline


def interpretar_frase(frase: str) -> dict:
    """Alias semântico para `parse_text_to_logline`.

    A função original continua existindo para compatibilidade
    com os testes, mas o sistema pode invocar este nome mais
    descritivo conforme definido nos prompts institucionais.
    """
    return parse_text_to_logline(frase)
