#Listing 5_21: Atlas cluster configuration
DATABASES = {
     'default': {
        'ENGINE': 'djongo',
        "CLIENT": {
            'name': 'djongodb',
            'host' : 
'mongodb+srv://username:password@cluster0.oh20x8g.mongodb.net/?retryWrites=true&w=majority ',                              
            'username': '<username>',
            'password' : '<password>'
        }
    }
 }
