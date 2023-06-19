# Furry Crossroads API Wrapper
Welcome to the Furry Crossroads API Wrapper! This is the official Python package developed to provide streamlined access to the backend features of the Furry Crossroads community. With this wrapper, you can seamlessly check your account data and perform other automation tasks within the Furry Crossroads community.

## Installation
Please note, this package is not available on the Python Package Index (PyPi). Hence, installation will need to be done directly from this GitHub repository using pip. Follow the instructions below:

```bash
pip install git+https://github.com/Furry-Crossroads/FCPy.git
```

## Setting Up a Virtual Environment
Before using this package, it's recommended to set up a Python virtual environment. This helps to isolate the project and avoid potential conflicts between dependencies. Additionally, this package authorizes through environment variables. This will increase security for you when developing your own applications, and is a requirement as such. 

### Windows
If you're using Windows (and installed py-launcher at setup), you can create a virtual environment with the following command:

```cmd
py -m venv env
```

Once your virtual environment is set up, you need to activate it. Use the following command in Windows:

```cmd
.\env\Scripts\activate
```

Finally, you can install the requirements:
```cmd
py -m pip install -r requirements.txt
```

### Linux/MacOS
If you're using a Linux-based system or MacOS, then follow these commands:

```bash
python3 -m venv env
source env/bin/activate
python3 -m pip install -r requirements.txt
```

## Loading Environment Variables
This package utilizes environment variables to load sensitive information into the API. You will need to modify the activate script in your virtual environment accordingly.

In Windows, add the necessary environment variables to the env\Scripts\activate.bat file:

```cmd
set "API_KEY=your-api-key"
set "OTHER_VARIABLE=your-value"
```
In Linux/MacOS, add the necessary environment variables to the env/bin/activate file:

```bash
export API_KEY=your-api-key
export OTHER_VARIABLE=your-value
```
Please replace your-api-key and your-value with your actual values. These settings typically won't persist between activations of your virtual environment. To resolve this, you can opt to modify the `activate` file in the virtual environment. However, this poses a greater security risk due to storing your sensative information as plain text. Simply take the commands above and append them at the beggining of your `activate` file.

## License
This project is licensed under the terms of the MIT License.

## Contact
If you encounter any issues or have suggestions for improvements, feel free to open an issue on this repository.

For direct queries, please contact me at:

Discord: Furry Crossroads Official (Discord)[https://discord.com/invite/ryydwvjtj2].

Email: voxlight@furrycrossroads.com

Furry Crossroads Username: your-username

Remember to always respect the terms of service and community rules when using this API wrapper. Enjoy your journey across the Furry Crossroads!