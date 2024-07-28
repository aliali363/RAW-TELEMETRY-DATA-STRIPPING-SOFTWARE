import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
from PIL import Image, ImageTk
import sys
from tkinter import ttk
# G:\Vibin\Projects\pythonProject2\UI.py



def create_dataframe(lines):
    data = []
    for line in lines:
        x = line.split()
        data.append(x)
        #

    # print(data)
    col = ['Parameter'] + [f'Column{i + 1}' for i in range(len(data[0]) - 1)]
    df = pd.DataFrame(data, columns=col)

    df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric)

    return df


def read_bits(data, bit_offset, num_bits):
    byte_offset = bit_offset // 8
    bit_position = bit_offset % 8
    result = 0
    bits_read = 0

    # If num_bits is less than 8, read only that specific bit
    if num_bits < 8:
        return (data[byte_offset] >> (7 - bit_position)) & 1

    while bits_read < num_bits:
        current_byte = data[byte_offset]
        remaining_bits_in_byte = 8 - bit_position
        bits_to_read = min(num_bits - bits_read, remaining_bits_in_byte)
        mask = (1 << bits_to_read) - 1
        result <<= bits_to_read
        result |= (current_byte >> (remaining_bits_in_byte - bits_to_read)) & mask
        bits_read += bits_to_read
        bit_position = 0
        byte_offset += 1

    return result


