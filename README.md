**************************************
Hands on deploying Redis in Kubernetes
**************************************

Create raw Kubernetes cluster on GKE
####################################

  * ``gcloud beta container --project "redis-on-k8s" clusters create "redis-cluster" --zone "us-west1-a" --no-enable-basic-auth --release-channel "regular" --machine-type "n1-standard-1" --image-type "COS" --disk-type "pd-standard" --disk-size "30" --metadata disable-legacy-endpoints=true --scopes "https://www.googleapis.com/auth/devstorage.read_only","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring","https://www.googleapis.com/auth/servicecontrol","https://www.googleapis.com/auth/service.management.readonly","https://www.googleapis.com/auth/trace.append" --preemptible --num-nodes "3" --enable-stackdriver-kubernetes --enable-ip-alias --network "projects/redis-on-k8s/global/networks/default" --subnetwork "projects/redis-on-k8s/regions/us-west1/subnetworks/default" --default-max-pods-per-node "110" --no-enable-master-authorized-networks --addons HorizontalPodAutoscaling,HttpLoadBalancing --enable-autoupgrade --enable-autorepair --max-surge-upgrade 1 --max-unavailable-upgrade 0``

Introduce our cluster to kubectl (create new kubeconfig entry)
##############################################################

  * ``gcloud container clusters get-credentials redis-cluster``

      .. note
  
      This also sets your kubectl default context

Deploy Redis to our GKE cluster
###############################

  * ``kubectl apply -f deploy/k8s-all-in-one-redis.yaml``


Cleanup
#######

  * ``gcloud container clusters delete redis-cluster``

