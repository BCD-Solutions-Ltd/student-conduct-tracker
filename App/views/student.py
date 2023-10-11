from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity


from App.controllers import *

student_views = Blueprint('student_views', __name__, template_folder='../templates')

@student_views.route('/student', methods=["POST"])
def create_student_action():
    data = request.get_json()
    stu_id = data.get('stu_id')
    name = data.get('name')
    
    return jsonify({"message":"Student created"}), 201

@student_views.route('/student/list', methods=['GET'])
def list_student_action():
    return jsonify(get_all_students())
    


@student_views.route('/student/<id>', methods=['PUT'])
def update_student_action(id):
    data = request.get_json
    name = data.get('name')

    update_student(id, name)

    return jsonify({"message":"Student updated"}), 200
