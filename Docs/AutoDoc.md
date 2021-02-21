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
``` python
AutoDoc.Equals(Object obj)
  Object obj #
```
### AutoDoc.ExportMKDocs
``` python
AutoDoc.ExportMKDocs(String path)
  String path #
```
### AutoDoc.ExportPythonAPI
``` python
AutoDoc.ExportPythonAPI(String path, Boolean pretty)
  String path #
  Boolean pretty #True
```
Export the API to disk. 
See docs for more, lol.
    1-
    2-
    3-

end.
### AutoDoc.GetClasses
``` python
AutoDoc.GetClasses()

```
### AutoDoc.GetHashCode
``` python
AutoDoc.GetHashCode()

```
### AutoDoc.GetMethods
``` python
AutoDoc.GetMethods(Boolean withClass, Boolean withNames, Boolean withTypes)
  Boolean withClass #False
  Boolean withNames #False
  Boolean withTypes #False
```
### AutoDoc.GetProperties
``` python
AutoDoc.GetProperties(Boolean withClass)
  Boolean withClass #False
```
### AutoDoc.GetPythonAPI
``` python
AutoDoc.GetPythonAPI()

```
Use reflection to generete the Python API List
### AutoDoc.GetType
``` python
AutoDoc.GetType()

```
### AutoDoc.HasTag
``` python
AutoDoc.HasTag(String tag, String text)
  String tag #
  String text #
```
### AutoDoc.ParamType
``` python
AutoDoc.ParamType(ParameterInfo param)
  ParameterInfo param #
```
### AutoDoc.ReadClass
``` python
AutoDoc.ReadClass(Type type, BindingFlags flags)
  Type type #
  BindingFlags flags #
```
### AutoDoc.ToString
``` python
AutoDoc.ToString()

```