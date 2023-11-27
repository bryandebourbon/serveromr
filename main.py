from fastapi import FastAPI, UploadFile, File
import subprocess
import os
import shutil

app = FastAPI()

@app.post("/image-to-musicxml")
async def image_to_musicxml(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
        return {"error": "Please upload a valid image file."}

    # Save the uploaded file temporarily
    with open("temp_image.png", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Replace 'your_oemer_command' with the actual command to run Oemer
    # and 'output_file.xml' with the expected output file name
    subprocess.run(["oemer", "temp_image.png"], check=True)

    # Read the output MusicXML file
    with open("temp_image.musicxml", "r") as file:
        musicxml_data = file.read()

    # Optionally, clean up the temporary files
    os.remove("temp_image.png")
    os.remove("output_file.xml")

    return {"musicxml": musicxml_data}
