---
title: "Show HN: Netflix migrated its Infrastructure to AWS" 
date: 2020-06-05 
draft: false 
---

Story source:

https://medium.com/@Zack.Grannan/the-epic-migration-of-netflix-to-aws-7f5c042fbafa


In its 20-year history, Netflix has grown from a DVD rental website with 30
employees to a global streaming service with over 5,000 titles, 130 million
subscribers, and $11 billion annual revenue that has drastically transformed
the entertainment industry.

At the Consumer Electronics Show in January 2016, Netflix CEO Reed Hastings
launched the service in more than 130 countries.

“While you have been listening to me talk, the Netflix service has gone live
in nearly every country of the world,” he announced on the Las Vegas
Convention Center stage. “Today, right now, you are witnessing the birth of a
global TV network.”

This was all made possible by a radical transformation of a previously
traditional IT operation, as Dave Hahn, a senior engineer in Netflix’s cloud
operations and reliability team, explained recently at the Service Desk and IT
Support Show in London.

“We flipped on the service for another 130 countries, and millions of new
customers that we hadn’t previously been servicing,” said Hahn.

“I think you can imagine the amount of work and thinking and architecture
design we had to do to open up to 130 countries, and millions of new customers
just in that moment; the technical architecture, the research, the billing
systems, the kind of people that we needed and the thinking about these kinds
of problems in order to make that happen.”

The journey began when Netflix decided to move from its own data centers to
the public cloud.

# Migrating with microservices

In 2008, Netflix was running relational databases in its own data centers when
disaster struck. A data center failure shut the entire service down and
stopped DVD shipments for three days.

The company’s owners faced a choice: turn Netflix into a world-class data
center operations company or move the service to the public cloud.

Netflix was growing fast. The thousands of videos and tens of millions of
customers were already generating an enormous quantity of data. The company
would struggle to rack the servers in their own data centers fast enough to
handle the ever-growing volumes, but the cloud would let them add thousands of
virtual servers and petabytes of storage within minutes.

Migration to the cloud was a clear choice. They soon became a poster child
customer for Amazon Web Services (AWS), choosing the company for its scale and
broad set of services and features.

The move would require a complete rearchitecting of the company’s traditional
infrastructure though. They could have forklifted all of their monolithic
enterprise systems out of the data center and dropped them into AWS, but this
would only have brought all of their old data center problems to the cloud.
Instead, they chose to rebuild the Netflix technology in AWS and fundamentally
change the way that the company operated.

“Software’s like anything else; if you can design it for the environment that
it’s going to be living in it will do more of the things you want it to do,
more often and more regularly,” said Hahn. “So we chose to move to
microservices.”

This made the infrastructure much more agile by breaking aspects of the
service up into multiple
[microservices](https://www.computerworlduk.com/applications/microservices-
explained-is-this-just-tweaked-soa-or-something-much-bigger-3638372/), managed
by their own small teams who understood how their service worked and
interacted with other systems. This was pretty groundbreaking at the time.

This provides clear, specific insights that make it easier to change the
service, which leads to smaller and faster deployments. It also allows them to
isolate services to understand the various performance profiles, patterns, and
securities in each micro-service, and move away from any individual piece
that’s causing a problem.

“I don’t have to assemble all of these pieces built by other people in order
to have a singular deployment,” said Hahn. “Any Netflix service team can
deploy its service at any time. It requires no coordination, no scheduling, no
crucible to get to production.”

# Benefits of the cloud

It took Netflix seven years to complete the migration to the cloud. In 2016,
the last remaining data centers used by the streaming service were shut down.
In its place was a new cloud infrastructure running all of Netflix’s computing
and storage needs, from customer information to recommendation algorithms.

The migration improved Netflix’s scalability and service availability and the
velocity by which the company could release new content, features, interfaces,
and interactions. It also freed up the capacity of engineers, cut the costs of
streaming, drastically improved availability, and added the experience and
expertise of AWS.

“The other thing is that the cost model is really nice for us,” added Hahn.
“You pay for what you use. That allows us to do a lot of experimentations.”

This gives them greater freedom to test new features and improve existing
ones, such as the rows of content recommendations that are personalized every
day.

