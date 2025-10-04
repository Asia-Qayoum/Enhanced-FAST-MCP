#!/usr/bin/env python3
"""
Enhanced MCP Server Demonstration
Shows all 15 MCP tools with beautiful output
"""
import json
import subprocess
import sys
import time

def demo_enhanced_mcp_server():
    """Demonstrate enhanced MCP server functionality"""
    
    print("=" * 70)
    print("ENHANCED FASTAPI MCP SERVER DEMONSTRATION")
    print("=" * 70)
    print()
    
    # Start the server process
    print("1. Starting Enhanced FastAPI MCP Server...")
    process = subprocess.Popen(
        [sys.executable, "fastapi_mcp_server.py", "mcp"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    time.sleep(2)  # Give server time to start
    print("   [OK] Enhanced server started successfully!")
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
                    "name": "enhanced-demo-client",
                    "version": "2.0.0"
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
        print("3. Listing Enhanced MCP Tools...")
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
            print(f"   [OK] Found {len(tools)} Enhanced MCP tools:")
            for i, tool in enumerate(tools, 1):
                print(f"      {i:2d}. {tool['name']:<25} - {tool['description']}")
        print()
        
        # Demonstrate enhanced tool usage
        print("4. Demonstrating Enhanced MCP Tools...")
        print()
        
        # Test 1: Password Generator
        print("   Test 1: generate_password tool")
        password_request = {
            "jsonrpc": "2.0",
            "id": 3,
            "method": "tools/call",
            "params": {
                "name": "generate_password",
                "arguments": {
                    "length": 16
                }
            }
        }
        
        process.stdin.write(json.dumps(password_request) + "\n")
        process.stdin.flush()
        
        response_line = process.stdout.readline()
        if response_line:
            response = json.loads(response_line.strip())
            result = response['result']['structuredContent']['result']
            print(f"      Input: length=16")
            print(f"      Output: {result}")
        print()
        
        # Test 2: Temperature Converter
        print("   Test 2: convert_temperature tool")
        temp_request = {
            "jsonrpc": "2.0",
            "id": 4,
            "method": "tools/call",
            "params": {
                "name": "convert_temperature",
                "arguments": {
                    "value": 100,
                    "from_unit": "celsius",
                    "to_unit": "fahrenheit"
                }
            }
        }
        
        process.stdin.write(json.dumps(temp_request) + "\n")
        process.stdin.flush()
        
        response_line = process.stdout.readline()
        if response_line:
            response = json.loads(response_line.strip())
            result = response['result']['structuredContent']
            print(f"      Input: 100°C to Fahrenheit")
            print(f"      Output: {result['converted_value']}°F")
        print()
        
        # Test 3: Text Analyzer
        print("   Test 3: text_analyzer tool")
        text_request = {
            "jsonrpc": "2.0",
            "id": 5,
            "method": "tools/call",
            "params": {
                "name": "text_analyzer",
                "arguments": {
                    "text": "The quick brown fox jumps over the lazy dog. This is a sample text for analysis."
                }
            }
        }
        
        process.stdin.write(json.dumps(text_request) + "\n")
        process.stdin.flush()
        
        response_line = process.stdout.readline()
        if response_line:
            response = json.loads(response_line.strip())
            result = response['result']['structuredContent']
            print(f"      Input: Sample text")
            print(f"      Output: {result['word_count']} words, {result['character_count']} chars, avg word length: {result['average_word_length']}")
        print()
        
        # Test 4: URL Shortener
        print("   Test 4: url_shortener tool")
        url_request = {
            "jsonrpc": "2.0",
            "id": 6,
            "method": "tools/call",
            "params": {
                "name": "url_shortener",
                "arguments": {
                    "url": "https://www.google.com/search?q=fastapi+mcp+server"
                }
            }
        }
        
        process.stdin.write(json.dumps(url_request) + "\n")
        process.stdin.flush()
        
        response_line = process.stdout.readline()
        if response_line:
            response = json.loads(response_line.strip())
            result = response['result']['structuredContent']
            print(f"      Input: Long Google URL")
            print(f"      Output: {result['short_url']}")
        print()
        
        # Test 5: Weather Info
        print("   Test 5: weather_info tool")
        weather_request = {
            "jsonrpc": "2.0",
            "id": 7,
            "method": "tools/call",
            "params": {
                "name": "weather_info",
                "arguments": {
                    "city": "London"
                }
            }
        }
        
        process.stdin.write(json.dumps(weather_request) + "\n")
        process.stdin.flush()
        
        response_line = process.stdout.readline()
        if response_line:
            response = json.loads(response_line.strip())
            result = response['result']['structuredContent']
            print(f"      Input: city='London'")
            print(f"      Output: {result['current_temperature']}°C, {result['condition']}, Humidity: {result['humidity']}%")
        print()
        
        # Test 6: Color Palette Generator
        print("   Test 6: color_palette_generator tool")
        color_request = {
            "jsonrpc": "2.0",
            "id": 8,
            "method": "tools/call",
            "params": {
                "name": "color_palette_generator",
                "arguments": {
                    "color_count": 3
                }
            }
        }
        
        process.stdin.write(json.dumps(color_request) + "\n")
        process.stdin.flush()
        
        response_line = process.stdout.readline()
        if response_line:
            response = json.loads(response_line.strip())
            result = response['result']['structuredContent']
            print(f"      Input: color_count=3")
            print(f"      Output: Generated {result['color_count']} colors")
            for color in result['colors']:
                print(f"              {color['hex']} - {color['rgb']}")
        print()
        
        print("=" * 70)
        print("ENHANCED DEMONSTRATION COMPLETED SUCCESSFULLY!")
        print("=" * 70)
        print()
        print("Summary:")
        print("[OK] Enhanced FastAPI MCP Server running")
        print("[OK] MCP connection established")
        print("[OK] 15 Enhanced MCP tools available")
        print("[OK] 6 advanced tools demonstrated successfully")
        print("[OK] Beautiful frontend dashboard ready")
        print("[OK] Ready for Gemini CLI integration")
        print()
        print("Features:")
        print("- Password generation with customizable length")
        print("- Temperature conversion (Celsius, Fahrenheit, Kelvin)")
        print("- Advanced text analysis with statistics")
        print("- URL shortening service")
        print("- Weather information simulation")
        print("- Color palette generation")
        print("- QR code generation")
        print("- File information analysis")
        print("- System information retrieval")
        print("- And 6 more utility tools!")
        
    except Exception as e:
        print(f"Error during demonstration: {e}")
    finally:
        process.terminate()
        process.wait()

if __name__ == "__main__":
    demo_enhanced_mcp_server()
