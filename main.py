import uvicorn
from fastapi import FastAPI, UploadFile, File
import img2barcode
import json
import configparser

app = FastAPI()

@app.post("/file/uploadscan")
async def upload_file(file: UploadFile = File()):
    
    mBarcode = img2barcode.findbarcodepng(file)
    string_res = json.dumps(mBarcode, ensure_ascii=False,) 
    return eval(string_res)

if __name__ == "__main__":
    config = configparser.ConfigParser()
#    config.read('/home/artur/101dalmatinas/config.ini')
#    conf_host = config['UVICORN']['host']
#    conf_port = int(config['UVICORN']['port'])
#    uvicorn.run(app, host=conf_host, port=conf_port)
uvicorn.run(app, host='0.0.0.0', port=9090)
