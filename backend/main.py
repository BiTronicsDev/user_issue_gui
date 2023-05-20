import pandas as pd
import uvicorn as uvicorn
from fastapi import FastAPI, UploadFile, File
import shutil
from NeuralData.classifier import ShishkaClassifier
from fastapi.responses import FileResponse, JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/dataset")
async def upload_file(file: UploadFile = File(...)):
    """
    Фунциия upload_file принимает файл, с помощью предобученной моделиShishkaClassifier
    предсказывает возможное появление переквалификации статуса обращения и возвращает
    измененный файл с этими предсказанными данными.

    :param file: UploadFile: Receive the file from the client
    :return: A fileresponse object
    :doc-author: zayycev22
    """
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
