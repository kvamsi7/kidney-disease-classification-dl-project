from flask import Flask, request, jsonify,render_template
import os
from flask_cors import CORS, cross_origin
from src.kidney_cnn_classifier.pipeline.prediction import PredictionPipeline
from src.kidney_cnn_classifier.utils.common import decodeImage,encodeImageIntoBase64

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

# os.environ['MLFLOW_TRACKING_URI'] = "https://dagshub.com/kvamsi7/kidney-disease-classification-dl-project.mlflow"
# os.environ['MLFLOW_TRACKING_USERNAME'] = "kvamsi7"
# os.environ['MLFLOW_TRACKING_PASSWORD'] = "d6b1c8cf96f5b7cc6f735f6e0c8d127e5ad9c82d"

# Create an instance of the ClientApp class for prediction
# test 1 

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route('/train', methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return "Training completed successfully"


@app.route('/predict', methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predict()
    return jsonify(result)

if __name__ == '__main__':
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080) 