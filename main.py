from flask import Flask, render_template
import units

app = Flask(__name__)

@app.route('/')
def all_candidate():
    candidates = units.load_candidates_from_json()
    return render_template('all_candidate.html', candidates=candidates)


@app.route('/candidate/<int:id>')
def candidate(id):
    candidate = units.get_candidate(id)
    return render_template('candidate.html', candidate=candidate)

@app.route('/search/<name>')
def search(name):
    candidate = units.get_candidates_by_name(name)
    candidate_count = len(candidate)
    if candidate == []:
        return 'Нет такого имени в списке кандидатов'
    return render_template('candidate_name.html', candidate=candidate, candidate_count=candidate_count)

@app.route('/skill/<skill>')
def candidate_skyll(skill):
    candidate = units.get_candidates_by_skill(skill)
    skill_count = len( candidate )
    if candidate == []:
        return "Нет таких skills"
    return render_template('candidate_skill.html', candidate=candidate, skill_count=skill_count, skill=skill)
app.run()