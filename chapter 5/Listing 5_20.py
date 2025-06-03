#Listing 5_20: DATABASE configuration for Djongo 
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'djongodb',
        'CLIENT': {
           'host': 'mongodb://localhost:27017',
        }
    }
