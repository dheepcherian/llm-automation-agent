from fastapi import FastAPI, HTTPException
import os

app = FastAPI()

# Route to handle task execution
@app.post("/run")
async def run_task(task: str):
    try:
        return {"message": f"Executing task: {task}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Route to read file contents
@app.get("/read")
async def read_file(path: str):
    if not path.startswith("/data/"):
        raise HTTPException(status_code=403, detail="Access to this path is forbidden.")
    
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="File not found.")
    
    with open(path, "r") as file:
        content = file.read()
    
    return {"content": content}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
 
