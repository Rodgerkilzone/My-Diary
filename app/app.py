from flask import Flask, jsonify, abort, make_response, request, url_for
import config
app = Flask(__name__)
entries = [
    {"id": 1,
     "title": 'football',
     "content": 'the match was greet although we did not win',
     "date": '5-8-2018'
     },
    {"id": 2,
     "title": 'church',
     "content": 'the service today was amaizing',
     "date": '5-8-2018'
     },
    {"id": 3,
     "title": 'movies',
     "content": 'i watched alot of movies today',
     "date": '5-8-2018'
     }
]

def make_uri(entry):
    new_entry = {}
    for field in entry:
        if field == 'id':
            new_entry['uri'] = url_for('get_entry', entry_id=entry['id'], _external=True)
        else:
            new_entry[field] = entry[field]
    return new_entry

# GET ALL ENTRIES
@app.route('/mydiary/api/v1/entries', methods=['GET'])
def get_entries():
    return jsonify({'entries': [make_uri(entry) for entry in entries]})

#GET SPECIFIC ENTRIES
@app.route('/mydiary/api/v1/entries/<int:entry_id>', methods=['GET'])
def get_entry(entry_id):
    entry = [entry for entry in entries if entry['id'] == entry_id]
    if len(entry) == 0:
        return jsonify({"error":"No entry found"}),400
    return jsonify({'entry': entry[0]})
#POST ENTRIES    
@app.route('/mydiary/api/v1/entries', methods=['POST'])
def create_entry():
    if not request.json or 'title' not in request.json:
        return jsonify({"error":"please enter title"}),400
    if not request.json or 'date' not in request.json:
        return jsonify({"error":"please enter date"}),400
    if not request.json or 'content' not in request.json:
        return jsonify({"error":"please enter content"}),400
    entry = {
        "id": entries[-1]['id'] + 1,
        "title": request.json['title'],
        "content": request.json.get('content', ''),
        "date":request.json.get('date', '')
    }
    entries.append(entry)
    return jsonify({'entry': entry}), 201
#UPDATE ENTRIES
@app.route('/mydiary/api/v1/entries/<int:entry_id>', methods=['PUT'])
def update_entry(entry_id):
    entry = [entry for entry in entries if entry['id'] == entry_id]
    if len(entry) == 0 or not request.json:
        return jsonify({"error":"No entry found"}),400
    entry[0]['title'] = request.json.get('title', entry[0]['title'])
    entry[0]['content'] = request.json.get('content', entry[0]['content'])
    entry[0]['date'] = request.json.get('date', entry[0]['date'])
    return jsonify({'entry': entry})

#DELETE ENTRIES
@app.route('/mydiary/api/v1/entries/<int:entry_id>', methods=['DELETE'])
def delete_entry(entry_id):
    entry = [entry for entry in entries if entry['id'] == entry_id]
    if len(entry) == 0:
         return jsonify({"error":"No entry found"}),400
    entries.remove(entry[0])
    return jsonify({'entry': "Entry has been Deleted"})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
