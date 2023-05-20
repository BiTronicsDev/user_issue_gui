import pandas as pd
import uvicorn as uvicorn
from fastapi import FastAPI, UploadFile, File
import shutil
from NeuralData.classifier import ShishkaClassifier
from fastapi.responses import FileResponse, JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/dataset")
async def upload_file(file: UploadFile = File(...)):
    if file.filename.split('.')[1] == 'csv':
        with open(f"files/{file.filename}", "wb") as f:
            shutil.copyfileobj(file.file, f)
        try:
            frame = pd.read_csv(f"files/{file.filename}")
            classifier = ShishkaClassifier(frame)
            classifier.reformat_df()
            ans = classifier.predict()
            frame = classifier.set_requal(frame, ans)
            frame.to_csv("files/answer.csv", index=False)
            del frame
        except Exception as e:
            print(e)
            return JSONResponse({'status': 'something went wrong'}, status_code=HTTP_400_BAD_REQUEST)
        else:
            return FileResponse("files/answer.csv")
    else:
        return JSONResponse({'status': 'bad_file'}, status_code=HTTP_400_BAD_REQUEST)

if __name__ == '__main__':
    uvicorn.run(app)
