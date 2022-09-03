import requests as rq
import json
import unidecode


def get_candidates_list(session):
    """
    Get the list of all the candidates for the current session.
    :param:
        - session: object
    :return:
        - candidates: json
    """
    
    candidates_list = "https://divulgacandcontas.tse.jus.br/divulga/rest/v1/candidatura/listar/2022/BR/2040602022/1/candidatos"
    response = session.get(candidates_list, headers=headers)
    candidates = json.loads(response.text)

    return candidates


def get_candidate_info(session, candidate_id):
    """
    Get information about a candidate.
    :param:
        - session: object
        - candidate_id:
    :return:
        - response: json
    """

    uri = f"https://divulgacandcontas.tse.jus.br/divulga/rest/v1/candidatura/buscar/2022/BR/2040602022/candidato/{candidate_id}"
    response = session.get(url=uri, headers=headers)

    return json.loads(response.text)


if __name__ == '__main__':

    headers = {
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0",
    }

    # create a session
    session = rq.Session()

    # save candidates into a file
    candidates = get_candidates_list(session)
    print(candidates)

    try:
        with open("candidates.json", "w") as f:
            f.write(json.dumps(candidates["candidatos"], indent=4))

        # read candidates from file and get the list of ids
        with open("candidates.json", "r") as f:
            candidates = json.loads(f.read())

    except Exception as e:
        print(f'Exception: {e}')

    # write the candidate data to a json file
    for candidate in candidates:
        candidate_info = get_candidate_info(session, candidate['id'])
        file_name = unidecode.unidecode(
            f"{candidate_info['numero']}_{candidate_info['nomeUrna'].lower().replace(' ', '_')}")

        with open(f"candidates/{file_name}.json", "w") as f:
            f.write(json.dumps(candidate_info, indent=4, ensure_ascii=False).encode('utf8').decode())
