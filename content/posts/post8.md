---
title: "Why your previous developer was terrible" 
date: 2020-06-05 
draft: false 
---

Story source:

https://link.medium.com/ffvxE8GC36


You hired a new developer for a project you’re working on and she seems to
have solved all of your problems. She’s been on the job for 3 days and she’s
already suggested upgrades for 5 of your libraries and re-organized your JIRA
issues. At every turn, she seems to validate your choice in hiring her. She’s
found 8 bugs that were glaring and would have caused a critical meltdown. How
terrible was your previous developer that he couldn’t have spotted any of
this?? She’s baffled by his decision to use the XYZ framework and doesn’t
understand why he chose to use Postgres instead of CouchDB for this particular
application. She complains to you that the lack of a CDN is costing you HOURS
in needless content serving. How could you have been so blind to not see any
of this? Well, it wasn’t your job, right? That was your previous developers’
job and he seems to have failed miserably. Good riddance.

# The curse of the present

Don’t worry — your situation is far from unique. I’ve seen it time and time
again that a new developer comes in and seems to change everything almost
overnight. She or he suggests new tools, new processes, new languages and new
everything. All of this while badmouthing the previous developer or team. I’ve
been on all sides of this fine play. I’ve been the “previous developer” who
got badmouthed by the new guy. I’ve been the new guy that used the previous
guy as my scapegoat. I’ve hired developers that have been in both positions.
I’ve worked for companies that couldn’t see what was plain to me: this happens
all the time.

It’s what I call the “curse of the present.” When you, as a developer, look at
the choices used to build a particular application, you’re blown away at the
poor decisions made at every turn. “Why, oh why, is this built with Rails when
Node.js would be so much better?” or “how could the previous developer not
have forseen that the database would need referential integrity when they
chose MongoDB?” But what you may not realize is that you are seeing the
application as it exists today. When the previous developer (or team) had to
develop it, they had to deal with a LOT of unknowns. They had to make many
decisions under a cloak of opacity. You are cursed with the knowledge of the
present, so the system seems like a hackjob of bad decisions.

# Pass the blame

Another reason that developers tend to blame the previous developer is because
it’s easy. The previous developer no longer has to justify his actions and
isn’t there to defend himself. So blaming him is **super** easy. If a
developer doesn’t want to work very hard or solve a particular problem, it’s
far easier to blame something inherent in the system rather than laziness (or
incomptence). When the boss asks “what’s the timeline on the [whatever],” it’s
easy and convenient to say “well, normally it would only take 2 weeks, but
since we’re dealing with an older version of [some library], it’ll probably
take a month.” It may be true that the older version will take more time, but
it also may be true that you, the developer, just don’t feel like working very
hard this month.

# Justification

You hired this new developer for a reason. After a series of interviews, some
coding tests and whatnot, you finally hired this person. Now, this person has
to justify that they’re worthwhile. Developers tend to think that a great way
to do this is by making **BIG** changes early on. Implementing all sorts of
processes that don’t need to be implemented and introducing all sorts of tools
that no one else on the team has heard of. I’ve seen countless permutations of
this behavior, where a developer will come around and say how bad using
Pivotal is and that we now need to use JIRA or they can’t believe we’re still
using Subversion and how we should move to Git. It justifies the knowledge
that we have and hopefully impresses you, oh glorious boss.

# End it

I think it’s a bad practice to simply blame the previous developer or team for
something. Give them the benefit of the doubt and assume that they made the
best decisions they could under the constraints they had. They didn’t have the
knowledge of the fully baked system. In the short term, it may impress the
overlords that brought you into the organization, but in the long run, it
hurts us all. We’ve all been that developer that’s been blamed for countless
problems after we leave — it doesn’t feel very good to know that it’s
happening to you, so why do it to others? Take the moral high ground. Even if
it is the previous guy’s fault, don’t frame it like that.

Be a hero in the long run by being a solid team player that makes good
judgement calls whenever you can. Don’t be the short-term hero that throws
people under the bus. You’ll probably get away with it, but we (the developer
community) won’t like you very much if you do. Now, granted, there are certain
cases where the previous developer was a truly terrible developer. In those
cases, make the stakeholders aware of everything all at once, rather than as a
convenient excuse for you to use whenever you either don’t want to do
something or can’t.

