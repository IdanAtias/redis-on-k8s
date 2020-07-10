#!/bin/sh
# you should have an ENV var CLUSTER_CTX with your cluster context
exec kubectl --context=$CLUSTER_CTX "$@"
