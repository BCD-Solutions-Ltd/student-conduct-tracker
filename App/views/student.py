from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity


from App.controllers import *

student_views = Blueprint('student_views', __name__, template_folder='../templates')

@student_views.route('/student', methods=["POST"])
def create_student_action():
    data = request.json

    stu_id = data.get('stu_id')
    name = data.get('name')
    
    new_stu = create_student(stu_id, name)

    if not new_stu:
        return jsonify({"message":"Student not created"}), 400
    
    return jsonify({"message":"Student created"}), 201

@student_views.route('/student/list', methods=['GET'])
def list_student_action():
    return jsonify(get_all_students())
    


@student_views.route('/student/<id>', methods=['PUT'])
def update_student_action(id):
    data = request.json
    name = data.get('name')

    if update_student(id, name):
        return jsonify({"message":"Student updated"}), 200

    return jsonify({"message":"Student not updated"}), 400

@student_views.route('/student/search')
def search_students_action():
    name = request.args.get('name')
    result = search_student(name)

    if result:
        return jsonify(result)
    
    return jsonify({"message":"Student not found"}), 400