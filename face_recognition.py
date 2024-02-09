from flask import Flask, request, jsonify
import csv

app=Flask(__name__)

csv_file_path='Classification_Results.csv'

def getNameFromFile(csv_file,target_file_name):
    with open(csv_file,'r') as file:
        reader=csv.DictReader(file)

        for row in reader:
            if row['Image']==target_file_name:
                return row['Results']

@app.route('/',methods=['POST'])
def post_data():
    request_data=request.get_json()
    # find the jpeg file name in the csv file
    target_file_name=request_data['file_name']
    print(target_file_name)
    result=getNameFromFile(csv_file_path,target_file_name)
    response_data={'name': result,'status':'Success'}

    return jsonify(response_data)


if __name__=='__main__':
   app.run(debug=True)