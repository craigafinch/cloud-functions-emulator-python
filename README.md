# cloud-functions-emulator-python
The Google Cloud Functions emulator for Python 3 helps you develop Google Cloud
Functions using Python running locally on your workstation. Working locally is much
faster than deploying code to Google, waiting for it to finish deploying, getting
an error, and finding the error message in the the Stackdriver logs.

# Installation
Clone the repo and change to the directory. Run the following:

```bash
source env/bin/activate
pip install -r requirements.txt
```

# Running the Framework

Copy `env.sh.dist` to `env.sh` and edit the file to define any environment variables
that your function will need in this file. This is equivalent to
[setting environment variables](https://cloud.google.com/functions/docs/env-var)
in the GCP Console or using the command:

```bash
gcloud functions deploy FUNCTION_NAME --set-env-vars FOO=bar
```

Once `env.sh` is configured, run the emulator:


```
source env.sh
flask run
```

To trigger the function, navigate to http://127.0.0.1:5000/route1 in a browser or with
a client such as curl, ARC, or Postman.

Because we set `FLASK_ENV=development`, Flask will watch for changes to your code, and
reload automatically. Error messages are displayed in the terminal and in the
browser.

# Developing Custom Functions
Define your trigger URLs as routes in `framework.py`. That's the only change you
should have to make in this file.

Define your functions in another file (module ), and import them into `framework.py`
There is an example function in file `main.py` (there is nothing magic about
the name `main.py`)

# Support

This software is released without any warranty or promise of support, with the goal
of helping other Python developers make use of Google Cloud Functions. If you are
looking for commercial support, please contact root@rootwork.it or visit
https://rootwork.it/contact-rootwork/


# Copyrights and Trademarks

I am neither an employee nor contractor of Google, and I have no affiliation with
Google Cloud Platform. All copyrights and trademarks mentioned in the source code
and documentation are the property of Google, and are used here under the doctrine
of "fair use."

The official, Google-supported Cloud Functions Emulator only supports Node.js,
and can be found here: https://github.com/GoogleCloudPlatform/cloud-functions-emulator
