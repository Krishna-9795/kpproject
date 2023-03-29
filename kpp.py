from flask import Flask, jsonify , request
app=Flask(__name__)
tasks=[
    {
        'id':1,
        'title':'Learn Python',
        'description':'Learn Python programming language',
        'done':False
    },
    {
        'id':2,
        'title':'Build a rest API',
        'description':'Build a restful api using python flask',
        'done':False
    }
]
app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks':tasks})
app.route('/tasks/<int:task_id>',methods=['GET'])
def get_task(task_id):
    task=[task for task in tasks if task['id']==task_id]
    if len(task)==0:
        abort (404)   
    return jsonify({'task':task[0]})
app.route('/tasks',methods=['POST'])
def create_task():
    if not request.json or not 'title' in request .json:
        abort (400)
    task={
        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',''),
        'done':False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201
app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)