---
title: "Complex Number Representations" 
date: 2020-06-05 
draft: false 
---

Story source:

https://leimao.github.io/blog/Complex-Number-Representations/


### Introduction

Complex numbers have been widely used in modern physics, such as Fourier
transform and Quantum mechanics. So I thought it would be important at least
to become familiar with some of the basic expressions and algebra for complex
numbers, even though they might have been taught in high school.

  

In this blog post, I would like to cover several basic expressions of complex
numbers and some of the simplest algebra based on some of the expressions.

### Complex Number

If we assume $\sqrt{-1}$ is valid and $i = \sqrt{-1}$, we could define the
following expression as complex number

where $a$ and $b$ are real numbers, and $a$ is called the real part of $c$,
whereas $b$ is its imaginary part.

### Complex Number Polar Coordinates

We could further use Cartesian coordinates $(a, b)$ to uniquely represent any
complex number.

It is also equivalent to represent the Cartesian coordinates $(a, b)$ using
polar coordinates $(\rho, \theta)$. Here, $\rho$ and $\theta$ are also called
the modulus and phase of $c$, respectively.

  

It is trivial to find

Conversely,

Therefore, we could represent a complex number using polar coordinates.

One of the reasons to consider using polar coordinates to represent complex
numbers is it has better physical interpretations on complex number algebra.

### Euler’s Formula

Euler’s Formula states that

This could be simply proved by expanding $e^{i\theta}$, $\cos \theta$ and
$\sin \theta$ using Taylor expansions, which I would not elaborate here.

### Complex Number Exponential Form

We were surprised to find that a complex number could be further simplified in
its expression.

This expression is called the exponential form of a complex number.

### Complex Number Algebra

We have two complex numbers, $c_1$ and $c_2$.

We would like to compute the addition, subtraction, multiplication, and
division for them.

  

The addition and subtraction are trivial.

The physical meanings of addition and subtraction are just simply the 2D
vector addition and subtraction.

  

The multiplication and division are slightly tedious.

It is not technically hard to verify the two equations above. But it is just
sometimes tedious to compute, and the physical meanings of multiplication and
division are not obvious.

  

If we use the exponential form of complex numbers, life becomes much easier.

The physical meanings of multiplication and division are polar coordinates
rotation with modulus expansion or contraction. Concretely, the modulus of the
two complex numbers are multiplied or divided, and the phase of the two
complex numbers are added or subtracted.

* * *

