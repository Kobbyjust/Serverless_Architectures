#!/usr/bin/env python3

import aws_cdk as cdk

from survey_collection.survey_collection_stack import SurveyCollectionStack


app = cdk.App()
SurveyCollectionStack(app, "survey-collection")

app.synth()
