# local_simple_cloud
Simple Local Cloud: An application built with FastAPI, HTML, and JavaScript. This application allows you to create a local cloud to store and access your files easily and securely. Upload, download, and manage your files from any device using this straightforward and customizable solution.



# FastAPI Program

This is a FastAPI program that provides file upload, download, and deletion functionality. It uses FastAPI, Jinja2Templates, and static files.

## Folder Structure

The program consists of the following folders:

- `templates`: Contains HTML templates used for rendering the web pages.
- `static`: Contains static files such as CSS stylesheets, JavaScript files, etc.

## Installation

1. Clone the repository:

  #!/bin/bash
   ~~~
    git clone https://github.com/H4cKer54N/local_simple_cloud
   ~~~
   
2.Install the dependencies:

~~~
pip install -r requirements.txt
~~~


## Usage

1. Start the FastAPI server:

~~~
uvicorn main:app --host 0.0.0.0 --port 8000
~~~

2. Open your web browser and navigate to http://localhost:8000 to access the application or http://192.168.1.yourlocalip:8000

## Endpoints

GET /: Displays a list of files in the "compartido" directory with their details like name, size, and last modified date. Renders the index.html template.

GET /download/{file_name}: Downloads the specified file from the "compartido" directory.

POST /upload/: Uploads one or more files to the "compartido" directory.

DELETE /delete/{file_name}: Deletes the specified file from the "compartido" directory.


## Contributing

Contributions are welcome! If you encounter any bugs or have suggestions for new features, please follow the guidelines below:

### Bug Reports

If you find a bug in the program, please submit a bug report by opening an issue in the **Bugs** section of the repository. Provide detailed information about the bug, including steps to reproduce it and any relevant error messages or screenshots.

### Feature Requests

If you have an idea for a new feature or an enhancement to existing functionality, please submit a feature request by opening an issue in the **Features** section of the repository. Clearly describe the proposed feature and explain how it would benefit the program.

## License

This project is licensed under the MIT License.


