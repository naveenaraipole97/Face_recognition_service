from flask import Flask, request, jsonify
import csv
import os

app=Flask(__name__)

csv_file_path='Classification_Results.csv'

def getNameFromFile(csv_file,target_file_name):
    with open(csv_file,'r') as file:
        reader=csv.DictReader(file)
        for row in reader:
            if row['Image']==target_file_name:
                print(row['Results'])
                return row['Results']

@app.route('/',methods=['POST'])
def post_data():
    if 'inputFile' not in request.files:
        return 'No File Uploaded, please upload!'

    file=request.files['inputFile']
    fileName, extension=os.path.splitext(file.filename)
    # check if the extension is valid?
    result=getNameFromFile(csv_file_path,fileName)
    response_data={'name': result,'status':'Success'}

    return jsonify(response_data)


if __name__=='__main__':
   app.run(host='0.0.0.0', port=80)