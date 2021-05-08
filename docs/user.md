# User Directions

## Starting the flask deployment pod

```
kubectl get pods -o wide
```
This should show you all pods running from previous deployment. From this list choose pod labeled savsmith-final-flask-deployment (there will be varrying endings to this pod name). For example: 

```
savsmith-final-flask-deployment-6dcc4f7bdc-tt9wh
```

To exec into this flask deployment we would follow: 
```
kubectl exec -it savsmith-final-flask-deployment-6dcc4f7bdc-tt9wh -- /bin/bash
```

## /jobs Route

```
root@savsmith-final-flask-deployment-6dcc4f7bdc-tt9wh:/app# curl 10.244.15.179:5000/jobs
```

## /generate Route
This route will allow the user to add new data possibly referencing a different area other than the four already presented (Austin, Greater Austin Area, Texas, The United States)

```
root@savsmith-final-flask-deployment-6dcc4f7bdc-tt9wh:/app# curl 10.244.15.179:5000/generate
```
Would prompt the user to fill in the six categories of data known about the employment/unemployment of the Area they are describing. Once data is inserted the program will return:

```
Data point has been created
```

## /query Route

This route will allow the user to find data of a specific year and area

```
root@savsmith-final-flask-deployment-6dcc4f7bdc-tt9wh:/app# curl 10.244.15.179:5000/query/2020/Austin
```
Would return:
```
Data in range {"Year": 2020, "Area": "Austin", "Employment": 556570, "Civilian Labor Force": 592927, "Unemployment": 36357, "Unemployment Rate": 0.061}
```
## /update Route

This route will allow the user to update and change any existing data. The data is identified by its year and area. 

```
root@savsmith-final-flask-deployment-6dcc4f7bdc-tt9wh:/app# curl 10.244.15.179:5000/update/2020/Austin
```
Will allow the user to update all/any of the six categories of data known for Austin employment in 2020. And would then return:

```
Updated data #followed by the data point the user just updated
```
However if the data point the user was trying to update did not exist it will return: 

```
Data point does not exist, add new entry instead
```

## /delete Route

This route will allow the user to delete a data point if it was unintentionally added or if they do not want to see certain data. 

```
root@savsmith-final-flask-deployment-6dcc4f7bdc-tt9wh:/app# curl 10.244.15.179:5000/delete/2020/Austin
```
Would return:

```
Data points have been deleted
```
