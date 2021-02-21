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
Equals(Object obj) -> Boolean
```
- __Object__ **obj**
### AutoDoc.ExportMKDocs
```
ExportMKDocs(String path) -> Void
```
- __String__ **path**
### AutoDoc.ExportPythonAPI
```
ExportPythonAPI(String path, Boolean pretty) -> Void
```
- __String__ **path** 
- __Boolean__ **pretty** True
Export the API to disk. 
See docs for more, lol.
    1-
    2-
    3-

end.
### AutoDoc.GetClasses
```
GetClasses() -> List`1
```
### AutoDoc.GetHashCode
```
GetHashCode() -> Int32
```
### AutoDoc.GetMethods
```
GetMethods(Boolean withClass, Boolean withNames, Boolean withTypes) -> List`1
```
- __Boolean__ **withClass** False
- __Boolean__ **withNames** False
- __Boolean__ **withTypes** False
### AutoDoc.GetProperties
```
GetProperties(Boolean withClass) -> List`1
```
- __Boolean__ **withClass** False
### AutoDoc.GetPythonAPI
```
GetPythonAPI() -> List`1
```
Use reflection to generete the Python API List
### AutoDoc.GetType
```
GetType() -> Type
```
### AutoDoc.HasTag
```
HasTag(String tag, String text) -> Boolean
```
- __String__ **tag** 
- __String__ **text**
### AutoDoc.ParamType
```
ParamType(ParameterInfo param) -> String
```
- __ParameterInfo__ **param**
### AutoDoc.ReadClass
```
ReadClass(Type type, BindingFlags flags) -> List`1
```
- __Type__ **type** 
- __BindingFlags__ **flags**
### AutoDoc.ToString
```
ToString() -> String
```