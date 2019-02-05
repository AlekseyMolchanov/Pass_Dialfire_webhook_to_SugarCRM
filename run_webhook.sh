# Example export Env
#
# export SUGAR_CRM_URL='http://crm.intra/service/v4_1/rest.php'
# export SUGAR_CRM_USERNAME=''
# export SUGAR_CRM_PASSWORD=''
# export SUGAR_CRM_ASSIGNED_USER_ID='<guid>'
# export no_proxy='crm.intra, 127.0.0.1'
export SUGAR_CRM_HOST='crm.intra:192.168.0.200'

docker build --rm -f "Dockerfile" -t dialfire_webhook:latest .
docker run -it -d --rm -p 8080:8080 -e SUGAR_CRM_URL -e SUGAR_CRM_USERNAME -e SUGAR_CRM_PASSWORD -e SUGAR_CRM_ASSIGNED_USER_ID -e no_proxy --name dialfire_webhook --add-host=$SUGAR_CRM_HOST dialfire_webhook
