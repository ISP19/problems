## Django Fixtures

# Question
what is Fixtures

# Answer
Fixtures is a collection of data in file type .json .yaml .xml django know how to turn them into database.

# Question
What is database?

# Answer
Database is an organized collection of data they use for provide facilities of searching specific record in given data.

# Question
How to make a database?

# Answer
**specific APP**
```
python manage.py dumpdata app > db.json
```
**specific table**
```
python manage.py dumpdata app.user > db.json
```

**Note1:** For other dumpdata commands<br />
` -e ` for exclude table you don't want to dump<br />
` --indent=<number> ` for a number indentation spaces
` --format ` for format a database type (.json .yaml .xml)

**Note2:** When you backup all database, it will backup all the database tables<br />

If you use this database dump to load the fresh database(in another django project), it can be causes IntegrityError<br />

To fix this problem, make sure to backup the database by excluding contenttypes and auth.permissions tables<br />

``` 
python manage.py dumpdata -exclude auth.permission --exclude contenttypes > db.json
```

# Question
How to load a database

# Answer
```
python manage.py loaddata app
```

# References
[Coderwall](https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata)