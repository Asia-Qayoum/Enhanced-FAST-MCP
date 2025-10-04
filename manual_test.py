#!/usr/bin/env python3
"""
Manual tool testing script
"""
import subprocess
import json
import sys

def test_tool(tool_name, args):
    """Test a specific tool"""
    request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": tool_name,
            "arguments": args
        }
    }
    
    process = subprocess.Popen(
        [sys.executable, "server.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    try:
        # Initialize
        init_request = {
            "jsonrpc": "2.0",
            "id": 0,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {"name": "test", "version": "1.0"}
            }
        }
        process.stdin.write(json.dumps(init_request) + "\n")
        process.stdin.flush()
        process.stdout.readline()  # Skip init response
        
        # Test tool
        process.stdin.write(json.dumps(request) + "\n")
        process.stdin.flush()
        response = process.stdout.readline()
        
        if response:
            result = json.loads(response.strip())
            print(f"Testing {tool_name}:")
            print(json.dumps(result, indent=2))
            return result
    finally:
        process.terminate()
        process.wait()

if __name__ == "__main__":
    print("=== FastMCP Tool Testing ===\n")
    
    # Test greet
    test_tool("greet", {"name": "Alice"})
    print()
    
    # Test add
    test_tool("add", {"a": 10, "b": 5})
    print()
    
    # Test multiply
    test_tool("multiply", {"a": 3.5, "b": 2.0})
    print()
    
    # Test system info
    test_tool("get_system_info", {})
    print()
    
    # Test todo list
    test_tool("create_todo_list", {"items": ["Buy groceries", "Walk dog", "Read book"]})
    print()
    
    # Test area calculation
    test_tool("calculate_area", {"length": 5.0, "width": 3.0})
