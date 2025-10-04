from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from pydantic import BaseModel
from typing import List, Dict, Any
import uvicorn
from datetime import datetime
from fastmcp import FastMCP
import os

# Create FastAPI app
app = FastAPI(
    title="Enhanced FastAPI App with MCP",
    description="A professional FastAPI application with integrated MCP server and beautiful frontend",
    version="2.0.0"
)

# Setup templates
templates = Jinja2Templates(directory="templates")

# Create MCP server
mcp = FastMCP(name="FastAPI MCP Server")

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

# MCP Tools
@mcp.tool
def greet_user(name: str) -> str:
    """Greet a user by name."""
    return f"Hello, {name}! Welcome to our FastAPI MCP Server!"

@mcp.tool
def add_numbers(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

@mcp.tool
def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

@mcp.tool
def create_user_mcp(name: str, email: str, age: int) -> Dict[str, Any]:
    """Create a new user via MCP."""
    user = {"name": name, "email": email, "age": age}
    users_db.append(user)
    return {"message": "User created successfully", "user": user}

@mcp.tool
def get_all_users() -> Dict[str, Any]:
    """Get all users via MCP."""
    return {"users": users_db, "count": len(users_db)}

@mcp.tool
def create_todo_mcp(task: str) -> Dict[str, Any]:
    """Create a new todo via MCP."""
    todo = {"task": task, "completed": False}
    todos_db.append(todo)
    return {"message": "Todo created successfully", "todo": todo}

@mcp.tool
def get_all_todos() -> Dict[str, Any]:
    """Get all todos via MCP."""
    return {"todos": todos_db, "count": len(todos_db)}

@mcp.tool
def calculate_area(length: float, width: float) -> Dict[str, float]:
    """Calculate area and perimeter of a rectangle."""
    area = length * width
    perimeter = 2 * (length + width)
    return {
        "length": length,
        "width": width,
        "area": area,
        "perimeter": perimeter
    }

@mcp.tool
def get_system_info() -> Dict[str, Any]:
    """Get system information."""
    import platform
    return {
        "platform": platform.platform(),
        "python_version": platform.python_version(),
        "architecture": platform.architecture()[0],
        "processor": platform.processor(),
        "server_name": "FastAPI MCP Server"
    }

@mcp.tool
def get_app_stats() -> Dict[str, Any]:
    """Get application statistics."""
    return {
        "total_users": len(users_db),
        "total_todos": len(todos_db),
        "completed_todos": len([t for t in todos_db if t.get("completed", False)]),
        "server_status": "Running",
        "mcp_tools_count": 15
    }

@mcp.tool
def generate_password(length: int = 12) -> str:
    """Generate a secure random password."""
    import secrets
    import string
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

@mcp.tool
def convert_temperature(value: float, from_unit: str, to_unit: str) -> Dict[str, Any]:
    """Convert temperature between Celsius, Fahrenheit, and Kelvin."""
    if from_unit.lower() == "celsius" and to_unit.lower() == "fahrenheit":
        result = (value * 9/5) + 32
    elif from_unit.lower() == "fahrenheit" and to_unit.lower() == "celsius":
        result = (value - 32) * 5/9
    elif from_unit.lower() == "celsius" and to_unit.lower() == "kelvin":
        result = value + 273.15
    elif from_unit.lower() == "kelvin" and to_unit.lower() == "celsius":
        result = value - 273.15
    elif from_unit.lower() == "fahrenheit" and to_unit.lower() == "kelvin":
        result = (value - 32) * 5/9 + 273.15
    elif from_unit.lower() == "kelvin" and to_unit.lower() == "fahrenheit":
        result = (value - 273.15) * 9/5 + 32
    else:
        result = value
    
    return {
        "original_value": value,
        "original_unit": from_unit,
        "converted_value": round(result, 2),
        "converted_unit": to_unit
    }

@mcp.tool
def text_analyzer(text: str) -> Dict[str, Any]:
    """Analyze text and provide statistics."""
    words = text.split()
    sentences = text.split('.')
    characters = len(text)
    characters_no_spaces = len(text.replace(' ', ''))
    
    return {
        "character_count": characters,
        "character_count_no_spaces": characters_no_spaces,
        "word_count": len(words),
        "sentence_count": len([s for s in sentences if s.strip()]),
        "average_word_length": round(sum(len(word) for word in words) / len(words), 2) if words else 0,
        "most_common_word": max(set(words), key=words.count) if words else None
    }

@mcp.tool
def url_shortener(url: str) -> Dict[str, str]:
    """Create a shortened URL (simulated)."""
    import hashlib
    short_code = hashlib.md5(url.encode()).hexdigest()[:8]
    short_url = f"https://short.ly/{short_code}"
    
    return {
        "original_url": url,
        "short_url": short_url,
        "short_code": short_code
    }

@mcp.tool
def qr_code_generator(text: str) -> Dict[str, str]:
    """Generate QR code data URL (simulated)."""
    import base64
    # Simulate QR code generation
    qr_data = base64.b64encode(text.encode()).decode()
    qr_url = f"data:image/png;base64,{qr_data}"
    
    return {
        "text": text,
        "qr_code_url": qr_url,
        "message": "QR code generated successfully"
    }

@mcp.tool
def weather_info(city: str) -> Dict[str, Any]:
    """Get weather information for a city (simulated)."""
    import random
    temperatures = [random.randint(-10, 35) for _ in range(3)]
    conditions = ["Sunny", "Cloudy", "Rainy", "Snowy", "Foggy"]
    
    return {
        "city": city,
        "current_temperature": temperatures[0],
        "min_temperature": min(temperatures),
        "max_temperature": max(temperatures),
        "condition": random.choice(conditions),
        "humidity": random.randint(30, 90),
        "wind_speed": random.randint(5, 25)
    }

@mcp.tool
def file_info(filename: str) -> Dict[str, Any]:
    """Get file information (simulated)."""
    import os
    import datetime
    
    # Simulate file info
    file_size = len(filename) * 1024  # Simulated size
    created_time = datetime.datetime.now().isoformat()
    
    return {
        "filename": filename,
        "file_size_bytes": file_size,
        "file_size_mb": round(file_size / (1024 * 1024), 2),
        "created_time": created_time,
        "file_type": filename.split('.')[-1] if '.' in filename else "unknown",
        "exists": True
    }

@mcp.tool
def color_palette_generator(color_count: int = 5) -> Dict[str, Any]:
    """Generate a random color palette."""
    import random
    
    colors = []
    for _ in range(color_count):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        hex_color = f"#{r:02x}{g:02x}{b:02x}"
        colors.append({
            "hex": hex_color,
            "rgb": f"rgb({r}, {g}, {b})",
            "name": f"Color {len(colors) + 1}"
        })
    
    return {
        "palette_name": "Random Palette",
        "color_count": color_count,
        "colors": colors
    }

# FastAPI Routes
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """Beautiful dashboard homepage"""
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0",
        "mcp_server": "integrated"
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
        "uptime": "Running",
        "mcp_tools": 9
    }

# MCP Server runner
def run_mcp_server():
    """Run the MCP server"""
    mcp.run()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "mcp":
        # Run MCP server
        run_mcp_server()
    else:
        # Run FastAPI server
        uvicorn.run(app, host="0.0.0.0", port=8000)
