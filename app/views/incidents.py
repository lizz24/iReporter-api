from flask import Flask, jsonify, request
from app.models.incident import Incident
from datetime import datetime
from app.validators.incident_schema import IncidentSchema

app = Flask(__name__)


incident_list = []

@app.route('/', methods=['GET'])
def home():
    return "WELCOME TO IREPORTER"

@app.route('/api/v1/red-flags', methods=['POST'])
def create_redflag():
    """ function for creating a red-flag"""
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
        "message": "Created red-flag record sucessfully"
        }]
    })

@app.route('/api/v1/red-flags', methods=['GET'])
def get_redflags():
    """ getting all red-flags"""
    Redflags = [incident.get_incident() for incident in incident_list]
    if len(incident_list) > 0:
     return jsonify({
         "data": Redflags,
         "status" : 200
        })
    else:
     return jsonify({
             "error": "Empty redflag list",
             "status": 404
             }), 404

@app.route('/api/v1/red-flags/<int:redflag_id>', methods=['GET'])
def get_single_redflag(redflag_id):
    """ function for getting a single redflag"""
    if redflag_id == 0 or redflag_id > len(incident_list):
        return jsonify({"error": "No recorded redflags to display, please create redflag"}), 400
    else:
        redflag = []
        incident = incident_list[redflag_id - 1]
        redflag.append(incident.get_incident())
    return jsonify({
                        "data": redflag,
                        "status": 200
                        })

@app.route('/api/v1/red-flags/<int:redflag_id>/location', methods=['PATCH'])
def edit_redflag_location(redflag_id):
    """ function for editing redflag location"""
    if redflag_id == 0 or redflag_id > len(incident_list):
        return jsonify({"error": "Redflag record id doesnot exist"}), 404
    data = (request.get_json())
    for incident in incident_list:
        if int(incident.id) == int(redflag_id):
            incident.location = data['location']
            return jsonify({
                "status": 200,
                "data": [{
                "id": redflag_id,
                "message": "Updated red-flag record’s location"
                }]
                })
        


@app.route('/api/v1/red-flags/<int:redflag_id>/comment', methods=['PATCH'])
def edit_redflag_comment(redflag_id):
    """ function for editing redflag comment"""
    if redflag_id == 0 or redflag_id > len(incident_list):
        return jsonify({"error": "The redflag record id doest exist"}), 404
    data = (request.get_json())
    for incident in incident_list:
        if int(incident.id) == int(redflag_id):
            incident.comment = data['comment']
            return jsonify({
                "status": 200,
                "data": [{
                "id": redflag_id,
                "message": "Updated red-flag record’s comment"
                }]
                })
      
@app.route('/api/v1/red-flags/<int:redflag_id>', methods=['DELETE'])
def delete_redflag(redflag_id):
    """ deleting a redflag"""
    if redflag_id == 0 or redflag_id > len(incident_list):
        return jsonify({"message": "redflag record out of range"}), 404
    for incident in incident_list:
        if incident.id == redflag_id:
            incident_list.remove(incident)
    return jsonify({
        "status": 200,
        "data":[{
        "id": redflag_id,
        "message": "red-flag record id has been deleted"
        }]
        })

@app.errorhandler(405)
def bad_method(error):
    return jsonify({
        "status": 405,
        "data": [{             
             "error": "The method request used is not supported for that url"
        }]
        })


@app.errorhandler(404)
def handle_bad_request(error):
    return jsonify({
        "status": 404,
        "data": [{    
             "error": "The requested input url is incorrect"
        }]
    })
