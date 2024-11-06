# J-DeepLearning-image-app-with-mlflow-DVC

## workflow
1. the first file we need to change is our config file, then we go 
2. secrets.yaml config file[used for secret database or credential you do not want to share with others], 
3. update params.yaml, it related to all the parameters for my project
4. Update the entity
5. Update the configuration manager in src config[update the configure.py in src folde]
6. Update the components: data ingesting, model preparation, model training, model evalution
7. Update the pipeline: training and prediction pipeline
8. Update the main.py [ to executed pipelines]
9. Update the dvc.yaml [lasly update DVC because inorder to use DVC, we first need to complete all the pipelines]
