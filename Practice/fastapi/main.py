from fastapi import FastAPI
# import kr rhe h fastapi ko
app = FastAPI()
# fastAPI ka ek object bnaaya h
@app.get("/home") #jaise hi user ayega toh api hit hogi, hmne ek route bnaya
def hello():
    return {"message": "Hello World"}

@app.get('/about')
def about():
    return {"message": "Bhai placement kyu nhi ho rhi"}

# the fast API is craxy when you will go to the route '/docs' then you will se that FastAPi has build the docuemntion for you already of both the tw routes that you ahve proceesed and 
# not only you can also interact with them