# Enhanced FastAPI MCP Server

A comprehensive FastAPI application integrated with FastMCP (Model Context Protocol) featuring an interactive frontend dashboard and multiple utility tools.

## 📹 **Screen Recording Demo**

**Watch the complete demonstration:** [Screen Recording](https://drive.google.com/file/d/1O4CHunMQFL7IzcyBI0_TLjSNnX9Wc-3z/view?usp=sharing)

The video shows:
- ✅ MCP Server running (`python enhanced_server.py mcp`)
- ✅ Gemini CLI MCP list command (`mcp list`)
- ✅ Usage of MCP tools through CLI
- ✅ Interactive frontend with temperature converter
- ✅ All 15+ MCP tools in action

## 🎯 **Submission Details**

**Project**: MCP Server using FAST MCP  
**Deadline**: October 4th, 2025  
**Repository**: [https://github.com/Asia-Qayoum/Enhanced-FAST-MCP.git](https://github.com/Asia-Qayoum/Enhanced-FAST-MCP.git)  
**Demo Video**: [https://drive.google.com/file/d/1O4CHunMQFL7IzcyBI0_TLjSNnX9Wc-3z/view?usp=sharing](https://drive.google.com/file/d/1O4CHunMQFL7IzcyBI0_TLjSNnX9Wc-3z/view?usp=sharing)

## Features

- **Enhanced FastAPI Web Application** with interactive frontend dashboard
- **MCP Server Integration** with 15+ available tools
- **Interactive Temperature Converter** with modal popup
- **Gemini CLI Compatible** for AI assistant integration
- **Real-time Data Management** for users and todos
- **Beautiful UI** with Tailwind CSS and Alpine.js
- **Multiple Utility Tools** (password generator, QR codes, weather, etc.)

## MCP Tools Available

### Basic Tools
1. `greet_user(name)` - Greet a user by name
2. `add_numbers(a, b)` - Add two numbers
3. `multiply_numbers(a, b)` - Multiply two numbers
4. `calculate_area(length, width)` - Calculate rectangle area and perimeter

### Data Management
5. `create_user_mcp(name, email, age)` - Create a new user via MCP
6. `get_all_users()` - Get all users
7. `create_todo_mcp(task)` - Create a new todo via MCP
8. `get_all_todos()` - Get all todos

### System & Stats
9. `get_system_info()` - Get system information
10. `get_app_stats()` - Get application statistics

### Advanced Tools
11. `generate_password(length, include_symbols)` - Generate secure passwords
12. `convert_temperature(value, from_unit, to_unit)` - Temperature conversion
13. `text_analyzer(text)` - Analyze text (word count, sentiment, etc.)
14. `url_shortener(url)` - Create shortened URLs
15. `qr_code_generator(text)` - Generate QR codes
16. `weather_info(city)` - Get weather information
17. `file_info(file_path)` - Get file information
18. `color_palette_generator()` - Generate color palettes

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd fastapi-mcp-server
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Run Enhanced FastAPI Web Server
```bash
python enhanced_server.py
```
Access the interactive dashboard at: http://localhost:8001

### Run MCP Server
```bash
python enhanced_server.py mcp
```

### Test MCP Tools
```bash
python final_test.py
```

## Gemini CLI Integration

1. Install Gemini CLI:
```bash
npm install -g @google/generative-ai-cli
```

2. Configure MCP server in Gemini CLI:
```json
{
  "mcpServers": {
    "Enhanced FastAPI MCP Server": {
      "command": "python",
      "args": ["enhanced_server.py", "mcp"]
    }
  }
}
```

3. Test with Gemini CLI:
```bash
gemini mcp list
gemini mcp call greet_user --name "Alice"
gemini mcp call add_numbers --a 5 --b 3
```

## API Endpoints

- `GET /` - Welcome page
- `GET /health` - Health check
- `GET /users` - List all users
- `POST /users` - Create a new user
- `GET /todos` - List all todos
- `POST /todos` - Create a new todo
- `POST /calculate` - Perform calculations
- `GET /stats` - Application statistics
- `GET /docs` - Swagger UI documentation

## Project Structure

```
├── enhanced_server.py          # Main Enhanced FastAPI + MCP server
├── fastapi_mcp_server.py       # Original FastAPI + MCP server
├── fastapi_app.py              # Standalone FastAPI app
├── server.py                   # Simple MCP server
├── final_test.py               # Comprehensive MCP testing script
├── test_mcp_tools.py           # MCP tools testing script
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── SUBMISSION.md               # Submission details
└── gemini_cli_config.json     # Gemini CLI configuration
```

## Testing

Run the comprehensive test suite:
```bash
python final_test.py
```

Or run individual tests:
```bash
python test_mcp_tools.py
python quick_test.py
```

## License

MIT License
