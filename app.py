from flask import Flask, jsonify, render_template, request, Game, app
game = Game()

@app.route("/")
def index():
    return render_template("index.html", grid_size=game.grid_size)

@app.route("/state")
def state():
    return jsonify
    ({"snake": game.snake.body,
        "food": game.food.position,
        "score" game.score,
        "game_over" game.game_over,})
    
@app.route("/move", methods=["POST"])
def move():
    direction = request.json.get("direction")
    game.change_direction(direction)
    return jsonify(success=True)

@app.route("/tick")
def tick():
    game.update()
    return jsonify(success=True)

@app.route("/restart")
def restart():
    global game
    game = Game()
    return jsonify(success=True)

if __name__ == "__main__":
    app.run(debug=True)