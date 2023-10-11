from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity


from App.controllers import *

student_views = Blueprint('student_views', __name__, template_folder='../templates')

# @student_views.route('/students', methods=["POST"])
# def create_student_action():
#     data = request.get_json()

@student_views.route('/student/list', methods=['GET'])
def list_student_action():
    return jsonify(get_all_students())
    

@student_views.route('/api/student', methods=['GET'])
def getall_student_action():
    students = get_all_students()
    return jsonify(students)

@student_views.route('/api/stuent', methods=['POST'])
def create_student_action():
    data = request.json
    add_student(data['studentid'], data['name'])
    return jsonify({'message': f"student {data['studentid']} created"})

@student_views.route('/api/studnt', methods=['PUT'])
def update_student_action():
    data = request.json
    update_student(data['studentid'], data['name'])
    return jsonify({'message': f"student name was updated to {data['name']} "})

@student_views.route('/api/students', methods=['GET'])
def geta_student_action():
    data = request.json
    student = get_student_toJSON(data['studentid'])
    return jsonify({'message': f"Student found:Student Id {data['studentid']} with name: {student['name']}"} )
