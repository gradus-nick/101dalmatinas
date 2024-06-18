import uvicorn
from fastapi import FastAPI, UploadFile, File
import img2barcode
import json
import configparser
import logging
from datetime import datetime

app = FastAPI()

@app.post("/file/uploadscan")
async def upload_file(file: UploadFile = File()):
    
    log_msg_start = {'datetime':datetime.now().strftime('%d.%m.%Y-%H:%M:%S'), 'filename':file.filename}
    logging.info(json.dumps(log_msg_start, ensure_ascii=False,))

    mBarcode = img2barcode.findbarcodepng(file)
    string_res = json.dumps(mBarcode, ensure_ascii=False,) 
    
    log_msg_finish = {'datetime':datetime.now().strftime('%d.%m.%Y-%H:%M:%S'), 'res':string_res}
    logging.info(log_msg_finish)

    return eval(string_res)

if __name__ == "__main__":
    config = configparser.ConfigParser()
    logging.basicConfig(level=logging.INFO, filename="101.log")

uvicorn.run(app, host='0.0.0.0', port=9090)
