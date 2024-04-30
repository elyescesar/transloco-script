import clipboard
import time
import threading

def monitor_clipboard():
    last_clipboard_content = clipboard.paste()
    while True:
        current_clipboard_content = clipboard.paste()
        if current_clipboard_content != last_clipboard_content:
            if current_clipboard_content:
                new_text = "{{ '" + current_clipboard_content + "' | transloco }}"
                clipboard.copy(new_text)
                print("Clipboard content modified.")
            else:
                print("No text was highlighted.")
            last_clipboard_content = new_text
        time.sleep(0.2)

clipboard_thread = threading.Thread(target=monitor_clipboard)
clipboard_thread.daemon = True
clipboard_thread.start()

while True: 
    time.sleep(1)
