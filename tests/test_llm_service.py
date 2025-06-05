import unittest
from backend.llm_service import parse_text_to_logline, interpretar_frase

SAMPLE = 'alice,fez,algo,2021-01-01,bob,ok,duvida,nao,pendente'


def _check_fields(logline):
    assert logline['who'] == 'alice'
    assert logline['did'] == 'fez'
    assert logline['this'] == 'algo'
    assert logline['when'] == '2021-01-01'
    assert logline['confirmed_by'] == 'bob'
    assert logline['if_ok'] == 'ok'
    assert logline['if_doubt'] == 'duvida'
    assert logline['if_not'] == 'nao'
    assert logline['status'] == 'pendente'


class LLMServiceTest(unittest.TestCase):
    def test_parse_text(self):
        logline = parse_text_to_logline(SAMPLE)
        _check_fields(logline)

    def test_interpretar_frase_alias(self):
        logline = interpretar_frase(SAMPLE)
        _check_fields(logline)


if __name__ == '__main__':
    unittest.main()
