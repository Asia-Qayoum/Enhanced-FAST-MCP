from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Dict, Any
import uvicorn
from datetime import datetime

# Create FastAPI app
app = FastAPI(
    title="Sample FastAPI App",
    description="A sample FastAPI application with MCP integration",
    version="1.0.0"
)

# Pydantic models
class User(BaseModel):
    name: str
    email: str
    age: int

class TodoItem(BaseModel):
    task: str
    completed: bool = False

class CalculationRequest(BaseModel):
    operation: str
    a: float
    b: float

# In-memory storage
users_db = []
todos_db = []

@app.get("/", response_class=HTMLResponse)
async def root():
    """Welcome page"""
    return """
    <html>
        <head>
            <title>Sample FastAPI App</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; }
                .container { max-width: 800px; margin: 0 auto; }
                h1 { color: #333; }
                .endpoint { background: #f5f5f5; padding: 10px; margin: 10px 0; border-radius: 5px; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚀 Sample FastAPI App</h1>
                <p>Welcome to our sample FastAPI application with MCP integration!</p>
                
                <h2>Available Endpoints:</h2>
                <div class="endpoint">
                    <strong>GET /users</strong> - List all users
                </div>
                <div class="endpoint">
                    <strong>POST /users</strong> - Create a new user
                </div>
                <div class="endpoint">
                    <strong>GET /todos</strong> - List all todos
                </div>
                <div class="endpoint">
                    <strong>POST /todos</strong> - Create a new todo
                </div>
                <div class="endpoint">
                    <strong>POST /calculate</strong> - Perform calculations
                </div>
                <div class="endpoint">
                    <strong>GET /health</strong> - Health check
                </div>
                
                <h2>📊 API Documentation:</h2>
                <p><a href="/docs">Swagger UI</a> | <a href="/redoc">ReDoc</a></p>
            </div>
        </body>
    </html>
    """

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    }

@app.get("/users")
async def get_users():
    """Get all users"""
    return {"users": users_db, "count": len(users_db)}

@app.post("/users")
async def create_user(user: User):
    """Create a new user"""
    users_db.append(user.dict())
    return {"message": "User created successfully", "user": user}

@app.get("/todos")
async def get_todos():
    """Get all todos"""
    return {"todos": todos_db, "count": len(todos_db)}

@app.post("/todos")
async def create_todo(todo: TodoItem):
    """Create a new todo"""
    todos_db.append(todo.dict())
    return {"message": "Todo created successfully", "todo": todo}

@app.post("/calculate")
async def calculate(request: CalculationRequest):
    """Perform mathematical calculations"""
    try:
        if request.operation == "add":
            result = request.a + request.b
        elif request.operation == "subtract":
            result = request.a - request.b
        elif request.operation == "multiply":
            result = request.a * request.b
        elif request.operation == "divide":
            if request.b == 0:
                raise HTTPException(status_code=400, detail="Division by zero")
            result = request.a / request.b
        else:
            raise HTTPException(status_code=400, detail="Invalid operation")
        
        return {
            "operation": request.operation,
            "a": request.a,
            "b": request.b,
            "result": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/stats")
async def get_stats():
    """Get application statistics"""
    return {
        "total_users": len(users_db),
        "total_todos": len(todos_db),
        "completed_todos": len([t for t in todos_db if t.get("completed", False)]),
        "uptime": "Running"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
