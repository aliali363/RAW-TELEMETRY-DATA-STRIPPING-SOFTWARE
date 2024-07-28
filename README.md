# Telemetry Raw Data Stripping Software using Python


Welcome to the **Telemetry Raw Data Stripping Software** project! This application is designed to revolutionize ISRO's telemetry data processing capabilities by automating the creation of output files. Our goal is to ensure data accuracy, operational efficiency, and consistency, which are crucial for the success of ISRO's missions.

<div align="center">
  ![giphy (1)](https://github.com/user-attachments/assets/cc6bcd0d-de89-4e7e-a9ba-26aabf762d5a)
</div>


## Key Features

- **User-Friendly GUI**: Built with Tkinter, our application features an intuitive interface for easy navigation.
  
- **File Handling**: Supports uploading of Tab and Binary files for telemetry data processing.

- **Data Extraction**: Automatically extracts specific packet details for individual parameters.

- **Output Generation**: Creates separate `.dat` files formatted in hexadecimal for each parameter.

## How It Works

1. **Upload Files**: Users can upload Tab and Binary files through the GUI.
  
2. **Input Parameters**: Enter the record size, stream/sample number, offset value, and bit size number of the timestamp.

3. **Process Data**: The software processes the input files, applying extensive string matching and exception handling.

4. **Output Files**: Generates formatted output files ready for visualization and analysis.

## Libraries Used

The software utilizes several Python libraries to enhance functionality:

- **Tkinter**: For creating the GUI.
- **Pandas**: For data manipulation and analysis.
- **Pillow**: For handling images in the GUI.
- **OS**: For file system operations.
- **sys**: For interacting with the Python interpreter.

## Installation

To get started, clone the repository and install the required libraries:

```bash
git clone https://github.com/your-repo/telemetry-data-stripping-software.git
cd telemetry-data-stripping-software
pip install -r requirements.txt
