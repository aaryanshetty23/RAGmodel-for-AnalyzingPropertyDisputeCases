from flask import Flask, request, jsonify
from flask_cors import CORS
import chain

app = Flask(__name__)
CORS(app)  

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    question = data['question']
    namespace = data['namespace']  
    answer, sources = chain.query_rag(question, namespace)  
    sources_content = [doc.page_content for doc in sources]
    return jsonify({
        'answer': answer,
        'sources': sources_content
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
