The "Science as Software" methodology
=====================================
There are many similarities between scientific research and software
development. Today many scientists develop their own software tools
for their scientific research, and as such use many of the development tools
and methodologies from software engineering. The question we pose here is::

    Is it possible to use software engineering methodologies to run a
    scientific project - essentially doing "science engineering"?

Science and Software development have a significant overlap between their respective
discipline methodologies:

======================  ===================================
Software                Science
======================  ===================================
Defining scope          Background research
----------------------  -----------------------------------
Requirements            Formulate hypothesis
----------------------  -----------------------------------
Design                  Experimental method planning
----------------------  -----------------------------------
Coding                  Data preparation / reduction
----------------------  -----------------------------------
Testing                 Data analysis / Hypothesis tests
----------------------  -----------------------------------
Documentation           Write / publish paper
----------------------  -----------------------------------
Deployment              Present work at conferences
======================  ===================================

Over the last couple of decades the whole software industry has used these steps
as a guide to delivering software on schedule to meet a certain goal.
Scientific research on the other hand follows a much more fluid format, where
scientists "play" with data to prove or disprove a certain idea.

Unfortunately the code writen to "play" with data is too often writen ad-hoc and
then thrown away after the project is complete. More often that not the code is
messy and undocumented, such that when the scientist returns to the code 6
months later, they can no longer make sense of their own constructions.
Cumulatively this leads to mountains of code being thrown away and results in
days and weeks of "wasted" time, as the results of any such study are difficult
to replicate or repeat.

Software developers on the other hand have long realised that their software
will most likely out-live them in their current position, and as such the code
*should* be writen in a way that the next developer on the project can read and
(more importantly) maintain the code base.

Given that both fields are essentially writing code to solve problems, might it
not be prudent for scientists then to also adopt such a mindset and the
associated practices and methodologies? Here I argue: yes they should!

In this project we will try to follow the workflow of a software developer
to attempt to answer a series of scientific questions in a coherent, repeatable,
documented, and above all orderly manner. Whether or not this methodology is
indeed applicable to science remains to be seen, but given the state of current
scientific coding techniques, it is definitely worth the attempt::

    Leave no code behind!
