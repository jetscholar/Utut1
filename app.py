from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/addTwo', methods=["POST"])
def addTwo():
    # Get the data from the POST
    dataDict = request.get_json()
    x = dataDict['x']
    y = dataDict['y']

    z = x + y

    retJson = {
        "z": z
    }

    return jsonify(retJson), 200

@app.route('/json')
def json_donuts():
    id = 14001
    retJson = {
                "id": id,
                "type": "donut",
                "name": "Cake",
                "ppu": 0.55,
                "batters":
                    {
                        "batter":
                            [
                                { "id": "1001", "type": "Regular" },
                                { "id": "1002", "type": "Chocolate" },
                                { "id": "1003", "type": "Blueberry" }, 
                                { "id": "1004", "type": "Devil's Food" }
                            ]
                    },
                "topping":
                    [
                        { "id": "5001", "type": "None" },
                        { "id": "5002", "type": "Glazed" },
                        { "id": "5005", "type": "Sugar" },
                        { "id": "5007", "type": "Powdered Sugar" },
                        { "id": "5006", "type": "Chocolate with Sprinkles" },
                        { "id": "5003", "type": "Chocolate" },
                        { "id": "5004", "type": "Maple" }
                    ]
    }
    return jsonify(retJson)


if __name__=="__main__":
    app.run(debug=True)