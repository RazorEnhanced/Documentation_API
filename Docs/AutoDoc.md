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
          

## Properties  
 
## Methods  
### AutoDoc.Equals
```py
AutoDoc.Equals(Object obj)
- Object **obj** ____```
### AutoDoc.ExportMKDocs
```py
AutoDoc.ExportMKDocs(String path)
- String **path** ____```
### AutoDoc.ExportPythonAPI
```py
AutoDoc.ExportPythonAPI(String path, Boolean pretty)
- String **path** ____
- Boolean **pretty** __True__```
Export the API to disk. 
See docs for more, lol.
    1-
    2-
    3-

end.
### AutoDoc.GetClasses
```py
AutoDoc.GetClasses()```
### AutoDoc.GetHashCode
```py
AutoDoc.GetHashCode()```
### AutoDoc.GetMethods
```py
AutoDoc.GetMethods(Boolean withClass, Boolean withNames, Boolean withTypes)
- Boolean **withClass** __False__
- Boolean **withNames** __False__
- Boolean **withTypes** __False__```
### AutoDoc.GetProperties
```py
AutoDoc.GetProperties(Boolean withClass)
- Boolean **withClass** __False__```
### AutoDoc.GetPythonAPI
```py
AutoDoc.GetPythonAPI()```
Use reflection to generete the Python API List
### AutoDoc.GetType
```py
AutoDoc.GetType()```
### AutoDoc.HasTag
```py
AutoDoc.HasTag(String tag, String text)
- String **tag** ____
- String **text** ____```
### AutoDoc.ParamType
```py
AutoDoc.ParamType(ParameterInfo param)
- ParameterInfo **param** ____```
### AutoDoc.ReadClass
```py
AutoDoc.ReadClass(Type type, BindingFlags flags)
- Type **type** ____
- BindingFlags **flags** ____```
### AutoDoc.ToString
```py
AutoDoc.ToString()```