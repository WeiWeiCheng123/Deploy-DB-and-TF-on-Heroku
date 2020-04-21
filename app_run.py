import tensorflow as tf
from flask import *
import numpy
import pandas as pd
numpy.random.seed(10)
import fileinput
from flask_sqlalchemy import SQLAlchemy
from dbModel import *
import os
import xlrd

new_model = tf.keras.models.load_model('xxxx.h5')
放模型ㄉ 放在同一個資料夾底下
#app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html', **locals())

@app.route('/upload', methods=['GET', 'POST'])
def upload():
     if request.method == 'POST':
             file = request.files['inputfile']
             newfile= FileContents(name=file.filename, data=file.read())
             db.session.add(newfile)
             db.session.commit()
     return redirect(url_for('index'))


@app.route('/predict', methods=['GET', 'POST'])
def predict():
     if request.method == 'POST':
             file = request.files['inputfile']
             test_df = pd.read_excel(file)
             test_df=test_df.values
             test_df = numpy.array(test_df, dtype=numpy.float32)
             predictions = new_model.predict(test_df)
             if (predictions[0][0]>predictions[0][1])&(predictions[0][0]>predictions[0][2])&(predictions[0][0]>predictions[0][3]):
                 results='1'
             if (predictions[0][1]>predictions[0][0])&(predictions[0][1]>predictions[0][2])&(predictions[0][1]>predictions[0][3]):
                 results='2'
             if (predictions[0][2]>predictions[0][0])&(predictions[0][2]>predictions[0][1])&(predictions[0][2]>predictions[0][3]):
                 results='3'
             if (predictions[0][3]>predictions[0][0])&(predictions[0][3]>predictions[0][1])&(predictions[0][3]>predictions[0][2]):
                 results='4'
     return render_template('index.html',results=results)
        



if __name__ == '__main__':
    app.run(debug=True)
    
    
