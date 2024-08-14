from PIL import Image
from landingai.predict import Predictor
from dotenv import load_dotenv
import os

load_dotenv()

endpoint_id = os.getenv("ENDPOINT_ID")
api_key = os.getenv("API_KEY")

#Enter path of all the images to be predicted in the img list, separated by commas(,)
#MAKE SURE TO REPLACE ALL '/' WITH '\' OR '\\'
# EXAMPLE - img = ["C:/Users/devan/Pictures/Screenshots/Screenshot 2024-08-14 113332.png","C:/Users/devan/Pictures/Screenshots/Screenshot 2024-08-14 113327.png"]
img=[]
l=len(img)

for i in range(0,l):
    image = Image.open(img[i])
    predictor = Predictor(endpoint_id, api_key=api_key)
    predictions = predictor.predict(image)
    print('Image- ',img[i])
    print(predictions)
    p=round(((i+1)/l)*100,2)
    print(f"{p}% completed")

print("All Predictions Completed") 
print("NOTE THAT THESE PREDICTIONS MAY NOT BE 100% ACCURATE")