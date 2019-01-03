from flask import Flask, jsonify, request
from app.models import Incident
from datetime import datetime
from marshmallow import Schema, fields,ValidationError
from app.validator import email, required

app = Flask(__name__)


redflags_list = []



class RedflagSchema(Schema):
    #Represents the schema for redflags
    type = fields.Str(required=False)
    comment = fields.Str(required=True, validate=(required))
    location = fields.Str(required=True, validate=(required))
    id = fields.Int(required=False)
    createdOn = fields.Str(required=False)
    createdBy = fields.Int(required=False)
    Images = fields.Str(required=False)
    status = fields.Str(required=False)
    Videos = fields.Str(required=False)


@app.route('/api/v1/red-flags', methods=['POST'])
def create_redflag():
    # function for creating a red-flag
    data, errors = RedflagSchema().load(request.get_json())
    
    if errors:
            return jsonify({
              "errors": errors, 
              "status": 422})

    id = len(redflags_list)+1
    createdOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    createdBy = id = len(redflags_list)+1
    status = "draft"
    type = "red-flag"
    red_flag = Incident(id, createdOn, createdBy, type, data['location'],
               status, data['Images'], data['Videos'], data['comment'])

    redflags_list.append(red_flag)

    return jsonify({
         "status": 201,
        "data": [{
        "id": id,
        "message": "Created red-flag record"
        }]
    })
