from flask import Flask, render_template, request, send_file, jsonify, send_from_directory
import psutil
import os
app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    # file = request.files['file']
    # file.save(f'/path/to/save/{file.filename}')
    # return "File uploaded successfully"
    return render_template("upload.html")

@app.route('/download-files', methods=['GET'])
def download_file():
    directory = request.args.get('directory')
    file = request.args.get('file')
    return send_from_directory(directory, file, as_attachment=True)

@app.route('/download', methods=['GET'])
def download():
    
    #return send_file(f'/path/to/files/{filename}', as_attachment=True)
    return render_template("download.html")

@app.route('/list-files', methods=['GET'])
def list_files():
    directory = request.args.get('directory')
    if not os.path.exists(directory):
        return jsonify([]), 404
    files = os.listdir(directory)
    return jsonify(files)
    
def get_system_info():
    info = {
        
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent,
        "uptime": get_uptime()
    }
    return info

def get_uptime():
    # Get system uptime
    return os.popen('uptime -p').read().strip()

@app.route('/')
def home():
    status_info = get_system_info()
    return render_template('homepage.html', status= status_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
