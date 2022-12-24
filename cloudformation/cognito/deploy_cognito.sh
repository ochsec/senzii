aws cloudformation deploy \
--template-file userpool.yaml \
--stack-name senzii-cognito-userpool \
--profile $1 \
--region $2 \
--parameter-overrides $(cat userpool.parameters | tr '\n' ' ')