from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import os
import datetime
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get("/", response_class=HTMLResponse)
async def read_directory(request: Request):
    files = os.listdir("./compartido/")
    file_details = []
    for file in files:
        stats = os.stat(f"./compartido/{file}")
        size_mb = stats.st_size / 1048576  # convert size to MB
        modified_time = datetime.datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
        file_details.append({"name": file, "size": f"{size_mb:.2f} MB", "last_modified": modified_time})
    return templates.TemplateResponse("index.html", {"request": request, "file_details": file_details})

@app.get("/download/{file_name}")
async def download_file(file_name: str):
    file_path = os.path.join("./compartido/", file_name)
    if os.path.isfile(file_path):
        return FileResponse(file_path)
    return {"message": "File not found"}

@app.post("/upload/")
async def upload_files(files: list[UploadFile] = File(...)):
    for file in files:
        file_location = f"./compartido/{file.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(await file.read())
    return RedirectResponse(url='/', status_code=303)

@app.delete("/delete/{file_name}")
async def delete_file(file_name: str):
    file_path = os.path.join("./compartido/", file_name)
    if os.path.isfile(file_path):
        os.remove(file_path)
        return {"message": "File deleted successfully"}
    return {"message": "File not found"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
