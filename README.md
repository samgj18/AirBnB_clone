<img src="https://www.holbertonschool.com/holberton-logo-twitter-card.png">

# Airbnb Clone Console

**Purpose**

The purpose of this project is to recreate the AirBnB site, from the back-end data management to the front-end user interface.

The project is currently in its first phase, where we are creating a command line interpretor to access objects that will store user data. Users can use the console to create objects, update object attributes, remove objects, list all objects, and store and read data from a .json file.

---

In order to begin the console, you can run either 'python3 console.py' or './console.py' in the command line.

Classes that are currently supported include BaseModel, User, City, State, Amenity, Review, and Place.

The console currently supports the following commands:

- **create \<class name>**, which will create an object of the class declared by user;
- **show \<class name> \<id>**, which will display the object information if it exists;
- **destroy \<class name> \<id>**, which will delete the object if it exists;
- **all \<class name>**, where the class name input is optional and the console will display all instances, or all instances of a specified object;
- **update \<class name> \<id> \<attribute name> \<attribute value>**, whilch will update an instance attribute of a previously declared object.

Additionally, the console also supports the following command formats:

- **\<class name>.all()**, which will display all instances of the specified class;
- **\<class name>.count()**, whilch will display the number of instances of the specified class;
- **\<class name>.show(\<id>)**, whilch will display the instance with correct id and class;
- **\<class name>.destroy(\<id>)**, which will delete the instance with correct id and class;
- **\<class name>.update(\<id>, \<attribute name>, \<attribute value>)**, which will update an instance of the given class and id with the new attribute;
- **\<class name>.update(\<id>, \<dictionary representation>)**, which will update an instance of the given class and id with a dictionary of key value pairs that will be new attributes for the objects.

### Example Usage

#### Interactive Mode

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
(hbnb)
(hbnb) quit
$
```

```
$ ./console.py
(hbnb) create BaseModel
5dccfbf9-03a6-45f7-8a75-80094392bf97
(hbnb) show BaseModel 5dccfbf9-03a6-45f7-8a75-80094392bf97
[BaseModel] (5dccfbf9-03a6-45f7-8a75-80094392bf97) {'id': '5dccfbf9-03a6-45f7-8a75-80094392bf97', 'updated_at': datetime.datetime(2018, 6, 13, 23, 10, 13, 549740), 'created_at': datetime.datetime(2018, 6, 13, 23, 10, 13, 549699)}
(hbnb) all
[[BaseModel] (5dccfbf9-03a6-45f7-8a75-80094392bf97) {'id': '5dccfbf9-03a6-45f7-8a75-80094392bf97', 'updated_at': datetime.datetime(2018, 6, 13, 23, 10, 13, 549740), 'created_at': datetime.datetime(2018, 6, 13, 23, 10, 13, 549699)}]
(hbnb) BaseModel.count
1
(hbnb) update BaseModel 5dccfbf9-03a6-45f7-8a75-80094392bf97 number 89
(hbnb) show BaseModel 5dccfbf9-03a6-45f7-8a75-80094392bf97
[BaseModel] (5dccfbf9-03a6-45f7-8a75-80094392bf97) {'number': '89', 'updated_at': datetime.datetime(2018, 6, 13, 23, 11, 51, 470426), 'created_at': datetime.datetime(2018, 6, 13, 23, 10, 13, 549699), 'id': '5dccfbf9-03a6-45f7-8a75-80094392bf97'}
(hbnb) create User
71e19890-6440-4ca9-9976-59ba61571f09
(hbnb) all
[[User] (71e19890-6440-4ca9-9976-59ba61571f09) {'id': '71e19890-6440-4ca9-9976-59ba61571f09', 'updated_at': datetime.datetime(2018, 6, 13, 23, 12, 39, 71568), 'created_at': datetime.datetime(2018, 6, 13, 23, 12, 39, 71532)}, [BaseModel] (5dccfbf9-03a6-45f7-8a75-80094392bf97) {'number': '89', 'updated_at': datetime.datetime(2018, 6, 13, 23, 11, 51, 470426), 'created_at': datetime.datetime(2018, 6, 13, 23, 10, 13, 549699), 'id': '5dccfbf9-03a6-45f7-8a75-80094392bf97'}]
(hbnb) destroy User 71e19890-6440-4ca9-9976-59ba61571f09
(hbnb) all
[[BaseModel] (5dccfbf9-03a6-45f7-8a75-80094392bf97) {'number': '89', 'updated_at': datetime.datetime(2018, 6, 13, 23, 11, 51, 470426), 'created_at': datetime.datetime(2018, 6, 13, 23, 10, 13, 549699), 'id': '5dccfbf9-03a6-45f7-8a75-80094392bf97'}]
(hbnb) destroy BaseModel 5dccfbf9-03a6-45f7-8a75-80094392bf97
(hbnb) all
[]
(hbnb) quit
$
```

---

**Authors**

- **Jhoan Rodríguez**, https://github.com/JhoanRodriguez
- **Samuel Gómez**, https://github.com/samgj18
