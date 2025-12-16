from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
  return {"status": "Backend is running 🚀"}
  @app.get("/test")
  def test():
    return {"message": "Hello from Render backend"}
