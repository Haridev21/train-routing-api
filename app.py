from flask import Flask, request, jsonify
import json
from dijkstra import dijkstra

app = Flask(__name__)

# Load graph
with open("graph_adjacency_list.json", "r") as f:
    graph = json.load(f)

@app.route("/shortest-path", methods=["POST"])
def shortest_path():
    data = request.json
    source = data["source"]
    destination = data["destination"]

    result = dijkstra(graph, source, destination)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
