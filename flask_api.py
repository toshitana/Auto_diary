from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import auth

# Firebase初期化
cred = firebase_admin.credentials.Certificate('path/to/your/serviceAccountKey.json')
firebase_admin.initialize_app(cred)

app = Flask(__name__)
CORS(app)

def verify_firebase_token(id_token):
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token
    except Exception as e:
        return None

@app.route('/api/generate_questions', methods=['POST'])
def generate_questions():
    id_token = request.headers['Authorization']
    decoded_token = verify_firebase_token(id_token)
    if not decoded_token:
        return jsonify({'error': 'Invalid token'}), 403

    user_id = decoded_token['uid']

    # 実際の質問生成ロジックに置き換えてください
    return jsonify(['Question 1', 'Question 2', 'Question 3'])

@app.route('/api/generate_diary', methods=['POST'])
def generate_diary():
    id_token = request.headers['Authorization']
    decoded_token = verify_firebase_token(id_token)
    if not decoded_token:
        return jsonify({'error': 'Invalid token'}), 403

    user_id = decoded_token['uid']
    questions_answers = request.json

    # 実際の日記生成ロジックに置き換えてください
    diary_text = 'Generated diary text based on questions and answers.'

    return jsonify({'diary': diary_text})

@app.route('/api/register_diary', methods=['POST'])
def register_diary():
    id_token = request.headers['Authorization']
    decoded_token = verify_firebase_token(id_token)
    if not decoded_token:
        return jsonify({'error': 'Invalid token'}), 403

    user_id = decoded_token['uid']
    diary_text = request.json['diary']

    # 実際の日記登録ロジックに置き換えてください
    # DBに登録後、成功したかどうかのレスポンスを返します。
    return jsonify({'status': 'success'})
