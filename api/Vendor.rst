:mod:`Vendor`
========================================
.. py:module:: Vendor


Properties
----------------
* Vendor.LastBuyList :mod:`List[Item]`

* Vendor.LastVendor :mod:`Mobile`


Methods
--------------

.. py:function:: Vendor.Buy(vendorSerial, itemID, amount) -> Void


* vendorSerial: :mod:`Int32` 
* itemID: :mod:`Int32` 
* amount: :mod:`Int32` 




.. py:function:: Vendor.BuyList(vendorSerial) -> List[Vendor.BuyItem]


* vendorSerial: :mod:`Int32` 




.. py:function:: Vendor.StoreBuyList(p, args) -> Void


* p: :mod:`PacketReader` 
* args: :mod:`PacketHandlerEventArgs` 



