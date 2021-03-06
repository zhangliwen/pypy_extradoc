Next stage of PyPy warmup improvements
======================================

Hello everyone.

I'm pleased to inform that we've finished another round of
improvements to the warmup performance of PyPy. Before I go
into details, I'll recap the achievements that we've done since we've started
working on the warmup performance. I picked a random PyPy from November 2014
(which is definitely before we started the warmup work) and compared it with
a recent one, after 5.0. The exact revisions are respectively ``ffce4c795283``
and ``cfbb442ae368``. First let's compare `pure warmup benchmarks`_ that
can be found in our benchmarking suite. Out of those,
``pypy-graph-alloc-removal`` numbers should be taken with a grain of salt,
since other work could have influenced the results.
The rest of the benchmarks mentioned is bottlenecked purely by warmup times.

You can see how much your program spends in warmup running
``PYPYLOG=jit-summary:- pypy your-program.py`` under "tracing" and "backend"
fields (in the first three lines). An example looks like that::

    [e00c145a41] {jit-summary
    Tracing:        71      0.053645 <- time spent tracing & optimizing
    Backend:        71      0.028659 <- time spent compiling to assembler
    TOTAL:                  0.252217 <- total run time of the program

The results of the benchmarks

+---------------------------+------------+------------+---------+----------------+----------------+
| benchmark                 | time - old | time - new | speedup | JIT time - old | JIT time - new |
+---------------------------+------------+------------+---------+----------------+----------------+
| function_call             | 1.86       | 1.42       | 1.3x    | 1.12s          | 0.57s          |
+---------------------------+------------+------------+---------+----------------+----------------+
| function_call2            | 5.17s      | 2.73s      | 1.9x    | 4.2s           | 1.6s           |
+---------------------------+------------+------------+---------+----------------+----------------+
| bridges                   | 2.77s      | 2.07s      | 1.3x    | 1.5s           | 0.8s           |
+---------------------------+------------+------------+---------+----------------+----------------+
| pypy-graph-alloc-removal  | 2.06s      | 1.65s      | 1.25x   | 1.25s          | 0.79s          |
+---------------------------+------------+------------+---------+----------------+----------------+

.. `pure warmup benchmarks`: https://bitbucket.org/pypy/benchmarks/src/59290b59a24e54057d4c694fa4f47e7879a347a0/warmup/?at=default

As we can see, the overall warmup benchmarks got up to **90% faster** with
JIT time dropping by up to **2.5x**. We have more optimizations in the pipeline,
with an idea how to transfer some of the JIT gains into more of a total program
runtime by jitting earlier and more eagerly.

Details of the last round of optimizations
------------------------------------------

Now the nitty gritty details - what did we actually do? I covered a lot of
warmup improvements in the `past`_ `blog`_ posts so I'm going to focus on
the last change, the jit-leaner-frontend branch. This last change is simple, instead of using
pointers to store the "operations" objects created during tracing, we use a compact list of
16-bit integers (with 16bit pointers in between). On 64bit machine the memory wins are
tremendous - the new representation is 4x more efficient to use 16bit pointers than full 64bit pointers.
Additionally, the smaller representation has much better cache behavior and much less
pointer chasing in memory. It also has a better defined lifespan, so we don't need to
bother tracking them by the GC, which also saves quite a bit of time.

.. _`past`: http://morepypy.blogspot.com/2015/10/pypy-memory-and-warmup-improvements-2.html
.. _`blog`: http://morepypy.blogspot.com/2015/09/pypy-warmup-improvements.html

The change sounds simple, but the details in the underlaying data mean that
everything in the JIT had to be changed which took quite a bit of effort :-)

Going into the future on the JIT front, we have an exciting set of optimizations,
ranging from faster loops through faster warmup to using better code generation
techniques and broadening the kind of program that PyPy speeds up. Stay tuned
for the updates.

We would like to thank our commercial partners for making all of this possible.
The work has been performed by `baroquesoftware`_ and would not be possible
without support from people using PyPy in production. If your company uses
PyPy and want it to do more or does not use PyPy but has performance problems
with the Python installation, feel free to get in touch with me, trust me using
PyPy ends up being a lot cheaper than rewriting everything in go :-)

.. _`baroquesoftware`: http://baroquesoftware.com

Best regards,
Maciej Fijalkowski

