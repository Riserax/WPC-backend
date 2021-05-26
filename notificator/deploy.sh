#!/bin/bash
BUCKET_NAME="${BUCKET_NAME:-192426}"
FUNCTION_NAME="${FUNCTION_NAME:-192426__notify}"
## build
rm lambda.zip || true

zip -r lambda.zip ./* \
    --exclude 'lambda.zip' \
    --exclude 'deploy.sh'

## release
aws s3 cp ./lambda.zip s3://${BUCKET_NAME}/code/${FUNCTION_NAME}/lambda.zip

## update code
aws lambda update-function-code --function-name ${FUNCTION_NAME} --s3-bucket ${BUCKET_NAME} --s3-key code/${FUNCTION_NAME}/lambda.zip --publish