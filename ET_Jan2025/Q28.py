from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the IITM BS Cricket Match Scoreboard!"

@app.route('/score/<team>') #students
def team_score(team):
    scores = {"students": 120, "instructors": 115}
    return f"{team.capitalize()} Score: {scores.get(team, 'Team not found')}"

@app.route('/score/<team>/<player>') #instructors/Dr.Prashant
def player_score(team, player):
    players = {
    "students": {"Rahul": 45, "Ananya": 30, "Karthik": 25},
    "instructors": {"Prof.Prashant": 40, "Prof.Mayur": 35,
    "Dr.Subendu": 20}
    }
    return f"{player} ({team.capitalize()}) Scored: {players.get(team,
    {}).get(player, 'Player not found' )}"

if __name__ == '__main__':
    app.run(debug=True)