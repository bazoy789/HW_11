import json

def load_candidates_from_json():
    with open('candidates.json', encoding='UTF-8') as file:
        return json.load(file)


def get_candidate(candidate_id):
    for candidate in load_candidates_from_json():
        if candidate_id == candidate['id']:
            return candidate
    return "Кандидат не найден"


def get_candidates_by_name(candidate_name):
    coincidence = []
    for candidate in load_candidates_from_json():
        if candidate_name.lower() in candidate['name'].lower():
            coincidence.append(candidate)
    return coincidence



def get_candidates_by_skill(skill_name):
    skill_list = []
    for candidate in load_candidates_from_json():
        if skill_name.lower() in candidate['skills'].lower().split(', '):
            skill_list.append(candidate)
    if skill_list == []:
        return "Кандидат не найден"
    return skill_list
