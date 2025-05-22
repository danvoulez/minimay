from backend.llm_service import parse_text_to_logline

def test_parse_text():
    text = 'alice,fez,algo,2021-01-01,ok,sim,dúvida,não,pendente'
    logline = parse_text_to_logline(text)
    assert logline['who'] == 'alice'
    assert logline['did'] == 'fez'
    assert logline['this'] == 'algo'
