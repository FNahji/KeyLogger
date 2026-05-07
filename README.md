# Keylogger

A Python based keylogger built to understand how keystroke capture works at a low level, a core concept in both offensive security and malware analysis.

Built for educational purposes. Only run on your own machine.

## What I Learned
- How attackers capture keystrokes silently
- Python file I/O with real-time flushing
- Handling keyboard input objects vs string characters
- Clean process termination using listener return values

## Features
- Logs all keystrokes including special keys
- Records session start and end timestamps
- Press Escape to stop cleanly
- Saves all output to log.txt

## Usage
Run the script. Press any keys to log them. Press Escape to end the session.

## Example Output
--- Session started: 2026-05-08 00:21:12 ---

hello[Key.space]world[Key.s

--- Session ended: 2026-05-08 00:30:12 ---
