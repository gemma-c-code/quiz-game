import json

FILE = "leaderboard.json"

def load_leaderboard():
    try:
        with open(FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return []
def save_leaderboard(data):
    with open(FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
def add_score(name, score):
    leaderboard = load_leaderboard()

    leaderboard.append({"name": name, "score": score})

    leaderboard.sort(key=lambda x: x["score"], reverse=True)

    save_leaderboard(leaderboard)

def get_top_scores(limit=5):
    leaderboard = load_leaderboard()
    return leaderboard[:limit]
