from PIL import Image
from landingai.predict import Predictor
import matplotlib.pyplot as plt


endpoint_id = "c7cb31bf-7dee-4c38-bbdf-22633f49f2b0"
api_key = "land_sk_dRxZP2L2PuiyGdYSZpsKKOSc1NKpfGWsj5jOW47k1oPeKK4vf3"

#Enter path of all the images to be predicted in the img list, separated by commas(,)
img = []
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