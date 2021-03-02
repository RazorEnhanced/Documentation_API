:mod:`Mobiles`
========================================
.. py:module:: Mobiles



Methods
--------------

.. py:function:: Mobiles.ApplyFilter(filter) -> List[Mobile]


* filter: :mod:`Mobiles.Filter` 




.. py:function:: Mobiles.ContextExist(serial, name) -> Int32


* serial: :mod:`Int32` 
* name: :mod:`String` 




.. py:function:: Mobiles.ContextExist(mob, name) -> Int32


* mob: :mod:`Mobile` 
* name: :mod:`String` 




.. py:function:: Mobiles.FindBySerial(serial) -> Mobile


* serial: :mod:`Int32` 




.. py:function:: Mobiles.GetPropStringByIndex(mob, index) -> String


* mob: :mod:`Mobile` 
* index: :mod:`Int32` 




.. py:function:: Mobiles.GetPropStringByIndex(serial, index) -> String


* serial: :mod:`Int32` 
* index: :mod:`Int32` 




.. py:function:: Mobiles.GetPropStringList(mob) -> List[String]


* mob: :mod:`Mobile` 




.. py:function:: Mobiles.GetPropStringList(serial) -> List[String]


* serial: :mod:`Int32` 




.. py:function:: Mobiles.GetPropValue(mob, name) -> Single


* mob: :mod:`Mobile` 
* name: :mod:`String` 




.. py:function:: Mobiles.GetPropValue(serial, name) -> Single


* serial: :mod:`Int32` 
* name: :mod:`String` 




.. py:function:: Mobiles.GetTrackingInfo() -> Mobiles.LastTrackingInfo







.. py:function:: Mobiles.Message(mobile, hue, message, wait) -> Void


* mobile: :mod:`Mobile` 
* hue: :mod:`Int32` 
* message: :mod:`String` 
* wait: :mod:`Boolean` 




.. py:function:: Mobiles.Message(serial, hue, message, wait) -> Void


* serial: :mod:`Int32` 
* hue: :mod:`Int32` 
* message: :mod:`String` 
* wait: :mod:`Boolean` 




.. py:function:: Mobiles.Select(mobiles, selector) -> Mobile


* mobiles: :mod:`List[Mobile]` 
* selector: :mod:`String` 




.. py:function:: Mobiles.SingleClick(mobileserial) -> Void


* mobileserial: :mod:`Int32` 




.. py:function:: Mobiles.SingleClick(mobile) -> Void


* mobile: :mod:`Mobile` 




.. py:function:: Mobiles.UseMobile(mobileserial) -> Void


* mobileserial: :mod:`Int32` 




.. py:function:: Mobiles.UseMobile(mobile) -> Void


* mobile: :mod:`Mobile` 




.. py:function:: Mobiles.WaitForProps(mobileserial, delay) -> Void


* mobileserial: :mod:`Int32` 
* delay: :mod:`Int32` 




.. py:function:: Mobiles.WaitForProps(m, delay) -> Void


* m: :mod:`Mobile` 
* delay: :mod:`Int32` 




.. py:function:: Mobiles.WaitForStats(m, delay) -> Void


* m: :mod:`Mobile` 
* delay: :mod:`Int32` 




.. py:function:: Mobiles.WaitForStats(mobileserial, delay) -> Void


* mobileserial: :mod:`Int32` 
* delay: :mod:`Int32` 



