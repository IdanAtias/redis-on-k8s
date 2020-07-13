#!/bin/bash

[[ -z $1 ]] && {
    echo "no path to deploy dir provided";
    exit 1;
}
[[ ! -d $1 ]] && {
    echo "path to deploy dir is not a valid directory";
    exit 1;
}

PATH_TO_DEPLOY_DIR=$1
OUTPUT_FILE="$PATH_TO_DEPLOY_DIR/k8s-all-in-one-redis.yaml"

touch $OUTPUT_FILE

cat $PATH_TO_DEPLOY_DIR/k8s-configmap-redis-config.yaml >> $OUTPUT_FILE
echo "---" >> $OUTPUT_FILE

cat $PATH_TO_DEPLOY_DIR/k8s-service-redis.yaml >> $OUTPUT_FILE
echo "---" >> $OUTPUT_FILE

cat $PATH_TO_DEPLOY_DIR/k8s-statefulset-redis.yaml >> $OUTPUT_FILE
echo "---" >> $OUTPUT_FILE

cat $PATH_TO_DEPLOY_DIR/k8s-deployment-contour.yaml >> $OUTPUT_FILE
echo "---" >> $OUTPUT_FILE

echo "done"

exit 0

