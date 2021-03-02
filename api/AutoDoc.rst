:mod:`AutoDoc`
========================================
.. py:module:: AutoDoc
   :synopsis: 
            <summary>
            Automatically generate the full list of RE Python API using Reflection.
            The API is further integrated with the data coming from standard C#  comments.
            </summary>
        



Methods
--------------

.. py:function:: AutoDoc.Equals(obj) -> Boolean


* obj: :mod:`Object` 




.. py:function:: AutoDoc.GetClasses() -> List[String]







.. py:function:: AutoDoc.GetMethods(withClass, withNames, withTypes) -> List[String]


* withClass: :mod:`Boolean` 
* withNames: :mod:`Boolean` 
* withTypes: :mod:`Boolean` 




.. py:function:: AutoDoc.GetMethodSignature(method, withClass, withNames, withTypes) -> String


* method: :mod:`DocMethod` 
* withClass: :mod:`Boolean` 
* withNames: :mod:`Boolean` 
* withTypes: :mod:`Boolean` 




.. py:function:: AutoDoc.GetProperties(withClass) -> List[String]


* withClass: :mod:`Boolean` 




.. py:function:: AutoDoc.GetPythonAPI() -> DocContainer





Use reflection to generete the Python API List

.. py:function:: AutoDoc.HasTag(tag, text) -> Boolean


* tag: :mod:`String` 
* text: :mod:`String` 




.. py:function:: AutoDoc.ReadClass(type, flags) -> DocContainer


* type: :mod:`Type` 
* flags: :mod:`BindingFlags` 




.. py:function:: AutoDoc.ResolveType(param) -> String


* param: :mod:`Type` 