“These large recommendation algorithms require a lot of computing work,” Hahn
explained. “If I want to find out if a new one we’re playing with does better,
I don’t want to turn off the old one, because you still need recommendations.

“I can now spin up an entirely new set of machines in the tens, or hundreds or
thousands in an afternoon and chunk through my data and see if we’ve done
better, and I only pay for the portions I use. It allows us an amazing amount
of freedom in experimentation.”

# Content delivery

The cloud is only one part of the Netflix user experience. Everything that
happens before they hit play takes place in AWS, but the video content that
follows comes from a separate system: Netflix OpenConnect, the company’s
proprietary content delivery network (CDN). The OpenConnect appliances store
the video content and deliver it to client devices.

CDNs are designed to deliver internet-based content to viewers by bringing it
closer to where they’re watching. Netflix originally outsourced streaming
video delivery to third-party CDN suppliers, but as the company grew, these
vendors struggled to support the traffic. Netflix needed more control over the
service and user experience.

The company decided to design a CDN tailored to its needs.

It now installs OpenConnect appliances that store and deliver content inside
local Internet Service Provider (ISP) data centers, which isolates the Netflix
service from the wider internet. Popularity algorithms and storage techniques
help distribute the content in ways that maximize offload efficiency. The
system reduces the demand on upstream network capacity and helps Netflix work
more closely with the ISP networks that host its traffic.

“We designed OpenConnect caching boxes to hold our content, and wherever we
can we install them inside of your internet service provider’s network, so
that when you see those video bits you aren’t actually transiting off of your
operator’s network,” said Hahn.

The new system cut the appearances of the loathed buffering wheel by an order
of magnitudes. It also allowed Netflix to make the CDN software more
intelligent. Now, whenever a customer presses play their device can get its
content from numerous places on the internet.

The investment paid off when a fire in an ISP data center in Brazil burned
down Netflix’s entire stack of machines. Customers who had been streaming from
the ISP didn’t experience any change in their user experience.

“Their devices already knew somewhere else to go get the data,” said Hahn. “It
didn’t interrupt even one frame of streaming when we literally burned down the
base.”

# Chaos engineering culture

Netflix developers are well known these days for their unique approach to
engineering culture. A self-service chaos engineering tool called the Chaos
Automation Platform was pioneered to test problems in their production
environments so they can be sure that their software will behave as they want
during a failure.

“People press the play button on Netflix thousands of times a second,” said
Hahn. “If the systems cannot auto recover, if they cannot handle bad
situations if they cannot self-repair, by the time I get a human involved, in
the best-case scenario, minutes have gone by.

“You can get an idea of how many of our customers we’ve disappointed in the
three or four or five minutes it may take to get a human involved, and in the
right place and work. Chaos engineering is an excellent inoculation of
failures.”

They use the chaos engineering method to ensure Netflix can survive a failure
in one of the three AWS regions it uses. Every month, they turn off one of the
regions and test that they can move all of the customers that it was serving
to another one within six minutes.

To embrace chaos without causing destruction, Netflix had to create a
corporate culture that supported such ideas.

The central principles were formalized in the 127-slide Netflix Culture Deck,
which Facebook COO Sheryl Sandberg [said](https://www.gq.com/story/netflix-
founder-reed-hastings-house-of-cards-arrested-development?mobify=0): “may well
be the most important document ever to come out of the Valley”.

A central tenet of the policy is balancing freedom with responsibility. Teams
are given ownership of their microservice and encouraged to act independently
but not recklessly.

“Netflix managers do not set out tasks for their employees to do or design
their projects,” said Hahn. “Their job is to give them the appropriate context
so they can make the decisions, to hire excellent, stunning colleagues for
them to work with, and to stay out of their way.”

The company avoids making too many rules beyond a set of fundamental
principles such as never touching customer data. Hahn describes the approach
as building guardrails but not gates and claims he can count on one hand the
number of times he’s had to tell an engineer exactly what to do.

“By making sure that that context is widely and regularly shared I can have
someone design a billing system, someone else working on algorithmic systems,
SREs on our reliability teams, and somebody else working on customer service,
and they’ll understand the same context and march towards the same goals,” he
said.

“That allows us to keep those teams loosely covered. We don’t have lots of
structures and controls, but we keep them highly aligned.”

