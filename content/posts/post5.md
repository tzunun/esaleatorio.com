---
title: "FreeNAS Is Coming to Linux" 
date: 2020-06-05 
draft: false 
---

Story source:

https://www.ixsystems.com/community/threads/starting-our-next-open-source-project-truenas-scale.85203/


Hello TrueNAS and FreeNAS Community,

As many of you are aware, TrueNAS 12.0 BETA is soon to be released. It

[unifies FreeNAS and TrueNAS into a single
image](https://www.ixsystems.com/blog/freenas-truenas-unification/)

and will make maintaining and documenting these releases significantly more
efficient. The early testing and reviews have gone very well and it’s exciting
to see the upcoming OpenZFS 2.0 perform as well as it does. We’re confident
that you’ll like TrueNAS CORE when you try it out.

With the bulk of the TrueNAS 12.0 development work starting to wind down, we
wanted to take some time to confirm the rumors of some new work that has been
occurring behind the scenes in the iX development labs. As some clever GitHub
code-watchers have already noticed, we’ve been hard at work on a new project
called TrueNAS SCALE. This is an ambitious new Open Source initiative allowing
us to take some big new steps forward in software-defined infrastructure
capabilities.

SCALE is an exciting new addition to the TrueNAS software family. It uses much
of the same TrueNAS 12.0 source code, but adds a few different twists.

For those eager to know more about the the goals of the SCALE project, they
are defined by this acronym:

**S**

cale-out

**C**

onverged

**A**

ctive-active

**L**

inux containers

**E**

asy-to-manage

Since many in our community have already noticed and been speculating for a
while, I’ll confirm now that SCALE is based upon Linux. Debian 11 (Bullseye)
is currently being used as the platform for this new project. Linux is a key
requirement to achieve some of the SCALE project goals. The ability to run
OpenZFS 2.0 across both FreeBSD and Linux provides the TrueNAS family with the
software diversity to service a wide variety of user infrastructure needs.

We’re pleased to let developers know that the

[source code](https://github.com/truenas/)

for TrueNAS SCALE is already available on GitHub and under very active
development. Over the next quarter, we will give you more detailed information
about the architecture, download links to the installation images, and more
details on how to get involved for collaboration. We’re currently hard at work
finishing up some of the base functionality on a very early developer preview
image. This nightly image will allow community developers and early technical
preview audiences to kick the tires and get more involved in the early
development stages of this new product. SCALE will be a development project
for the remainder of 2020 with a planned release in 2021.

We are starting a

[new discussion group](https://www.ixsystems.com/community/forums/truenas-
scale-discussion/)

for project SCALE as well. If you or your organization are keen to contribute
to a project with these goals, then please follow and comment in the
discussion group and we’ll keep you in the loop.

It’s important to note that the SCALE project doesn’t change the plans for the
continued support and development of TrueNAS CORE and TrueNAS Enterprise on
FreeBSD. The full suite of software will be very complementary to each other.
Much of the software base will be common and all of them will support being
fully managed via TrueCommand.

