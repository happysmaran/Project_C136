from flask import Flask, jsonify, request
from data import data

app=Flask(__name__)
@app.route("/")

def index():
    '''The Flask API displayer'''
    return jsonify({
        "data":data,
        "message":"success"
        })

@app.route("/planet")
def planet():
    '''Retreives the data for each planet'''
    name=request.args.get("name")
    planet_data=next(item for item in data if item["name"]==name)
    return jsonify({
        "data":planet_data,
        "message":"success"
        })

if __name__ == "__main__":
    app.run()
