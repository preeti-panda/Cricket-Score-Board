from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/submit_score', methods=['POST'])
def submit_score():
    team_name = request.form.get('team')
    batsman_name = request.form.get('batsman-name')
    
    ones = int(request.form.get('ones', 0))
    fours = int(request.form.get('fours', 0))
    sixes = int(request.form.get('sixes', 0))
    balls = int(request.form.get('balls', 0))
    
    bowler_name = request.form.get('bowler-name')
    runs_given = int(request.form.get('runs-given', 0))
    overs = float(request.form.get('overs', 0))
    wickets = int(request.form.get('wickets', 0))
    
    runs_team1 = int(request.form.get('runs_team1', 0))
    runs_team2 = int(request.form.get('runs_team2', 0))
    
    total_runs = (ones * 1) + (fours * 4) + (sixes * 6)

    if runs_team1 > runs_team2:
        result = f"{team_name} won the match!"
    elif runs_team1 < runs_team2:
        result = "Opponent team won the match!"
    else:
        result = "The match is a tie!"

    return f"""
    <h2>Match Summary</h2>
    <p><b>Team:</b> {team_name}</p>
    <p><b>Batsman:</b> {batsman_name} - {total_runs} runs in {balls} balls</p>
    <p><b>Bowler:</b> {bowler_name} - {wickets} wickets, {runs_given} runs in {overs} overs</p>
    <p><b>Final Score:</b> Team 1: {runs_team1}, Team 2: {runs_team2}</p>
    <h3>{result}</h3>
    """

if __name__ == "__main__":
    app.run(debug=True)
