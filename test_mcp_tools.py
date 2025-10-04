#!/usr/bin/env python3
"""
Comprehensive MCP Tools Testing Script
Tests all MCP tools available in the FastAPI MCP Server
"""
import asyncio
import json
import subprocess
import sys
from typing import Any, Dict

class MCPTester:
    def __init__(self):
        self.process = None
    
    async def start_server(self):
        """Start the MCP server"""
        self.process = subprocess.Popen(
            [sys.executable, "fastapi_mcp_server.py", "mcp"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        await asyncio.sleep(2)  # Give server time to start
    
    async def send_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Send a request to the MCP server"""
        try:
            self.process.stdin.write(json.dumps(request) + "\n")
            self.process.stdin.flush()
            
            response_line = self.process.stdout.readline()
            if response_line:
                return json.loads(response_line.strip())
            return {"error": "No response received"}
        except Exception as e:
            return {"error": str(e)}
    
    async def initialize(self):
        """Initialize the MCP connection"""
        init_request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {
                    "name": "mcp-tester",
                    "version": "1.0.0"
                }
            }
        }
        
        print("Initializing MCP connection...")
        response = await self.send_request(init_request)
        if "result" in response:
            print("MCP connection initialized successfully!")
            print(f"   Server: {response['result']['serverInfo']['name']}")
            print(f"   Version: {response['result']['serverInfo']['version']}")
        else:
            print(f"Initialization failed: {response}")
        return response
    
    async def test_tool(self, tool_name: str, args: Dict[str, Any], description: str):
        """Test a specific MCP tool"""
        print(f"\nTesting {tool_name}: {description}")
        
        request = {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/call",
            "params": {
                "name": tool_name,
                "arguments": args
            }
        }
        
        response = await self.send_request(request)
        
        if "result" in response:
            print(f"SUCCESS - {tool_name}")
            print(f"   Result: {json.dumps(response['result'], indent=2)}")
        else:
            print(f"FAILED - {tool_name}")
            print(f"   Error: {response.get('error', 'Unknown error')}")
        
        return response
    
    async def run_all_tests(self):
        """Run all MCP tool tests"""
        print("Starting FastAPI MCP Server Tests")
        print("=" * 50)
        
        await self.start_server()
        await self.initialize()
        
        # Test all available tools
        tests = [
            ("greet_user", {"name": "Alice"}, "Greet a user"),
            ("add_numbers", {"a": 15, "b": 25}, "Add two numbers"),
            ("multiply_numbers", {"a": 4.5, "b": 2.0}, "Multiply two numbers"),
            ("create_user_mcp", {"name": "John Doe", "email": "john@example.com", "age": 30}, "Create user via MCP"),
            ("get_all_users", {}, "Get all users"),
            ("create_todo_mcp", {"task": "Complete MCP project"}, "Create todo via MCP"),
            ("get_all_todos", {}, "Get all todos"),
            ("calculate_area", {"length": 10.0, "width": 5.0}, "Calculate rectangle area"),
            ("get_system_info", {}, "Get system information"),
            ("get_app_stats", {}, "Get application statistics")
        ]
        
        print(f"\nRunning {len(tests)} MCP tool tests...")
        
        for tool_name, args, description in tests:
            await self.test_tool(tool_name, args, description)
        
        print("\n" + "=" * 50)
        print("All tests completed!")
    
    async def cleanup(self):
        """Clean up the server process"""
        if self.process:
            self.process.terminate()
            self.process.wait()

async def main():
    tester = MCPTester()
    try:
        await tester.run_all_tests()
    finally:
        await tester.cleanup()

if __name__ == "__main__":
    asyncio.run(main())
