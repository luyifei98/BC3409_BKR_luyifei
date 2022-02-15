#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import render_template,request
from keras.models import load_model
@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="POST":
        NPTA=float(request.form.get("NPTA"))
        TLTA=float(request.form.get("TLTA"))
        WCTA=float(request.form.get("WCTA"))
        print(NPTA,TLTA,WCTA)
        model = load_model("BKRNN")
        pred=model.predict([[NPTA,TLTA,WCTA]])
        print(pred)
        s ="The predicted bankruptcy score is " +str(pred)
        return(render_template("index.html",result=s))
    else:
        return(render_template("index.html",result="2"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:




