:mod:`Vendor`
========================================
.. py:module:: Vendor
   :synopsis: 
            <summary>
            @nodoc
            @experimental
            The Vendor class allow you to read the list items purchased last.
            </summary>
        



Methods
--------------

.. py:function:: Vendor.BuyList(vendorSerial) -> List[Vendor.BuyItem]


* vendorSerial: :mod:`Int32` Serial of the Vendor (default: -1 - most recent trade)


Get the list of items purchased in the last trade, with a specific Vendor.
