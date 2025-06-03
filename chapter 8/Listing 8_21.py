#Listing 8_21 : mutation string 
mutation_string = '''
    mutation {
        createBook(title: "Numerical Python", author: "Johansan", price: 4000, publisher:"Springer") {
            book {
                title
                author
                price
                publisher
            }
        }
    }
'''


result = schema.execute(mutation_string)
