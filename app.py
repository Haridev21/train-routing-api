from flask import Flask, request, jsonify
import json
from dijkstra import dijkstra
import os

app = Flask(__name__)

# Load graph from file
GRAPH_FILE = "graph_adjacency_list.json"
if not os.path.exists(GRAPH_FILE):
    raise FileNotFoundError(f"{GRAPH_FILE} not found")

with open(GRAPH_FILE, "r") as f:
    graph = json.load(f)

@app.route("/shortest-path", methods=["POST"])
def shortest_path():
    data = request.json
    if not data or "source" not in data or "destination" not in data:
        return jsonify({"error": "Missing source or destination"}), 400

    source = data["source"]
    destination = data["destination"]

    try:
        result = dijkstra(graph, source, destination)
    except KeyError:
        return jsonify({"error": "Invalid node in graph"}), 400

    return jsonify(result)

if __name__ == "__main__":
    # Use PORT environment variable if provided (Render sets this automatically)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
