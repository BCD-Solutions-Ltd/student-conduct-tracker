from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity

from App.controllers import *

review_views = Blueprint('review_views', __name__, template_folder='../templates')

@review_views.route('/api/review', methods=['POST'])
def create_review_action():
    data = request.json
    log_review( data['studentid'], data['review_t']):
    return jsonify({'message': f"review for: {data['studentid']} created"})


@review_views.route('/api/review/upvote', methods=['POST'])
def update_upvotes_action():
    data = request.json
    upvote_review(data['revid'])):
    return jsonify({'message': f"review with id: {data['revid']} upvoted "})


@review_views.route('/api/review/downvote', methods=['POST'])
def update_downvotes_action():
    data = request.json
    downvote_review(data['revid'])):
    return jsonify({'message': f"review with id: {data['revid']} downvoted "})
