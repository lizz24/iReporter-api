@app.route('/api/v1/red-flags', methods=['GET'])
def get_redflags():
    # getting all red-flags
    Redflags = [incident.get_incident() for incident in redflags_list]
    if len(redflags_list) > 0:
     return jsonify({
         "data": Redflags,
         "status" : 200
        })
    else:
     return jsonify({
             "error": "no data entry for red-flags",
             "status": 404
             })
