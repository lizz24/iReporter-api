from flask import Flask, jsonify, request
from app.models.incident import Incident
from datetime import datetime
from app.validators.incident_schema import IncidentSchema

app = Flask(__name__)


incident_list = []

@app.route('/api/v1/red-flags', methods=['POST'])
def create_redflag():
    # function for creating a red-flag
    data, errors = IncidentSchema().load(request.get_json())
    
    if errors:
            return jsonify({
              "errors": errors, 
              "status": 422})

    id = len(incident_list)+1
    createdOn = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    createdBy = id = len(incident_list)+1
    status = "draft"
    type = "red-flag"
    red_flag = Incident(id, createdOn, createdBy, type, data['location'],
               status, data['Images'], data['Videos'], data['comment'])

    incident_list.append(red_flag)

    return jsonify({
         "status": 201,
        "data": [{
        "id": id,
        "message": "Created red-flag record"
        }]
    })
