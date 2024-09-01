# Python External Data Packaging Example

This is a proof of concept that shows how to include auxiliary/external data in your Python wheels, without having to include that data in your source code directory.
You can have that data in completely separate directories, and it will be installed into specific system directories from where you can access it.

## Instructions for Seeing It in Action

### 1. Download the repository files
The following instructions assume you're inside the repository's main directory, unless noted otherwise.


### 2. Install PDM
On your terminal:

`pip install --upgrade pdm`


### 3. Build the wheel package
On your terminal:

`pdm build`

This should create a file with `.whl` extension in the `dist` subdirectory.


### 4. Install the wheel
On your terminal:

`pip install dist/%YOUR_WHEEL_FILE_NAME%`

where you need to substitute `%YOUR_WHEEL_FILE_NAME%` for the filename of your wheel, which was created in the previous step.


### 5. Go into some other directory for testing
On your terminal:

`cd %SOME_OTHER_DIRECTORY_PATH%`

where you need to substitute `%SOME_OTHER_DIRECTORY_PATH%` for the path of some other directory, to test the installed package.


### 6. Run the package as a script
This is the easiest way to test, but of course you can now import the package into any scripts in your environment.
On your terminal:

`python -m awesome_package.awesome_module`

This should copy the auxiliary data files into your testing directory, and print the outputs of the auxiliary scripts

