# GithubApiCrawler

At First clone the repository from Github and switch to the new directory:

    git clone https://github.com/ahsaan-habib/GithubApiCrawler.git
    cd GithubApiCrawler

## Set Up The Environment

### Step 1: Create a Virtual Environment

A virtual environment is an isolated environment where you can install Python packages without affecting your system-wide Python installation. It's good practice to create one for each project.

Open your terminal and run the following command to create a virtual environment named `venv`:

```bash
python -m venv venv
```

### Step 2: Activate the Virtual Environment

Now that you have created the virtual environment, you need to activate it. Activation sets your terminal session to use the Python interpreter and packages within the virtual environment.

On Windows, use the following command:

```bash
venv\Scripts\activate
```

On macOS and Linux, use:

```bash
source venv/bin/activate
```

You'll notice that your terminal prompt changes to indicate that the virtual environment is active.

### Step 3: Install Project Dependencies

To install the required Python packages for your project, you can use a `requirements.txt` file that lists these dependencies. Ensure that you have a `requirements.txt` file in your project directory, and then run the following command:

```bash
pip install -r requirements.txt
```

This command reads the list of dependencies from `requirements.txt` and installs them within the virtual environment.

### Step 4: Run Your Python Script

Now that you are inside the virtual environment with dependencies installed, you can run your Python script. Navigate to the directory where your Python script (`filename.py`) is located.

Run your Python script using the `python` command:

```bash
python ./GithubAPICrawler.py
```

Your script will execute within the virtual environment, using the Python interpreter and packages installed in that environment.

### Step 5: Deactivate the Virtual Environment (Optional)

When you're done working on your project and want to leave the virtual environment, you can deactivate it. Simply run:

```bash
deactivate
```

Your terminal prompt will return to its normal state, indicating that you have left the virtual environment.

That's it! You've successfully set up a Python project using a virtual environment, installed project dependencies, and executed a Python script.

Happy coding!
