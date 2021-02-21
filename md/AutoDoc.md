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
```
AutoDoc.Equals(obj) -> Boolean
```
- **obj**: Object
### AutoDoc.ExportMKDocs
```
AutoDoc.ExportMKDocs(path) -> Void
```
- **path**: String
### AutoDoc.ExportPythonAPI
```
AutoDoc.ExportPythonAPI(path, pretty) -> Void
```
- **path**: String 
- **pretty**: Boolean True
Export the API to disk. 
See docs for more, lol.
    1-
    2-
    3-

end.
### AutoDoc.GetClasses
```
AutoDoc.GetClasses() -> List`1
```
### AutoDoc.GetHashCode
```
AutoDoc.GetHashCode() -> Int32
```
### AutoDoc.GetMethods
```
AutoDoc.GetMethods(withClass, withNames, withTypes) -> List`1
```
- **withClass**: Boolean False
- **withNames**: Boolean False
- **withTypes**: Boolean False
### AutoDoc.GetProperties
```
AutoDoc.GetProperties(withClass) -> List`1
```
- **withClass**: Boolean False
### AutoDoc.GetPythonAPI
```
AutoDoc.GetPythonAPI() -> List`1
```
Use reflection to generete the Python API List
### AutoDoc.GetType
```
AutoDoc.GetType() -> Type
```
### AutoDoc.HasTag
```
AutoDoc.HasTag(tag, text) -> Boolean
```
- **tag**: String 
- **text**: String
### AutoDoc.ParamType
```
AutoDoc.ParamType(param) -> String
```
- **param**: ParameterInfo
### AutoDoc.ReadClass
```
AutoDoc.ReadClass(type, flags) -> List`1
```
- **type**: Type 
- **flags**: BindingFlags
### AutoDoc.ToString
```
AutoDoc.ToString() -> String
```