:mod:`PathFinding`
========================================
.. py:module:: PathFinding
   :synopsis: 
            <summary>
            This class implements the PathFinding algorithm using A-Star. 
            </summary>
        



Methods
--------------

.. py:function:: PathFinding.GetPath(dst_x, dst_y, ignoremob) -> List[Tile]


* dst_x: :mod:`Int32` Destination X.
* dst_y: :mod:`Int32` Destination Y.
* ignoremob: :mod:`Boolean` Ignores any mobiles with the path calculation.


Compute the path for the given destination and returns a list of Tile (coordinates).

.. py:function:: PathFinding.Go(r) -> Boolean


* r: :mod:`PathFinding.Route` A customized Route object.


Check if a destination is reachable.

.. py:function:: PathFinding.RunPath(path, timeout, debugMessage, useResync) -> Boolean


* path: :mod:`List[Tile]` 
* timeout: :mod:`Single` 
* debugMessage: :mod:`Boolean` 
* useResync: :mod:`Boolean` 




.. py:function:: PathFinding.Tile(x, y) -> Tile


* x: :mod:`Int32` X coordinate
* y: :mod:`Int32` Y coordinate


Create a Tile starting from X,Y coordinates (see PathFindig.RunPath)
