import dearpygui.dearpygui as dpg
import shutil
import time

version_id = 1
interval = 30

def set_interval(sender, app_data):
    global interval
    interval = app_data

def copy_file_manual():
    global version_id

    source = f"example-file.txt"
    target = f"example-file{version_id}.txt"
    version_id += 1
    shutil.copyfile(source, target)
    print(f"File {target} copied manually.")

def copy_file_automatic():
    global version_id

    source = f"example-file.txt"
    target = f"example-file{version_id}.txt"
    version_id += 1
    shutil.copyfile(source, target)
    print(f"File {target} copied automatically.")

def run_gui():
    dpg.create_context()
    dpg.create_viewport()
    dpg.setup_dearpygui()

    with dpg.window(label="Example Window"):
        dpg.add_text("Hello world")
        dpg.add_button(label="Copy File", callback=copy_file_manual)
        dpg.add_slider_float(label="Interval", default_value=interval, min_value=10.0, max_value=60.0, callback=set_interval)

    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

# Start GUI
run_gui()

while True:
    copy_file_automatic()
    time.sleep(interval)