from flask import Flask, render_template, request
#import nltk
import numpy as np
#import random
#import string # to process standard python strings
from werkzeug.utils import secure_filename           #for image input
import os
from tensorflow.keras.models import Sequential, model_from_json, load_model
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense






app = Flask(__name__)



   
  
'''from twilio.rest import Client as Call

def Calling(number):
  print("Inside Call Function")
  From_Number = "+12028901465"
  numb="+91"+str(number)
  no=int(numb)
  To_Number = no  #provide an emergency number in any variable to from_number e.g firebriged calling number
  Src_Path = "http://static.fullstackpython.com/phone-calls-python.xml"  #add here the

  client = Call("AC0ec3e7a01f011fc686aaf5dcd91c5881" , "2cebe4f3021a076998417b7625992b99")
  print('call initialted')
  client.calls.create(to = To_Number, from_=From_Number, url = Src_Path, method = 'GET')
  print('Call has been triggered successfully')'''
  
#new_model = load_model('natural_disaster.model') 
           

new_model = load_model('my_model.h5')
def imageprocess(imagename):
    

    # Check its architecture
    #new_model.summary()
    import numpy as np
    from keras.preprocessing import image
    test_image = image.load_img(imagename, target_size = (64, 64))   #file to be predicted imagename
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = new_model.predict(test_image)
    print(result)

    if result[0][0] == 0:
       prediction = 'Fire brigade number'
    else:
       prediction = 'Smoke'
	
    return prediction

#define app routes
@app.route("/")
def index():
    return render_template("index.html")
	



@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   global secure_filename
   if request.method == 'POST':
      f = request.files['file']
      secure_filename = secure_filename(f.filename)
      img_path=os.path.join(app.root_path,secure_filename)
      f.save(img_path)
      print("File name printed")
      print(f.filename)
      print(secure_filename)
      pred = imageprocess(secure_filename)
      return render_template("imageoutput.html",value=pred)




if __name__ == "__main__":
    app.run(debug=True)