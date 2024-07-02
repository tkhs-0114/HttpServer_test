from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route("/", methods=['GET','POST'])
def Test():
    if request.method == 'GET':
        return 'OK'
    else:
        data = request.get_json()
        return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)