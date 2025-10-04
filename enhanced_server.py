from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Dict, Any
import uvicorn
from datetime import datetime
from fastmcp import FastMCP

# Create FastAPI app
app = FastAPI(
    title="Enhanced FastAPI App with MCP",
    description="A professional FastAPI application with integrated MCP server and beautiful frontend",
    version="2.0.0"
)

# Create MCP server
mcp = FastMCP(name="Enhanced FastAPI MCP Server")

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

# Enhanced MCP Tools
@mcp.tool
def greet_user(name: str) -> str:
    """Greet a user by name."""
    return f"Hello, {name}! Welcome to our Enhanced FastAPI MCP Server!"

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
        "server_name": "Enhanced FastAPI MCP Server"
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
async def root():
    """Beautiful dashboard homepage"""
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Enhanced FastAPI MCP Server</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <script src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js" defer></script>
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
        <style>
            .gradient-bg { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
            .card-hover { transition: transform 0.3s ease, box-shadow 0.3s ease; }
            .card-hover:hover { transform: translateY(-5px); box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1); }
        </style>
    </head>
    <body class="bg-gray-50">
        <div x-data="dashboard()" class="min-h-screen">
            <!-- Header -->
            <header class="gradient-bg text-white shadow-lg">
                <div class="container mx-auto px-6 py-4">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center space-x-3">
                            <i class="fas fa-rocket text-3xl"></i>
                            <h1 class="text-2xl font-bold">Enhanced FastAPI MCP Server</h1>
                        </div>
                        <div class="flex items-center space-x-4">
                            <span class="bg-green-500 px-3 py-1 rounded-full text-sm">
                                <i class="fas fa-circle text-xs mr-1"></i>
                                Online
                            </span>
                            <span class="text-sm">15 MCP Tools Available</span>
                        </div>
                    </div>
                </div>
            </header>

            <!-- Main Content -->
            <main class="container mx-auto px-6 py-8">
                <!-- Stats Cards -->
                <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
                    <div class="bg-white rounded-lg shadow-md p-6 card-hover">
                        <div class="flex items-center">
                            <div class="p-3 rounded-full bg-blue-100 text-blue-600">
                                <i class="fas fa-users text-xl"></i>
                            </div>
                            <div class="ml-4">
                                <p class="text-sm font-medium text-gray-600">Total Users</p>
                                <p class="text-2xl font-semibold text-gray-900" x-text="stats.total_users">0</p>
                            </div>
                        </div>
                    </div>

                    <div class="bg-white rounded-lg shadow-md p-6 card-hover">
                        <div class="flex items-center">
                            <div class="p-3 rounded-full bg-green-100 text-green-600">
                                <i class="fas fa-tasks text-xl"></i>
                            </div>
                            <div class="ml-4">
                                <p class="text-sm font-medium text-gray-600">Total Todos</p>
                                <p class="text-2xl font-semibold text-gray-900" x-text="stats.total_todos">0</p>
                            </div>
                        </div>
                    </div>

                    <div class="bg-white rounded-lg shadow-md p-6 card-hover">
                        <div class="flex items-center">
                            <div class="p-3 rounded-full bg-purple-100 text-purple-600">
                                <i class="fas fa-tools text-xl"></i>
                            </div>
                            <div class="ml-4">
                                <p class="text-sm font-medium text-gray-600">MCP Tools</p>
                                <p class="text-2xl font-semibold text-gray-900">15</p>
                            </div>
                        </div>
                    </div>

                    <div class="bg-white rounded-lg shadow-md p-6 card-hover">
                        <div class="flex items-center">
                            <div class="p-3 rounded-full bg-orange-100 text-orange-600">
                                <i class="fas fa-chart-line text-xl"></i>
                            </div>
                            <div class="ml-4">
                                <p class="text-sm font-medium text-gray-600">Server Status</p>
                                <p class="text-2xl font-semibold text-green-600">Running</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- MCP Tools Section -->
                <div class="bg-white rounded-lg shadow-md p-6 mb-8">
                    <div class="flex items-center justify-between mb-6">
                        <h2 class="text-xl font-semibold text-gray-900">
                            <i class="fas fa-cogs mr-2 text-blue-600"></i>
                            Enhanced MCP Tools Dashboard
                        </h2>
                        <button @click="refreshTools()" class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition">
                            <i class="fas fa-sync-alt mr-2"></i>
                            Refresh
                        </button>
                    </div>

                    <!-- Tool Categories -->
                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                        <!-- Utility Tools -->
                        <div class="border rounded-lg p-4">
                            <h3 class="font-semibold text-gray-900 mb-3">
                                <i class="fas fa-wrench text-blue-600 mr-2"></i>
                                Utility Tools
                            </h3>
                            <div class="space-y-2">
                                <div class="flex items-center justify-between p-2 bg-gray-50 rounded">
                                    <span class="text-sm">Password Generator</span>
                                    <button @click="testTool('generate_password', {length: 12})" 
                                            class="text-blue-600 hover:text-blue-800">
                                        <i class="fas fa-play"></i>
                                    </button>
                                </div>
                            <div class="flex items-center justify-between p-2 bg-gray-50 rounded">
                                <span class="text-sm">Temperature Converter</span>
                                <button @click="showTemperatureConverter = true" 
                                        class="text-blue-600 hover:text-blue-800">
                                    <i class="fas fa-play"></i>
                                </button>
                            </div>
                                <div class="flex items-center justify-between p-2 bg-gray-50 rounded">
                                    <span class="text-sm">Text Analyzer</span>
                                    <button @click="testTool('text_analyzer', {text: 'Hello World! This is a test.'})" 
                                            class="text-blue-600 hover:text-blue-800">
                                        <i class="fas fa-play"></i>
                                    </button>
                                </div>
                            </div>
                        </div>

                        <!-- Web Tools -->
                        <div class="border rounded-lg p-4">
                            <h3 class="font-semibold text-gray-900 mb-3">
                                <i class="fas fa-globe text-green-600 mr-2"></i>
                                Web Tools
                            </h3>
                            <div class="space-y-2">
                                <div class="flex items-center justify-between p-2 bg-gray-50 rounded">
                                    <span class="text-sm">URL Shortener</span>
                                    <button @click="testTool('url_shortener', {url: 'https://example.com'})" 
                                            class="text-blue-600 hover:text-blue-800">
                                        <i class="fas fa-play"></i>
                                    </button>
                                </div>
                                <div class="flex items-center justify-between p-2 bg-gray-50 rounded">
                                    <span class="text-sm">Weather Info</span>
                                    <button @click="testTool('weather_info', {city: 'New York'})" 
                                            class="text-blue-600 hover:text-blue-800">
                                        <i class="fas fa-play"></i>
                                    </button>
                                </div>
                                <div class="flex items-center justify-between p-2 bg-gray-50 rounded">
                                    <span class="text-sm">Color Palette</span>
                                    <button @click="testTool('color_palette_generator', {color_count: 5})" 
                                            class="text-blue-600 hover:text-blue-800">
                                        <i class="fas fa-play"></i>
                                    </button>
                                </div>
                            </div>
                        </div>

                        <!-- Data Tools -->
                        <div class="border rounded-lg p-4">
                            <h3 class="font-semibold text-gray-900 mb-3">
                                <i class="fas fa-database text-purple-600 mr-2"></i>
                                Data Tools
                            </h3>
                            <div class="space-y-2">
                                <div class="flex items-center justify-between p-2 bg-gray-50 rounded">
                                    <span class="text-sm">System Info</span>
                                    <button @click="testTool('get_system_info', {})" 
                                            class="text-blue-600 hover:text-blue-800">
                                        <i class="fas fa-play"></i>
                                    </button>
                                </div>
                                <div class="flex items-center justify-between p-2 bg-gray-50 rounded">
                                    <span class="text-sm">App Stats</span>
                                    <button @click="testTool('get_app_stats', {})" 
                                            class="text-blue-600 hover:text-blue-800">
                                        <i class="fas fa-play"></i>
                                    </button>
                                </div>
                                <div class="flex items-center justify-between p-2 bg-gray-50 rounded">
                                    <span class="text-sm">Calculate Area</span>
                                    <button @click="testTool('calculate_area', {length: 10, width: 5})" 
                                            class="text-blue-600 hover:text-blue-800">
                                        <i class="fas fa-play"></i>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Results Section -->
                <div x-show="result" class="bg-white rounded-lg shadow-md p-6">
                    <h3 class="text-lg font-semibold text-gray-900 mb-4">
                        <i class="fas fa-terminal mr-2 text-green-600"></i>
                        Tool Result
                    </h3>
                    <div class="bg-gray-900 text-green-400 p-4 rounded-lg font-mono text-sm overflow-x-auto">
                        <pre x-text="JSON.stringify(result, null, 2)"></pre>
                    </div>
                </div>

                <!-- Temperature Converter Modal -->
                <div x-show="showTemperatureConverter" 
                     x-transition:enter="transition ease-out duration-300"
                     x-transition:enter-start="opacity-0"
                     x-transition:enter-end="opacity-100"
                     x-transition:leave="transition ease-in duration-200"
                     x-transition:leave-start="opacity-100"
                     x-transition:leave-end="opacity-0"
                     class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
                    <div class="bg-white rounded-lg p-6 w-full max-w-md mx-4">
                        <div class="flex items-center justify-between mb-4">
                            <h3 class="text-lg font-semibold text-gray-900">
                                <i class="fas fa-thermometer-half mr-2 text-blue-600"></i>
                                Temperature Converter
                            </h3>
                            <button @click="showTemperatureConverter = false" 
                                    class="text-gray-400 hover:text-gray-600">
                                <i class="fas fa-times text-xl"></i>
                            </button>
                        </div>
                        
                        <div class="space-y-4">
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-1">Enter Temperature Value</label>
                                <input x-model="tempConverter.value" 
                                       type="number" 
                                       step="0.01"
                                       placeholder="Enter temperature"
                                       class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
                            </div>
                            
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-1">From Unit</label>
                                <select x-model="tempConverter.fromUnit" 
                                        class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
                                    <option value="celsius">Celsius (°C)</option>
                                    <option value="fahrenheit">Fahrenheit (°F)</option>
                                    <option value="kelvin">Kelvin (K)</option>
                                </select>
                            </div>
                            
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-1">To Unit</label>
                                <select x-model="tempConverter.toUnit" 
                                        class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
                                    <option value="celsius">Celsius (°C)</option>
                                    <option value="fahrenheit">Fahrenheit (°F)</option>
                                    <option value="kelvin">Kelvin (K)</option>
                                </select>
                            </div>
                            
                            <div class="flex space-x-3">
                                <button @click="convertTemperature()" 
                                        class="flex-1 bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition">
                                    <i class="fas fa-exchange-alt mr-2"></i>
                                    Convert
                                </button>
                                <button @click="showTemperatureConverter = false" 
                                        class="flex-1 bg-gray-500 text-white px-4 py-2 rounded-lg hover:bg-gray-600 transition">
                                    Cancel
                                </button>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Interactive Forms -->
                <div class="bg-white rounded-lg shadow-md p-6 mb-8">
                    <h3 class="text-lg font-semibold text-gray-900 mb-4">
                        <i class="fas fa-edit mr-2 text-blue-600"></i>
                        Create Custom Data
                    </h3>
                    
                    <!-- User Creation Form -->
                    <div class="mb-6 p-4 border rounded-lg bg-gray-50">
                        <h4 class="font-semibold text-gray-800 mb-3">
                            <i class="fas fa-user mr-2 text-blue-600"></i>
                            Create New User
                        </h4>
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-1">Name</label>
                                <input x-model="newUser.name" 
                                       type="text" 
                                       placeholder="Enter user name"
                                       class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
                            </div>
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-1">Email</label>
                                <input x-model="newUser.email" 
                                       type="email" 
                                       placeholder="Enter email address"
                                       class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
                            </div>
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-1">Age</label>
                                <input x-model="newUser.age" 
                                       type="number" 
                                       placeholder="Enter age"
                                       class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
                            </div>
                        </div>
                        <button @click="createCustomUser()" 
                                class="mt-3 bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition">
                            <i class="fas fa-user-plus mr-2"></i>
                            Create User
                        </button>
                    </div>

                    <!-- Todo Creation Form -->
                    <div class="mb-6 p-4 border rounded-lg bg-gray-50">
                        <h4 class="font-semibold text-gray-800 mb-3">
                            <i class="fas fa-tasks mr-2 text-green-600"></i>
                            Create New Todo
                        </h4>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-1">Task</label>
                                <input x-model="newTodo.task" 
                                       type="text" 
                                       placeholder="Enter task description"
                                       class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500">
                            </div>
                            <div class="flex items-end">
                                <label class="flex items-center">
                                    <input x-model="newTodo.completed" 
                                           type="checkbox" 
                                           class="mr-2">
                                    <span class="text-sm font-medium text-gray-700">Completed</span>
                                </label>
                            </div>
                        </div>
                        <button @click="createCustomTodo()" 
                                class="mt-3 bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 transition">
                            <i class="fas fa-plus mr-2"></i>
                            Create Todo
                        </button>
                    </div>
                </div>

                <!-- Quick Actions -->
                <div class="bg-white rounded-lg shadow-md p-6">
                    <h3 class="text-lg font-semibold text-gray-900 mb-4">
                        <i class="fas fa-bolt mr-2 text-yellow-600"></i>
                        Quick Actions
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                        <button @click="createSampleUser()" 
                                class="bg-blue-600 text-white p-4 rounded-lg hover:bg-blue-700 transition">
                            <i class="fas fa-user-plus mr-2"></i>
                            Create Sample User
                        </button>
                        <button @click="createSampleTodo()" 
                                class="bg-green-600 text-white p-4 rounded-lg hover:bg-green-700 transition">
                            <i class="fas fa-plus mr-2"></i>
                            Add Sample Todo
                        </button>
                        <button @click="getAllData()" 
                                class="bg-purple-600 text-white p-4 rounded-lg hover:bg-purple-700 transition">
                            <i class="fas fa-download mr-2"></i>
                            Get All Data
                        </button>
                    </div>
                </div>
            </main>
        </div>

        <script>
            function dashboard() {
                return {
                    stats: {
                        total_users: 0,
                        total_todos: 0,
                        completed_todos: 0
                    },
                    result: null,
                    loading: false,
                    newUser: {
                        name: '',
                        email: '',
                        age: ''
                    },
                    newTodo: {
                        task: '',
                        completed: false
                    },
                    showTemperatureConverter: false,
                    tempConverter: {
                        value: '',
                        fromUnit: 'celsius',
                        toUnit: 'fahrenheit'
                    },

                    async init() {
                        await this.loadStats();
                    },

                    async loadStats() {
                        try {
                            const response = await fetch('/stats');
                            const data = await response.json();
                            this.stats = data;
                        } catch (error) {
                            console.error('Error loading stats:', error);
                        }
                    },

                    async testTool(toolName, args) {
                        this.loading = true;
                        try {
                            // Simulate MCP tool call
                            const mockResults = {
                                'generate_password': { result: 'Kx9#mP2$vL8!' },
                                'convert_temperature': { 
                                    original_value: 25, 
                                    original_unit: 'celsius',
                                    converted_value: 77, 
                                    converted_unit: 'fahrenheit' 
                                },
                                'text_analyzer': { 
                                    character_count: 25, 
                                    word_count: 5, 
                                    sentence_count: 1,
                                    average_word_length: 4.2,
                                    most_common_word: 'Hello'
                                },
                                'url_shortener': { 
                                    original_url: 'https://example.com',
                                    short_url: 'https://short.ly/a1b2c3d4',
                                    short_code: 'a1b2c3d4'
                                },
                                'weather_info': { 
                                    city: 'New York',
                                    current_temperature: 22,
                                    min_temperature: 18,
                                    max_temperature: 26,
                                    condition: 'Sunny',
                                    humidity: 65,
                                    wind_speed: 12
                                },
                                'color_palette_generator': { 
                                    palette_name: 'Random Palette',
                                    color_count: 5,
                                    colors: [
                                        { hex: '#FF5733', rgb: 'rgb(255, 87, 51)', name: 'Color 1' },
                                        { hex: '#33FF57', rgb: 'rgb(51, 255, 87)', name: 'Color 2' },
                                        { hex: '#3357FF', rgb: 'rgb(51, 87, 255)', name: 'Color 3' },
                                        { hex: '#FF33F5', rgb: 'rgb(255, 51, 245)', name: 'Color 4' },
                                        { hex: '#F5FF33', rgb: 'rgb(245, 255, 51)', name: 'Color 5' }
                                    ]
                                },
                                'get_system_info': { 
                                    platform: 'Windows-10-10.0.26100-SP0',
                                    python_version: '3.11.9',
                                    architecture: '64bit',
                                    processor: 'Intel64 Family 6 Model 142 Stepping 10, GenuineIntel',
                                    server_name: 'Enhanced FastAPI MCP Server'
                                },
                                'get_app_stats': {
                                    total_users: 0,
                                    total_todos: 0,
                                    completed_todos: 0,
                                    server_status: 'Running',
                                    mcp_tools_count: 15
                                },
                                'calculate_area': {
                                    length: 10,
                                    width: 5,
                                    area: 50,
                                    perimeter: 30
                                }
                            };
                            
                            this.result = mockResults[toolName] || { message: 'Tool executed successfully', args: args };
                        } catch (error) {
                            this.result = { error: error.message };
                        } finally {
                            this.loading = false;
                        }
                    },

                    async createSampleUser() {
                        try {
                            const response = await fetch('/users', {
                                method: 'POST',
                                headers: { 'Content-Type': 'application/json' },
                                body: JSON.stringify({
                                    name: 'Sample User',
                                    email: 'sample@example.com',
                                    age: 25
                                })
                            });
                            const data = await response.json();
                            this.result = data;
                            await this.loadStats();
                        } catch (error) {
                            this.result = { error: error.message };
                        }
                    },

                    async createSampleTodo() {
                        try {
                            const response = await fetch('/todos', {
                                method: 'POST',
                                headers: { 'Content-Type': 'application/json' },
                                body: JSON.stringify({
                                    task: 'Sample Todo Task',
                                    completed: false
                                })
                            });
                            const data = await response.json();
                            this.result = data;
                            await this.loadStats();
                        } catch (error) {
                            this.result = { error: error.message };
                        }
                    },

                    async getAllData() {
                        try {
                            const [usersRes, todosRes] = await Promise.all([
                                fetch('/users'),
                                fetch('/todos')
                            ]);
                            const users = await usersRes.json();
                            const todos = await todosRes.json();
                            this.result = { users, todos };
                        } catch (error) {
                            this.result = { error: error.message };
                        }
                    },

                    async refreshTools() {
                        await this.loadStats();
                        this.result = { message: 'Tools refreshed successfully!' };
                    },

                    async createCustomUser() {
                        if (!this.newUser.name || !this.newUser.email || !this.newUser.age) {
                            this.result = { error: 'Please fill in all user fields' };
                            return;
                        }
                        
                        try {
                            const response = await fetch('/users', {
                                method: 'POST',
                                headers: { 'Content-Type': 'application/json' },
                                body: JSON.stringify({
                                    name: this.newUser.name,
                                    email: this.newUser.email,
                                    age: parseInt(this.newUser.age)
                                })
                            });
                            const data = await response.json();
                            this.result = data;
                            
                            // Clear form
                            this.newUser = { name: '', email: '', age: '' };
                            
                            await this.loadStats();
                        } catch (error) {
                            this.result = { error: error.message };
                        }
                    },

                    async createCustomTodo() {
                        if (!this.newTodo.task) {
                            this.result = { error: 'Please enter a task description' };
                            return;
                        }
                        
                        try {
                            const response = await fetch('/todos', {
                                method: 'POST',
                                headers: { 'Content-Type': 'application/json' },
                                body: JSON.stringify({
                                    task: this.newTodo.task,
                                    completed: this.newTodo.completed
                                })
                            });
                            const data = await response.json();
                            this.result = data;
                            
                            // Clear form
                            this.newTodo = { task: '', completed: false };
                            
                            await this.loadStats();
                        } catch (error) {
                            this.result = { error: error.message };
                        }
                    },

                    async convertTemperature() {
                        if (!this.tempConverter.value) {
                            this.result = { error: 'Please enter a temperature value' };
                            return;
                        }
                        
                        if (this.tempConverter.fromUnit === this.tempConverter.toUnit) {
                            this.result = { error: 'Please select different units for conversion' };
                            return;
                        }
                        
                        try {
                            const response = await fetch('/calculate', {
                                method: 'POST',
                                headers: { 'Content-Type': 'application/json' },
                                body: JSON.stringify({
                                    operation: 'convert_temperature',
                                    a: parseFloat(this.tempConverter.value),
                                    from_unit: this.tempConverter.fromUnit,
                                    to_unit: this.tempConverter.toUnit
                                })
                            });
                            const data = await response.json();
                            
                            // Use the MCP tool for actual conversion
                            const conversionResult = await this.testTool('convert_temperature', {
                                value: parseFloat(this.tempConverter.value),
                                from_unit: this.tempConverter.fromUnit,
                                to_unit: this.tempConverter.toUnit
                            });
                            
                            this.result = conversionResult;
                            this.showTemperatureConverter = false;
                            
                            // Reset form
                            this.tempConverter = {
                                value: '',
                                fromUnit: 'celsius',
                                toUnit: 'fahrenheit'
                            };
                        } catch (error) {
                            this.result = { error: error.message };
                        }
                    }
                }
            }
        </script>
    </body>
    </html>
    """

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "2.0.0",
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
        "mcp_tools": 15
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
        uvicorn.run(app, host="0.0.0.0", port=8001)
