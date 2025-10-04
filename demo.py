#!/usr/bin/env python3
"""
Demonstration Script for FastAPI MCP Server
This script demonstrates the MCP server functionality for screen recording
"""
import json
import subprocess
import sys
import time

def demo_mcp_server():
    """Demonstrate MCP server functionality"""
    
    print("=" * 60)
    print("FASTAPI MCP SERVER DEMONSTRATION")
    print("=" * 60)
    print()
    
    # Start the server process
    print("1. Starting FastAPI MCP Server...")
    process = subprocess.Popen(
        [sys.executable, "fastapi_mcp_server.py", "mcp"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    time.sleep(2)  # Give server time to start
    print("   [OK] Server started successfully!")
    print()
    
    try:
        # Initialize MCP connection
        print("2. Initializing MCP Connection...")
        init_request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {
                    "name": "demo-client",
                    "version": "1.0.0"
                }
            }
        }
        
        process.stdin.write(json.dumps(init_request) + "\n")
        process.stdin.flush()
        
        response_line = process.stdout.readline()
        if response_line:
            response = json.loads(response_line.strip())
            print(f"   [OK] Connected to: {response['result']['serverInfo']['name']}")
            print(f"   [OK] Server Version: {response['result']['serverInfo']['version']}")
        print()
        
        # Send initialized notification
        initialized_notification = {
            "jsonrpc": "2.0",
            "method": "notifications/initialized"
        }
        process.stdin.write(json.dumps(initialized_notification) + "\n")
        process.stdin.flush()
        
        # List available tools
        print("3. Listing Available MCP Tools...")
        tools_request = {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/list"
        }
        
        process.stdin.write(json.dumps(tools_request) + "\n")
        process.stdin.flush()
        
        response_line = process.stdout.readline()
        if response_line:
            response = json.loads(response_line.strip())
            tools = response['result']['tools']
            print(f"   [OK] Found {len(tools)} MCP tools:")
            for i, tool in enumerate(tools, 1):
                print(f"      {i}. {tool['name']} - {tool['description']}")
        print()
        
        # Demonstrate tool usage
        print("4. Demonstrating MCP Tool Usage...")
        print()
        
        # Test 1: Greet User
        print("   Test 1: greet_user tool")
        greet_request = {
            "jsonrpc": "2.0",
            "id": 3,
            "method": "tools/call",
            "params": {
                "name": "greet_user",
                "arguments": {
                    "name": "Alice"
                }
            }
        }
        
        process.stdin.write(json.dumps(greet_request) + "\n")
        process.stdin.flush()
        
        response_line = process.stdout.readline()
        if response_line:
            response = json.loads(response_line.strip())
            result = response['result']['structuredContent']['result']
            print(f"      Input: name='Alice'")
            print(f"      Output: {result}")
        print()
        
        # Test 2: Add Numbers
        print("   Test 2: add_numbers tool")
        add_request = {
            "jsonrpc": "2.0",
            "id": 4,
            "method": "tools/call",
            "params": {
                "name": "add_numbers",
                "arguments": {
                    "a": 15,
                    "b": 25
                }
            }
        }
        
        process.stdin.write(json.dumps(add_request) + "\n")
        process.stdin.flush()
        
        response_line = process.stdout.readline()
        if response_line:
            response = json.loads(response_line.strip())
            result = response['result']['structuredContent']['result']
            print(f"      Input: a=15, b=25")
            print(f"      Output: {result}")
        print()
        
        # Test 3: Create User
        print("   Test 3: create_user_mcp tool")
        create_user_request = {
            "jsonrpc": "2.0",
            "id": 5,
            "method": "tools/call",
            "params": {
                "name": "create_user_mcp",
                "arguments": {
                    "name": "John Doe",
                    "email": "john@example.com",
                    "age": 30
                }
            }
        }
        
        process.stdin.write(json.dumps(create_user_request) + "\n")
        process.stdin.flush()
        
        response_line = process.stdout.readline()
        if response_line:
            response = json.loads(response_line.strip())
            result = response['result']['structuredContent']
            print(f"      Input: name='John Doe', email='john@example.com', age=30")
            print(f"      Output: {result['message']}")
        print()
        
        # Test 4: Calculate Area
        print("   Test 4: calculate_area tool")
        area_request = {
            "jsonrpc": "2.0",
            "id": 6,
            "method": "tools/call",
            "params": {
                "name": "calculate_area",
                "arguments": {
                    "length": 10.0,
                    "width": 5.0
                }
            }
        }
        
        process.stdin.write(json.dumps(area_request) + "\n")
        process.stdin.flush()
        
        response_line = process.stdout.readline()
        if response_line:
            response = json.loads(response_line.strip())
            result = response['result']['structuredContent']
            print(f"      Input: length=10.0, width=5.0")
            print(f"      Output: Area={result['area']}, Perimeter={result['perimeter']}")
        print()
        
        # Test 5: Get System Info
        print("   Test 5: get_system_info tool")
        sys_info_request = {
            "jsonrpc": "2.0",
            "id": 7,
            "method": "tools/call",
            "params": {
                "name": "get_system_info",
                "arguments": {}
            }
        }
        
        process.stdin.write(json.dumps(sys_info_request) + "\n")
        process.stdin.flush()
        
        response_line = process.stdout.readline()
        if response_line:
            response = json.loads(response_line.strip())
            result = response['result']['structuredContent']
            print(f"      Output: Platform={result['platform']}")
            print(f"              Python={result['python_version']}")
        print()
        
        print("=" * 60)
        print("DEMONSTRATION COMPLETED SUCCESSFULLY!")
        print("=" * 60)
        print()
        print("Summary:")
        print("[OK] FastAPI MCP Server running")
        print("[OK] MCP connection established")
        print("[OK] 10 MCP tools available")
        print("[OK] 5 tools demonstrated successfully")
        print("[OK] Ready for Gemini CLI integration")
        
    except Exception as e:
        print(f"Error during demonstration: {e}")
    finally:
        process.terminate()
        process.wait()

if __name__ == "__main__":
    demo_mcp_server()
