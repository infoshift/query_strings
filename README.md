Query Strings
=============

A quick guide on query strings.

## Setting a Value to a Key
To set a value to a specific key in the query string,
/resource?key=value

```python
key = request.args.get('key')
```

## Setting a List Value to a Key
Set a list of values to a specific key in the query
string. You can retrieve this using a specific. 
/resource?list[]=1&list[]=2

```python
list_ = request.args.getlist('list[]')
```

## Setting a Boolean Value to a Key
Set a boolean value to a specific key in the query
string.
/resource?boolean

```python
boolean = 'boolean' in request.args
```
