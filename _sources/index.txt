.. NSLS-II arch documentation master file, created by
   sphinx-quickstart on Sun Jan 18 10:00:09 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Data Muxer
----------

Data Muxer is a tool for interleaving ("muxing") separate streams of data
based on time. For example, readings taking asynchronously must be aligned --
that is, assigned common bins in time -- before they can be plotted against
each other.

API reference
=============

.. currentmodule:: datamuxer

DataMuxer
+++++++++

.. autosummary::
   :toctree: generated/

   DataMuxer
   DataMuxer.bin_by_edges
   DataMuxer.bin_on
   DataMuxer.from_events
   DataMuxer.to_sparse_dataframe


.. autosummary::
   :toctree: generated/

   ColSpec

Helpers
+++++++

.. autosummary::
   :toctree: generated/

   dataframe_to_dict

Exceptions
++++++++++

.. autosummary::
   :toctree: generated/

   BinningError
   BadDownsamplerError
