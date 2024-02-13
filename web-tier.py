from flask import Flask, request, jsonify
import csv
import os
import asyncio
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor()

app=Flask(__name__)

csv_file_path='Classification_Results.csv'

Results_dict={}

def getNameFromFile(csv_file,target_file_name):
    if not bool(Results_dict):
        with open(csv_file,'r') as file:
            reader=csv.DictReader(file)
            for row in reader:
                Results_dict[row['Image']]=row['Results']
    if(Results_dict[target_file_name]):
        return Results_dict[target_file_name]
    return "Not Found"

async def async_getNameFromFile(csv_file_path,fileName):
    loop=asyncio.get_event_loop()
    result=await loop.run_in_executor(executor,getNameFromFile,csv_file_path,fileName)
    return result

@app.route('/',methods=['POST'])
async def post_data():
    if 'inputFile' not in request.files:
        return 'No File Uploaded, please upload!'

    file=request.files['inputFile']
    fileName, extension=os.path.splitext(file.filename)
    # check if the extension is valid?
    result=await async_getNameFromFile(csv_file_path,fileName)
    # result=getNameFromFile(csv_file_path,fileName)
    response_data=fileName+':'+result
    response_data=response_data.replace('"','')
    response_data=response_data.strip()
    return response_data


if __name__=='__main__':
   app.run(host='0.0.0.0', port=80)