#!/usr/bin/env python3
"""
Simple MCP Server Test - Working Version
"""
import json
import subprocess
import sys

def test_mcp_server():
    """Test the MCP server with proper initialization"""
    
    # Start the server process
    process = subprocess.Popen(
        [sys.executable, "fastapi_mcp_server.py", "mcp"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    try:
        # Send initialize request
        init_request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {
                    "name": "test-client",
                    "version": "1.0.0"
                }
            }
        }
        
        print("Sending initialize request...")
        process.stdin.write(json.dumps(init_request) + "\n")
        process.stdin.flush()
        
        # Read response
        response_line = process.stdout.readline()
        if response_line:
            response = json.loads(response_line.strip())
            print(f"Initialize response: {json.dumps(response, indent=2)}")
        
        # Send initialized notification
        initialized_notification = {
            "jsonrpc": "2.0",
            "method": "notifications/initialized"
        }
        
        print("\nSending initialized notification...")
        process.stdin.write(json.dumps(initialized_notification) + "\n")
        process.stdin.flush()
        
        # Send tools/list request
        tools_request = {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/list"
        }
        
        print("\nSending tools/list request...")
        process.stdin.write(json.dumps(tools_request) + "\n")
        process.stdin.flush()
        
        # Read response
        response_line = process.stdout.readline()
        if response_line:
            response = json.loads(response_line.strip())
            print(f"Tools list: {json.dumps(response, indent=2)}")
        
        # Test greet tool
        greet_request = {
            "jsonrpc": "2.0",
            "id": 3,
            "method": "tools/call",
            "params": {
                "name": "greet_user",
                "arguments": {
                    "name": "World"
                }
            }
        }
        
        print("\nTesting greet_user tool...")
        process.stdin.write(json.dumps(greet_request) + "\n")
        process.stdin.flush()
        
        # Read response
        response_line = process.stdout.readline()
        if response_line:
            response = json.loads(response_line.strip())
            print(f"Greet result: {json.dumps(response, indent=2)}")
        
        # Test add tool
        add_request = {
            "jsonrpc": "2.0",
            "id": 4,
            "method": "tools/call",
            "params": {
                "name": "add_numbers",
                "arguments": {
                    "a": 5,
                    "b": 3
                }
            }
        }
        
        print("\nTesting add_numbers tool...")
        process.stdin.write(json.dumps(add_request) + "\n")
        process.stdin.flush()
        
        # Read response
        response_line = process.stdout.readline()
        if response_line:
            response = json.loads(response_line.strip())
            print(f"Add result: {json.dumps(response, indent=2)}")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        process.terminate()
        process.wait()

if __name__ == "__main__":
    print("Testing FastAPI MCP Server...")
    test_mcp_server()
