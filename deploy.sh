oc delete project/zombiestorm
sleep 40
oc new-project zombiestorm
#oc new-app glennswest/zombiestorm:70e7678
#oc expose service/zombiestorm
oc create -f zombiestorm.yaml
#oc expose po/zombiestorm
#oc expose svc/zombiestorm

