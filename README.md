# AWS Slack Invite

This project is for creating a simple, static website for inviting users to a Slack Team Chat. It is completely hosted
within AWS and (depending on your load) should be completely free to host.

## How to use
This project is composed of two core components - the S3 static website code and the Lambda function "serverside"/ code (for sending invitations to emails).

## Cookiecutter

To begin, install `cookiecutter`, and create your project. Run:

    $ pip install cookiecutter
    $ cookiecutter gh:cmeadows/aws-slack-invite
    slack_domain []: <this is your domain found at yourdomain.slack.com>
    slack_oauth_token []: <slack oauth token (https://api.slack.com/docs/oauth)>
    api_gateway_url []: <your deployed API Gateway URL>

## Deployment

##### Static Website on S3
1. (Optional) Replace the `s3/static/background.jpg` with your background image
2. Upload the contents of the `s3` directory to an S3 bucket.
3. Follow instructions [here](http://docs.aws.amazon.com/gettingstarted/latest/swh/website-hosting-intro.html) on how to setup a static website on S3.
4. (Optional) You can setup a CloudFront distribution for the static content.

##### AWS Lambda
1. Create an AWS Lambda function.
2. Copy `lambda/lambda_function.py` code into AWS Lambda code editor.

##### API Gateway
1. Create an AWS API Gateway API by uploading the provided `api-gateway/swagger.yaml` file in the console.

## Similar Projects
* https://github.com/rauchg/slackin
* https://github.com/acemod/slackin-python
* https://github.com/acemod/aws-slackin
