print('type \'add\' to add a movie')
print('type \'list\' to list all movies')
print('type \'search\' to add a movie')
print('type \'exit\' to close application')

movie_collection = []

selection = input()
while selection.lower() != 'exit':
    if selection.lower() == 'add':
        movie_var = input('Insert movie name: ')
        director_var = input('Insert director name: ')
        year_var = input('Insert movie year: ')

        movie_collection.append({'movie': movie_var, 'director': director_var, 'year': year_var })

    elif selection.lower() == 'list':
        print(movie_collection)
    elif selection.lower() == 'search':


        search_property = ''
        for v in movie_collection[0].keys():
            yes_or_no = input(f'Do you wanna search by property {v}, type \'yes\' or \'no\'')
            if yes_or_no.lower() == 'yes':
                search_property = v
                break

        if search_property == '':
            print('Can\'t search since no property was selected.')
        else:
            property_value = input('Type the property value: ')
            for item in movie_collection:
                if item[search_property].lower() == property_value.lower():
                    print(item)

    else:
        print('Command not valid, please try again.')
    selection = input()