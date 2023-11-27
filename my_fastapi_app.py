from fastapi import FastAPI, UploadFile, File
from PIL import Image
import cv2
import music21

app = FastAPI()

@app.post("/image-to-musicxml")
async def image_to_musicxml(file: UploadFile):
    # Check if the uploaded file is an image
    if not file.filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
        return {"error": "Please upload a valid image file."}

    # Process the image
    image = Image.open(file.file)
    # Convert the image to grayscale
    grayscale_image = image.convert('L')
    
    # Use OpenCV to further process the image as needed
    # You can apply image processing techniques to extract musical information

    # Generate a simple MusicXML with music21
    score = music21.stream.Score()
    part = music21.stream.Part()
    note = music21.note.Note("C4")  # Change this to create your desired music
    part.append(note)
    score.insert(0, part)
    
    # Convert the MusicXML score to a string
    musicxml = score.write('musicxml')

    return {"musicxml": musicxml}

