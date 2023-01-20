
# Welcome to serverlessWebApp CDK Python project!

You should explore the contents of this project. It demonstrates a CDK app with an instance of a stack (`serverless_web_app_stack`)
This project consists of
1. AWS Amplify: for hosting the frontend application
2. API Gateway: which sends a POST request to a lambda function
3. Lambda: For Processing (Inserting data into a database)
4. DynamoDB: A NoSql database

# Key things to note before running this project
 Upon running this app stack all the resources for this architecture will be deploy
 
 ---Note:
    1. For this particular project we will be hosting our frontend(index.html) directly on AWS Amplify without connecting to a source repo(Github, CodeCommit). Update the API Gateway in the index.html file

    2. Also do well to update the right database name in the lambda function


The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization process also creates
a virtualenv within this project, stored under the .venv directory.  To create the virtualenv
it assumes that there is a `python3` executable in your path with access to the `venv` package.
If for any reason the automatic creation of the virtualenv fails, you can create the virtualenv
manually once the init process completes.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

You can now begin exploring the source code, contained in the hello directory.
There is also a very trivial test included that can be run like this:

```
$ pytest
```

To add additional dependencies, for example other CDK libraries, just add to
your requirements.txt file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
