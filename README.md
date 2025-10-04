# FastAPI MCP Server

A sample FastAPI application with integrated Model Context Protocol (MCP) server using FastMCP.

## Features

- **FastAPI Web Application** with REST endpoints
- **MCP Server Integration** with 9 available tools
- **Gemini CLI Compatible** for AI assistant integration
- **Real-time Data Management** for users and todos

## MCP Tools Available

1. `greet_user(name)` - Greet a user by name
2. `add_numbers(a, b)` - Add two numbers
3. `multiply_numbers(a, b)` - Multiply two numbers
4. `create_user_mcp(name, email, age)` - Create a new user via MCP
5. `get_all_users()` - Get all users
6. `create_todo_mcp(task)` - Create a new todo via MCP
7. `get_all_todos()` - Get all todos
8. `calculate_area(length, width)` - Calculate rectangle area and perimeter
9. `get_system_info()` - Get system information
10. `get_app_stats()` - Get application statistics

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

### Run FastAPI Web Server
```bash
python fastapi_mcp_server.py
```
Access the web interface at: http://localhost:8000

### Run MCP Server
```bash
python fastapi_mcp_server.py mcp
```

### Test MCP Tools
```bash
python test_mcp_tools.py
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
    "FastAPI MCP Server": {
      "command": "python",
      "args": ["fastapi_mcp_server.py", "mcp"]
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
├── fastapi_mcp_server.py    # Main FastAPI + MCP server
├── fastapi_app.py          # Standalone FastAPI app
├── server.py               # Simple MCP server
├── test_mcp_tools.py       # MCP tools testing script
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── claude_desktop_config.json  # Claude Desktop configuration
```

## Testing

Run the test suite:
```bash
python test_mcp_tools.py
```

## Screen Recording

A screen recording demonstrating:
1. MCP server running
2. Gemini CLI MCP list command
3. Usage of MCP tools

[Link to screen recording will be provided]

## License

MIT License
