# AutoDoc  
            <summary>
            Automatically generate the Python API
            DOING:
            0a. Read Reflection
            0b. Read Comments 
            0c. Produce a JSON-compatible object.
            TODO:
            1. Autocomplete/SyntaxHighlight for script editor
            2. Wiki Documentation
            3. razor.py 
            </summary>
          

### Properties  
 
### Methods  
## AutoDoc.Equals
```python
AutoDoc.Equals(Object obj)
- Object **obj** ____```
## AutoDoc.ExportMKDocs
```python
AutoDoc.ExportMKDocs(String path)
- String **path** ____```
## AutoDoc.ExportPythonAPI
```python
AutoDoc.ExportPythonAPI(String path, Boolean pretty)
- String **path** ____
- Boolean **pretty** __True__```
Export the API to disk. 
See docs for more, lol.
    1-
    2-
    3-

end.
## AutoDoc.GetClasses
```python
AutoDoc.GetClasses()```
## AutoDoc.GetHashCode
```python
AutoDoc.GetHashCode()```
## AutoDoc.GetMethods
```python
AutoDoc.GetMethods(Boolean withClass, Boolean withNames, Boolean withTypes)
- Boolean **withClass** __False__
- Boolean **withNames** __False__
- Boolean **withTypes** __False__```
## AutoDoc.GetProperties
```python
AutoDoc.GetProperties(Boolean withClass)
- Boolean **withClass** __False__```
## AutoDoc.GetPythonAPI
```python
AutoDoc.GetPythonAPI()```
Use reflection to generete the Python API List
## AutoDoc.GetType
```python
AutoDoc.GetType()```
## AutoDoc.HasTag
```python
AutoDoc.HasTag(String tag, String text)
- String **tag** ____
- String **text** ____```
## AutoDoc.ParamType
```python
AutoDoc.ParamType(ParameterInfo param)
- ParameterInfo **param** ____```
## AutoDoc.ReadClass
```python
AutoDoc.ReadClass(Type type, BindingFlags flags)
- Type **type** ____
- BindingFlags **flags** ____```
## AutoDoc.ToString
```python
AutoDoc.ToString()```