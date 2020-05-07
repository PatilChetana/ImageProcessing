


from flask import Flask, render_template, request,jsonify


from tensorflow.keras.models import load_model

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense





app = Flask(__name__)


model = load_model('my_model.h5')


#training phases below


  

#testing phase below  (run this code everytime, donot run the whole code)


@app.route('/', methods=['GET', 'POST'])
def calls():
  import numpy as np
  from tensorflow.keras.preprocessing import image
  test_image = image.load_img('sample4.png', target_size = (64, 64))   #file to be predicted imagename
  test_image = image.img_to_array(test_image)
  test_image = np.expand_dims(test_image, axis = 0)
  result = model.predict(test_image)
  print(result)
  global prediction
  if result[0][0] == 0:
       prediction = 'Fire brigade number'
  else:
       prediction = 'Smoke'

  print(prediction)
  return prediction







#define app routes
#@app.route("/")
#def index():
#    return render_template("index.html")


    
   # return render_template("index.html")





if __name__ == "__main__":
    app.run(debug=True)