from backend.llm_service import parse_text_to_logline, interpretar_frase

def test_parse_text():
    text = 'alice,fez,algo,2021-01-01,ok,sim,dúvida,não,pendente'
    logline = parse_text_to_logline(text)
    assert logline['who'] == 'alice'
    assert logline['did'] == 'fez'
    assert logline['this'] == 'algo'

def test_interpretar_frase():
    frase = 'bob,construiu,algo,2022-02-02,ok,sim,dúvida,não,pendente'
    logline = interpretar_frase(frase)
    assert logline['who'] == 'bob'
    assert logline['did'] == 'construiu'
    assert logline['this'] == 'algo'
