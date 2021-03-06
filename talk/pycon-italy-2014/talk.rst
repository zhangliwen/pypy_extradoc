.. include:: beamerdefs.txt

================================
PyPy Status
================================

About me
---------

- PyPy core dev

- ``pdb++``, ``fancycompleter``, ...

- Consultant, trainer

- http://antocuni.eu


PyPy is not dead
----------------

- No PyPy status talk at EuroPython 2013

  * for the first time since 2004!

  * for no good reason :)

- PyPy is healthy and alive

|pause|

- WARNING: This talk is boring

  * "it just works"

What is PyPy?
--------------

* RPython toolchain

  - subset of Python

  - ideal for writing VMs

  - JIT & GC for free

* Python interpreter

  - written in RPython

  - **FAST**

* Whatever (dynamic) language you want

  - smalltalk, prolog, PHP, javascript, ...


PyPy: past two years (1)
-----------------------------

- PyPy 2.0 (May 2013)

  * beta ARM, CFFI, unicode performance

  * stackless + JIT (eventlet, gevent, ...)

|pause|

- PyPy 2.1 (July 2013)

  * stable ARM

  * py3k (3.2.3), numpy, general improvements, bugfixes

|pause|

- PyPy 2.2 (November 2013)

  * incremental GC, faster JSON

  * more JIT, more py3k

  * more numpy, numpy C API


PyPy: past two years (2)
-------------------------

- PyPy 2.3 (May 2014)

- Lot of internal refactoring

- C API for embedding

  * pypy + uWSGI (thanks to Roberto De Ioris)

- the usual, boring, general improvements


More PyPy-powered languages
----------------------------

- RPython: general framework for dynamic languages

- Topaz: implementing Ruby

  * most of the language implemented

  * "definitely faster than MRI"

  * https://github.com/topazproject/topaz

- HippyVM: implementing PHP

  * ~7x faster than standard PHP

  * http://hippyvm.com/



Fundraising campaign
---------------------

- py3k: 50'852 $ of 105'000 $ (48.4%)

- numpy: 48'121 $ of 60'000 $ (80.2%)

- STM, 1st call: 25'000 $

- STM, 2nd call: 2'097 $ of 80'000 $ (2.6%)

  * more on STM later

- thank to all donors!

Current status
---------------

- Python code: "it just works"

- C code: better than ever!

  * cpyext: more complete, but still slow

  * CFFI: the future

  * Native PyPy C API for embedding

  * cppyy for C++

- Lots of CFFI modules around:

  * pygame_cffi, psycopg2_cffi, lxml

- numpy: in-progress (more later)


Speed: 6.3x faster than CPython
--------------------------------

.. image:: speed.png
   :scale: 47%


ARM
----

- Official support since PyPy 2.1

- "it just works"

- ~7.5x faster than CPython on ARM

- thanks to Raspberry-Pi foundation

- distributed as part of Raspbian OS


numpy
-----

- as usual, in-progress

- ~80% of numpy implemented

  * 2336 passing tests out of 3265

  * http://buildbot.pypy.org/numpy-status/latest.html

- just try it

- no scipy :-/


py3k
----

- 3.2: stable

- 3.3: branch started, in-progress

- some missing optimizations

  * getting better


CFFI
-----

- Python <-> C interfacing done right

  * existing shared libraries

  * custom C code

- Inspired by LuaJIT's FFI

- Alternative to C-API, ctypes, Cython, etc.

- Fast on CPython, super-fast on PyPy


cppyy
------

- Interface to C++

- Based on reflection, no need to write wrappers

- PyPy-only, similar to PyCintex for CPython

- Main use case: ROOT

  * http://root.cern.ch

  * "a set of OO frameworks with all the functionality needed to handle and
    analyze large amounts of data in a very efficient way"

- 3x faster than CPython


The future: STM
----------------

- Software Transactional Memory

- Strategy to solve race conditions

- "Finger crossed", rollback in case of conflicts

- On-going research project

  * by Armin Rigo and Remi Meier

STM semantics
-------------

- N threads

- Each thread split into atomic blocks

- Sequential execution in some arbitrary order

- In practice:

- Parallel execution, conflicts solved by STM


Unit of execution (1)
---------------------

- Atomic blocks == 1 Python bytecode

- Threads are executed in arbitrary order, but bytecodes are atomic

- ==> Same semantics as GIL

- "and this will solve the GIL problem" (A. Rigo, EuroPython 2011 lighting talk)

Unit of execution (2)
----------------------

- Larger atomic blocks

- ``with atomic:``

- Much easier to use than explicit locks

- Can be hidden by libraries to provide even higher level paradigms

  * e.g.: Twisted apps made parallel out of the box

Race conditions
---------------

- They don't magically disappear

- With explicit locks

  * ==> BOOM

  * you fix bugs by preventing race conditions

- With atomic blocks

  * ==> Rollaback

  * Performance penalty

  * You optimize by preventing race conditions

- Fast&broken vs. Slower&correct


Implementation
---------------

- Conflicts detection, commit and rollaback is costly

- Original goal (2011): 2x-5x slower than PyPy without STM

  * But parallelizable!

|pause|

- Current goal (2014): 25% slower than PyPy without STM

- Yes, that's 10x less overhead than original goal

- mmap black magic

Current status
---------------

- Preliminary versions of pypy-jit-stm available

- The JIT overhead is still a bit too high

- Lots of polishing needed


Contacts, Q&A
--------------

- http://pypy.org

- http://morepypy.blogspot.com/

- twitter: @antocuni

- Available for consultancy & training:

  * http://antocuni.eu

  * info@antocuni.eu

- Any question?

