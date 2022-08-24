import requests as rq
import json
import unidecode

headers = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0",
    }

# create a session
session = rq.Session()

def get_candidates_list(session):
    listar_candidatos = "https://divulgacandcontas.tse.jus.br/divulga/rest/v1/candidatura/listar/2022/BR/2040602022/1/candidatos"
    response = session.get(listar_candidatos, headers=headers)
    candidatos = json.loads(response.text)
    
    return candidatos

def get_candidate_info(session, candidate_id):
    uri = f"https://divulgacandcontas.tse.jus.br/divulga/rest/v1/candidatura/buscar/2022/BR/2040602022/candidato/{candidate_id}"
    response = session.get(url=uri,headers=headers)

    return json.loads(response.text)

# save candidatos into a file
candidatos = get_candidates_list(session)

with open("candidatos/candidatos.json", "w") as f:
    f.write(json.dumps(candidatos["candidatos"], indent=4))

# read candidates from file and get the list of ids
with open("candidatos/candidatos.json", "r") as f:
    candidatos = json.loads(f.read())

# write the candidate data to a json file
for candidato in candidatos:
    candidato_info = get_candidate_info(session, candidato['id'])
    file_name = unidecode.unidecode(f"{candidato_info['numero']}_{candidato_info['nomeUrna'].lower().replace(' ', '_')}")
    # print(candidato_info)
    with open(f"candidatos/{file_name}.json", "w") as f:
        f.write(json.dumps(candidato_info, indent=4))

