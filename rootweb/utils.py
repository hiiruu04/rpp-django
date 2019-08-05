from random_forest.models_randomForest import RandomForest

def get_pickle():
    pickle = RandomForest.objects.all()
    return pickle