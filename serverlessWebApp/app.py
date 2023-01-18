#!/usr/bin/env python3

import aws_cdk as cdk

from serverless_web_app.serverless_web_app_stack import ServerlessWebAppStack


app = cdk.App()
ServerlessWebAppStack(app, "serverless-web-app")

app.synth()
