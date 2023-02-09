from uuid import uuid4
from flask import Flask, make_response, request
import dbhelpers as dh
import apihelpers as a
import json
import dbcreds as d





app = Flask(__name__)

@app.post('/api/client')
def question_by_id():    
    valid_check=a.check_endpoint_info(request.json, ['id'])
    if (valid_check != None):
        return make_response(json.dumps(valid_check, default=str), 400)
    result = dh.run_statement('CALL search_question_by_id(?)', [request.json.get('id')])

    if (type(result) == list):
        return make_response(json.dumps(result, default=str), 200)
    else:
        return make_response(json.dumps(result, default=str), 400)

@app.get('/api/client')
def show_all():
    result = dh.run_statement('CALL show_all()')

    if (type(result) == list):
        print(result, "here is line 37 --------------")
        dh.create_dictionary_randomization(result)
        return make_response(json.dumps(result, default=str), 200)
    else:
        return make_response(json.dumps(result, default=str), 400)
    
@app.post('/api/clients')
def add_new_question():

    valid_check=a.check_endpoint_info(request.json, ['question', 'answer_1', 'answer_2', 'answer_3', 'answer_4'])
    if (valid_check != None):
        return make_response(json.dumps(valid_check, default=str), 400)
    
    result = dh.run_statement('CALL add_question(?,?,?,?,?)', [request.json.get('question'), request.json.get('answer_1'), request.json.get('answer_2'), request.json.get('answer_3'), request.json.get('answer_4')])

    if (type(result) == list):
        return make_response(json.dumps(result, default=str), 200)
    else:
        return make_response(json.dumps(result, default=str), 400)
    



if (d.production_mode == True):
    print("Running in Production Mode")
    import bjoern #type:ignore
    bjoern.run(app, "0.0.0.0", 5000)
    app.run(debug=True)
else:
    from flask_cors import CORS
    CORS(app)
    print("Running in Testing Mode")
    app.run(debug=True)