# RAW-TELEMETRY-DATA-STRIPPING-SOFTWARE
 The "Telemetry Raw Data Stripping Software using Python" project is poised to make a substantial impact on ISRO's telemetry data processing capabilities. By automating the creation of output files, the system ensures data accuracy, operational efficiency, and consistency, all of which are essential for the success of ISRO's missions. 
The primary users of the system will be data analysts, engineers, and scientists at ISRO involved in telemetry data processing. They are expected to have a basic understanding of data formats and processing techniques. The objective of this project is to extract raw telemetry data, focusing on extracting specific packet details for individual parameters. The next step involves creating separate .dat files for each parameter, formatted in hexadecimal, which will be instrumental for subsequent visualization tasks.
This has been accomplished using extensive string matching and exception handling. Some human errors still persist, not following the rule-based processing of the parameters of the document. Most of these have been handled by prompting the user.
This Python code defines a graphical user interface (GUI) application using the Tkinter library for processing and stripping input files, specifically Tab files and Binary files. The application is designed for generating Raw Telemetry data stripping software.
The GUI includes buttons for uploading tab file (telemetry data) and binary file and the user input such as record size, stream/sample number, offset value and bit size number of the time stamp, button to submit. The interface is visually appealing with background images and logos related to the Indian Space Research Organisation (ISRO).
This “Telemetry Raw Data Stripping Software using python” aims to empower users with a versatile tool for preprocessing raw data, streamlining the data preparation phase, and facilitating more efficient downstream analysis and decision-making processes.
Overall, this GUI application streamlines the process of files and processing, providing a user-friendly interface for handling input files effectively.


# Libraries Used:
The Python program leverages the following libraries to facilitate data handling, file manipulation, and error checking:
⮚	Operating System (OS): This module provides a portable way of using operating system-dependent functionality, such as reading or writing to the file system and manipulating file paths.
⮚	Tkinter: It's a standard GUI (Graphical User Interface) library for Python. You're using it to create the main application window, labels, buttons, entry widgets, and file dialogs.
⮚	File dialog: This submodule of tkinter provides dialog boxes for file selection.
⮚	Message box: Another submodule of tkinter, it provides dialog boxes for showing messages to the user.
⮚	Pandas: It's a powerful data manipulation library. Used to create and manipulate Data Frames, which are tabular data structures used for storing and analysing data.
⮚	Pillow (Python Imaging Library (PIL)): It's used for opening, manipulating, and saving many different images file formats. You're using it to handle images in your GUI application.
⮚	sys: This module provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter.
⮚	ttk (themed tkinter): This submodule of tkinter provides access to the Tk themed widget set.