def extract_data_from_bin(dataframe,binary_file_path,record_size,samp_num,timestamp_offset,timestamp_num_bits,parameter_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(parameter_folder):
        os.makedirs(parameter_folder)

    # Initialize files for each parameter
    parameter_files = {}
    for parameter in dataframe['Parameter'].unique():
        file_name = f"{parameter}.txt"
        file_path = os.path.join(parameter_folder, file_name)
        parameter_files[parameter] = open(file_path, "w")

    with open(binary_file_path, 'rb') as file:
        df_new = dataframe[(dataframe['Column2'] == int(samp_num)) | (dataframe['Column2'] == 0)]
        record_index = 0

        while True:
            record_position = file.tell()
            record = file.read(record_size)
            if not record:
                break

            results = {}  # Initialize results dictionary for each record

            # Read timestamp value
            file.seek(record_position + (timestamp_offset // 8))
            timestamp_data = file.read((timestamp_num_bits + 7) // 8)
            timestamp_value = read_bits(timestamp_data, timestamp_offset % 8, timestamp_num_bits)

            for _, row in df_new.iterrows():
                parameter = row['Parameter']
                num_samples = row['Column1']
                offset = row['Column4']
                num_bits = row['Column8']
                increment = row['Column5']
                parameter_results = []

                for i in range(int(num_samples)):
                    current_offset = int(offset) + (i * int(increment))
                    byte_offset = current_offset // 8
                    bit_position = current_offset % 8

                    file.seek(record_position + byte_offset)
                    data = file.read((bit_position + int(num_bits) + 7) // 8)

                    extracted_bits = read_bits(data, bit_position, int(num_bits))
                    parameter_results.append(hex(extracted_bits))

                if parameter not in results:
                    results[parameter] = []

                results[parameter].append(parameter_results)
            
            # Write results to corresponding parameter files for each record
            for parameter, data in results.items():
                parameter_file = parameter_files[parameter]
                parameter_file.write(f"{record_index}, {timestamp_value}")
                max_samples = max(df_new[df_new['Parameter'] == parameter]['Column1'])
                for sample_set in data:
                    for sample in sample_set:
                        parameter_file.write(f", {sample}" if sample != '-' else ", -")
                parameter_file.write("\n")

            record_index += 1

    # Close all parameter files
    for parameter_file in parameter_files.values():
        parameter_file.close()


def update_params():
    # Extracting Data from the File 1 and storing it in DataFrames using Panda
    file_path = file1_entry.get()

    with open(file_path, 'r') as file:
        lines = file.readlines()
    df = create_dataframe(lines)

    # Extraction of data from the binary file
    bin_file = file2_entry.get()
    record_size = int(file3_entry.get())
    sample_number = int(file4_entry.get())
    timestamp_offset = int(file6_entry.get())
    timestamp_num_bits = int(file7_entry.get())

    parameter_folder = "."

    extract_data_from_bin(df, bin_file, record_size, sample_number, timestamp_offset, timestamp_num_bits, parameter_folder)

    # Display a dialog box with the output folder directory
    messagebox.showinfo("Parameters Folder", f"Parameter files are saved in: {os.path.abspath(parameter_folder)}")

    sys.exit(1)


def browser_file1():
    path = filedialog.askopenfilename()
    file1_entry.insert(0, path)


def browser_file2():
    path = filedialog.askopenfilename()
    file2_entry.insert(0, path)

#gui
def resize(event=None):
    new_width = root.winfo_width()
    new_height = root.winfo_height()

    # Resize the background image
    resized_image = background_image.resize((new_width, new_height), Image.ANTIALIAS)
    background_photo = ImageTk.PhotoImage(resized_image)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")
    canvas.image = background_photo  # Keep a reference to avoid garbage collection

    # Reposition buttons and entries
    canvas.coords(file8_label_window, new_width // 2, new_height // 2 -200)

    #canvas.coords(file1_label_window, (new_width // 2 - 100), new_height // 2 - 150)
    #canvas.coords(file1_entry_window, new_width // 2 , new_height // 2 - 150)
    canvas.coords(file1_button_window, new_width // 2 , new_height // 2 - 150)

    #canvas.coords(file2_label_window, new_width // 2 - 100, new_height // 2 - 100)
    #canvas.coords(file2_entry_window, new_width // 2, new_height // 2 - 100)
    canvas.coords(file2_button_window, new_width // 2, new_height // 2 - 100)

    canvas.coords(file3_label_window, new_width // 2 - 100, new_height // 2 - 50)
    canvas.coords(file3_entry_window, (new_width // 2) + 28, new_height // 2 - 50)

    canvas.coords(file4_label_window, new_width // 2 - 100, new_height // 2 - 0)
    canvas.coords(file4_entry_window, (new_width // 2) + 42, new_height // 2 - 0)

    canvas.coords(file5_label_window, new_width // 2 , new_height // 2 + 50)

    canvas.coords(file6_label_window, new_width // 2 - 100, new_height // 2 + 100)
    canvas.coords(file6_entry_window, (new_width // 2) + 33, new_height // 2 + 100)

    canvas.coords(file7_label_window, new_width // 2 - 100, new_height // 2 + 150)
    canvas.coords(file7_entry_window, (new_width // 2) + 28, new_height // 2 + 150)



    canvas.coords(update_button_window, new_width // 2, new_height // 2 + 200)

# Create main application window
root = tk.Tk()
root.title("Integrated File Handler")
root.geometry("1920x1080")

# Set background image
background_image_path = r"C:\Users\SDSC-SHAR\Desktop\project\Waste proj\pic.png"
background_image = Image.open(background_image_path)

# Create a canvas to place the background image
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)

file8_label = tk.Label(root, text="RAW DATA STRIPPING", bg= 'BLUE' , fg='WHITE')
file8_label_window = canvas.create_window(400, 180, window=file8_label)


# Create entry widgets for the file paths
#file1_label = tk.Label(root, text="File 1:")
#file1_label_window = canvas.create_window(400, 200, window=file1_label)
file1_entry = tk.Entry(root)
#file1_entry_window = canvas.create_window(400, 230, window=file1_entry)
file1_button = tk.Button(root, text="Upload file..", command=browser_file1 , bg= 'black' , fg='white')   # Using ttk.Button
file1_button_window = canvas.create_window(400, 260, window=file1_button)

#file2_label = tk.Label(root, text="Binary File:")
#file2_label_window = canvas.create_window(400, 300, window=file2_label)
file2_entry = tk.Entry(root)
#file2_entry_window = canvas.create_window(400, 330, window=file2_entry)
file2_button = tk.Button(root, text="Upload binary files...", command=browser_file2)  # Using ttk.Button
file2_button_window = canvas.create_window(400, 360, window=file2_button)

file3_label = tk.Label(root, text="Record Size:")
file3_label_window = canvas.create_window(400, 400, window=file3_label)
file3_entry = tk.Entry(root)
file3_entry_window = canvas.create_window(400, 430, window=file3_entry)

file4_label = tk.Label(root, text="Sample number:")
file4_label_window = canvas.create_window(400, 500, window=file4_label)
file4_entry = tk.Entry(root)
file4_entry_window = canvas.create_window(400, 530, window=file4_entry)

# INPUT FOR TIMESTAMP OFFSET
file5_label = tk.Label(root, text="Time Stamp", bg= 'red' , fg='yellow')
file5_label_window = canvas.create_window(400, 600, window=file5_label)

file6_label = tk.Label(root, text="Offset value : ")
file6_label_window = canvas.create_window(400, 700, window=file6_label)
file6_entry = tk.Entry(root)
file6_entry_window = canvas.create_window(400, 730, window=file6_entry)

# INPUT FOR TIMESTAMP NUMBER OF BITS TO READ
file7_label = tk.Label(root, text="No. of bits : ")
file7_label_window = canvas.create_window(400, 800, window=file7_label)
file7_entry = tk.Entry(root)
file7_entry_window = canvas.create_window(400, 830, window=file7_entry)

# button to update the third file
update_button = ttk.Button(root, text="SUBMIT", command=update_params)  # Using ttk.Button
update_button_window = canvas.create_window(400, 900, window=update_button)

# Bind the configure event to the resize function
root.bind("<Configure>", resize)

# Initial call to resize to set background and positions
root.update_idletasks()  # Ensure the window is fully loaded
resize()  # Call resize without parameters

root.mainloop()



