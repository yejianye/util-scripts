#!/usr/bin/env python
import subprocess
import argparse
import sys

def run_command(command, input=None):
    """Run a shell command and return its stdout as a string"""
    result = subprocess.run(command, shell=True, capture_output=True, text=True, input=input)
    return result.stdout

def run_apple_script(script_str):
    """Run an AppleScript and return its stdout as a string"""
    result = subprocess.run(['osascript', '-e', script_str], capture_output=True, text=True)
    return result.stdout

def copy_to_clipboard(text, html):
    """Copy text and HTML to clipboard on macOS"""
    if not html:
        html = text
    html = run_command("hexdump -ve '1/1 \"%.2x\"'", input=html)
    run_apple_script(f'set the clipboard to {{text:"{text}", «class HTML»:«data HTML{html}»}}')

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Command line tool for clipboard operations')
    parser.add_argument('--text', default='', help='Text content')
    parser.add_argument('--html', default='', help='HTML content')
    
    args = parser.parse_args()
    if args.text == 'stdin':
        args.text = sys.stdin.read()

    if args.html == 'stdin':
        args.html = sys.stdin.read()
    
    copy_to_clipboard(args.text, args.html)
