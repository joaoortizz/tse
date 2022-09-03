import requests as rq
import json
import unidecode




if __name__ == '__main__':

    headers = {
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0",
    }

    # create a session
    session = rq.Session()

    uri = f"https://divulgacandcontas.tse.jus.br/divulga/rest/v1/candidatura/buscar/2022/BR/2040602022/candidato/280001607829"
    response = session.get(url=uri, headers=headers)

    candidate_info = json.loads(response.text)
    print(candidate_info['nomeCompleto'])
    print(json.dumps(candidate_info, indent=4, ensure_ascii=False).encode('utf8').decode())
    # with open(f"TEST_DECODE.json", "w") as f:
    #     # f.write(json.dumps(candidate_info, indent=4).encode(encoding='ascii').decode(encoding='latin-1'))
    #     f.write(json)
