import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/cgi-bin/status_static', methods=['GET'])
def status_static():
    file_path = '/var/www/iprouter/knxstatic.json'
    try:
        # 检查文件是否存在
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                import json
                data = json.load(file)
                return jsonify(data)
        else:
            return jsonify({"error": "文件未找到"}), 404
    except Exception as e:
        return jsonify({"error": f"读取文件时出错: {str(e)}"}), 500

@app.route('/cgi-bin/status_dynamic', methods=['GET'])
def status_dynamic():
    file_path = '/var/www/iprouter/knxdynamic.json'
    try:
        # 检查文件是否存在
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                import json
                data = json.load(file)
                return jsonify(data)
        else:
            return jsonify({"error": "文件未找到"}), 404
    except Exception as e:
        return jsonify({"error": f"读取文件时出错: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
