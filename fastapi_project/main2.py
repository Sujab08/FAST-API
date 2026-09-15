from fastapi import FastAPI
app=FastAPI()
# list={"india":"hindi",
# "pak":"urdu","america":"eng","odisha":"odia"}
# list2=list.keys()
@app.get("/")
def home():
    return {"hello world"} 
list=["cloth","food","electronics","furniture","stationary","sports","toys"]
@app.get("/{lang}")
def home(lang):
    if lang not in list:
        return {"not available"}
    #return {f"{list.get(lang)} is the main language"}
    return {"avaliable"}
# from fastapi import FastAPI
# @app.get("/seema")
# def sujab():
#     return {" i love you seema very much"}