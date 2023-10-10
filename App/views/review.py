from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity

from App.controllers import *

review_views = Blueprint('review_views', __name__, template_folder='../templates')


@review_views.route('/reviews', methods=['POST'])
def create_review_action():
    data = request.get_json()
    stu_id = data.get('studentID')
    content = data.get('content')
    votes = data.get('votes')

    if not(stu_id and content and votes):
        return jsonify({"error":"Bad Request"}), 400
    
    create_review(stu_id, content)

    return jsonify({"message": "Review added"}), 201


@review_views.route('/reviews/list', methods=['GET'])
def list_reviews_action():
    reviews = list_reviews()
    if not reviews:
        return jsonify({"error":"Table empty"}), 400
    return jsonify(reviews)

