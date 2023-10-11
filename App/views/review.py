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


@review_views.route('/reviews/<stu_id>/<rev_id>/upvote', methods=['POST'])
def upvote_review(rev_id):
    review = find_review_by_id(rev_id)

    if review is None:
        return jsonify({"error": "Review not found"}), 404

    review['votes'] += 1

    return jsonify({"message": "Review upvoted"}), 200

@review_viewws.route('/reviews/<stu_id>/<rev_id>/downvote', methods=['POST'])
def downvote_review(rev_id):
    review = find_review_by_id(rev_id)

    if review is None:
        return jsonify({"error": "Review not found"}), 404

    review['votes'] -= 1

    return jsonify({"message": "Review downvoted"}), 200