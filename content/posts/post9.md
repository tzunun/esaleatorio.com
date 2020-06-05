---
title: "Kolmogorov Complexity" 
date: 2020-06-05 
draft: false 
---

Story source:

https://en.wikipedia.org/wiki/Kolmogorov_complexity


Measure of algorithmic complexity

[![](//upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Mandelpart2_red.png/310px-
Mandelpart2_red.png)](/wiki/File:Mandelpart2_red.png)

This image illustrates part of the

[Mandelbrot set](/wiki/Mandelbrot_set "Mandelbrot set")
[fractal](/wiki/Fractal "Fractal")

. Simply storing the 24-bit color of each pixel in this image would require
1.62 million bytes, but a small computer program can reproduce these 1.62
million bytes using the definition of the Mandelbrot set and the coordinates
of the corners of the image. Thus, the Kolmogorov complexity of the raw file
encoding this bitmap is much less than 1.62 million bytes in any pragmatic
model of computation.

In [algorithmic information theory](/wiki/Algorithmic_information_theory
"Algorithmic information theory") (a subfield of [computer
science](/wiki/Computer_science "Computer science") and
[mathematics](/wiki/Mathematics "Mathematics")), the **Kolmogorov complexity**
of an object, such as a piece of text, is the length of a shortest [computer
program](/wiki/Computer_program "Computer program") (in a predetermined
[programming language](/wiki/Programming_language "Programming language"))
that produces the object as output. It is a measure of the
[computational](/wiki/Computation "Computation") resources needed to specify
the object, and is also known as **algorithmic complexity** ,
**Solomonoff–Kolmogorov–Chaitin complexity** , **program-size complexity** ,
**descriptive complexity** , or **algorithmic entropy**. It is named after
[Andrey Kolmogorov](/wiki/Andrey_Kolmogorov "Andrey Kolmogorov"), who first
published on the subject in 1963.[1][2]

The notion of Kolmogorov complexity can be used to state and [prove
impossibility](/wiki/Proof_of_impossibility "Proof of impossibility") results
akin to [Cantor's diagonal argument](/wiki/Cantor%27s_diagonal_argument
"Cantor's diagonal argument"), [Gödel's incompleteness
theorem](/wiki/G%C3%B6del%27s_incompleteness_theorem "Gödel's incompleteness
theorem"), and [Turing's halting problem](/wiki/Halting_problem "Halting
problem"). In particular, no program _P_ computing a [lower
bound](/wiki/Lower_bound "Lower bound") for each text's Kolmogorov complexity
can return a value essentially larger than _P_ 's own length (see section §
Chaitin's incompleteness theorem); hence no single program can compute the
exact Kolmogorov complexity for infinitely many texts.

##
Definition[[edit](/w/index.php?title=Kolmogorov_complexity&action=edit&section=1
"Edit section: Definition")]

Consider the following two [strings](/wiki/String_\(computer_science\) "String
\(computer science\)") of 32 lowercase letters and digits:

    `abababababababababababababababab` , and
    `4c1j5b2p0cv4w1x8rx2y39umgw5q85s7`

The first string has a short English-language description, namely "`write ab
16 times`", which consists of **17** characters. The second one has no obvious
simple description (using the same character set) other than writing down the
string itself, i.e., "`write 4c1j5b2p0cv4w1x8rx2y39umgw5q85s7`" which has
**38** characters. Hence the operation of writing the first string can be said
to have "less complexity" than writing the second.

More formally, the [complexity](/wiki/Complexity "Complexity") of a string is
the length of the shortest possible description of the string in some fixed
[universal](/wiki/Turing_complete "Turing complete") description language (the
sensitivity of complexity relative to the choice of description language is
discussed below). It can be shown that the Kolmogorov complexity of any string
cannot be more than a few bytes larger than the length of the string itself.
Strings like the _abab_ example above, whose Kolmogorov complexity is small
relative to the string's size, are not considered to be complex.

The Kolmogorov complexity can be defined for any mathematical object, but for
simplicity the scope of this article is restricted to strings. We must first
specify a description language for strings. Such a description language can be
based on any computer programming language, such as
[Lisp](/wiki/Lisp_programming_language "Lisp programming language"),
[Pascal](/wiki/Pascal_\(programming_language\) "Pascal \(programming
language\)"), or [Java](/wiki/Java_\(programming_language\) "Java
\(programming language\)"). If **P** is a program which outputs a string _x_ ,
then **P** is a description of _x_. The length of the description is just the
length of **P** as a character string, multiplied by the number of bits in a
character (e.g., 7 for [ASCII](/wiki/ASCII "ASCII")).

We could, alternatively, choose an encoding for [Turing
machines](/wiki/Turing_machine "Turing machine"), where an _encoding_ is a
function which associates to each Turing Machine **M** a bitstring < **M** >.
If **M** is a Turing Machine which, on input _w_ , outputs string _x_ , then
the concatenated string < **M** > _w_ is a description of _x_. For theoretical
analysis, this approach is more suited for constructing detailed formal proofs
and is generally preferred in the research literature. In this article, an
informal approach is discussed.

Any string _s_ has at least one description. For example, the second string
above is output by the program:

    
    
    **function** GenerateString2()
        **return** "4c1j5b2p0cv4w1x8rx2y39umgw5q85s7"
    

whereas the first string is output by the (much shorter) pseudo-code:

    
    
    **function** GenerateString1()
        **return** "ab" × 16
    

If a description _d_ ( _s_ ) of a string _s_ is of minimal length (i.e., using
the fewest bits), it is called a **minimal description** of _s_ , and the
length of _d_ ( _s_ ) (i.e. the number of bits in the minimal description) is
the **Kolmogorov complexity** of _s_ , written _K_ ( _s_ ). Symbolically,

    _K_ ( _s_ ) = | _d_ ( _s_ )|.

The length of the shortest description will depend on the choice of
description language; but the effect of changing languages is bounded (a
result called the _invariance theorem_ ).

## Invariance
theorem[[edit](/w/index.php?title=Kolmogorov_complexity&action=edit&section=2
"Edit section: Invariance theorem")]

### Informal
treatment[[edit](/w/index.php?title=Kolmogorov_complexity&action=edit&section=3
"Edit section: Informal treatment")]

There are some description languages which are optimal, in the following
sense: given any description of an object in a description language, said
description may be used in the optimal description language with a constant
overhead. The constant depends only on the languages involved, not on the
description of the object, nor the object being described.

Here is an example of an optimal description language. A description will have
two parts:

  * The first part describes another description language.
  * The second part is a description of the object in that language.

In more technical terms, the first part of a description is a computer
program, with the second part being the input to that computer program which
produces the object as output.

**The invariance theorem follows:** Given any description language _L_ , the
optimal description language is at least as efficient as _L_ , with some
constant overhead.

**Proof:** Any description _D_ in _L_ can be converted into a description in
the optimal language by first describing _L_ as a computer program _P_ (part
1), and then using the original description _D_ as input to that program (part
2). The total length of this new description _D′_ is (approximately):

    | _D′_ | = | _P_ | + | _D_ |

The length of _P_ is a constant that doesn't depend on _D_. So, there is at
most a constant overhead, regardless of the object described. Therefore, the
optimal language is universal [up to](/wiki/Up_to "Up to") this additive
constant.

### A more formal
treatment[[edit](/w/index.php?title=Kolmogorov_complexity&action=edit&section=4
"Edit section: A more formal treatment")]

**Theorem** : If _K_ 1 and _K_ 2 are the complexity functions relative to
[Turing complete](/wiki/Turing_complete "Turing complete") description
languages _L_ 1 and _L_ 2, then there is a constant _c_ – which depends only
on the languages _L_ 1 and _L_ 2 chosen – such that

    ∀ _s_. − _c_ ≤ _K_ 1( _s_ ) − _K_ 2( _s_ ) ≤ _c_.

**Proof** : By symmetry, it suffices to prove that there is some constant _c_
such that for all strings _s_

    _K_ 1( _s_ ) ≤ _K_ 2( _s_ ) + _c_.

Now, suppose there is a program in the language _L_ 1 which acts as an
[interpreter](/wiki/Interpreter_\(computing\) "Interpreter \(computing\)") for
_L_ 2:

    
    
    **function** InterpretLanguage( **string** _p_ )
    

where _p_ is a program in _L_ 2. The interpreter is characterized by the
following property:

    Running `InterpretLanguage` on input _p_ returns the result of running _p_.

Thus, if **P** is a program in _L_ 2 which is a minimal description of _s_ ,
then `InterpretLanguage`( **P** ) returns the string _s_. The length of this
description of _s_ is the sum of

  1. The length of the program `InterpretLanguage`, which we can take to be the constant _c_.
  2. The length of **P** which by definition is _K_ 2( _s_ ).

This proves the desired upper bound.

## History and
context[[edit](/w/index.php?title=Kolmogorov_complexity&action=edit&section=5
"Edit section: History and context")]

[Algorithmic information theory](/wiki/Algorithmic_information_theory
"Algorithmic information theory") is the area of computer science that studies
Kolmogorov complexity and other complexity measures on strings (or other [data
structures](/wiki/Data_structure "Data structure")).

The concept and theory of Kolmogorov Complexity is based on a crucial theorem
first discovered by [Ray Solomonoff](/wiki/Ray_Solomonoff "Ray Solomonoff"),
who published it in 1960, describing it in "A Preliminary Report on a General
Theory of Inductive Inference"[3] as part of his invention of [algorithmic
probability](/wiki/Algorithmic_probability "Algorithmic probability"). He gave
a more complete description in his 1964 publications, "A Formal Theory of
Inductive Inference," Part 1 and Part 2 in _Information and Control_.[4][5]

Andrey Kolmogorov later [independently published](/wiki/Multiple_discovery
"Multiple discovery") this theorem in _Problems Inform. Transmission_[6] in
1965. [Gregory Chaitin](/wiki/Gregory_Chaitin "Gregory Chaitin") also presents
this theorem in _J. ACM_ – Chaitin's paper was submitted October 1966 and
revised in December 1968, and cites both Solomonoff's and Kolmogorov's
papers.[7]

The theorem says that, among algorithms that decode strings from their
descriptions (codes), there exists an optimal one. This algorithm, for all
strings, allows codes as short as allowed by any other algorithm up to an
additive constant that depends on the algorithms, but not on the strings
themselves. Solomonoff used this algorithm and the code lengths it allows to
define a "universal probability" of a string on which inductive inference of
the subsequent digits of the string can be based. Kolmogorov used this theorem
to define several functions of strings, including complexity, randomness, and
information.

When Kolmogorov became aware of Solomonoff's work, he acknowledged
Solomonoff's priority.[8] For several years, Solomonoff's work was better
known in the Soviet Union than in the Western World. The general consensus in
the scientific community, however, was to associate this type of complexity
with Kolmogorov, who was concerned with randomness of a sequence, while
Algorithmic Probability became associated with Solomonoff, who focused on
prediction using his invention of the universal prior probability
distribution. The broader area encompassing descriptional complexity and
probability is often called Kolmogorov complexity. The computer scientist Ming
Li considers this an example of the [Matthew
effect](/wiki/Matthew_effect_\(sociology\) "Matthew effect \(sociology\)"):
"…to everyone who has more will be given…"[9]

There are several other variants of Kolmogorov complexity or algorithmic
information. The most widely used one is based on [self-delimiting
programs](/w/index.php?title=Self-delimiting_program&action=edit&redlink=1
"Self-delimiting program \(page does not exist\)"), and is mainly due to
[Leonid Levin](/wiki/Leonid_Levin "Leonid Levin") (1974).

An axiomatic approach to Kolmogorov complexity based on [Blum
axioms](/wiki/Blum_axioms "Blum axioms") (Blum 1967) was introduced by Mark
Burgin in the paper presented for publication by Andrey Kolmogorov.[10]

## Basic
results[[edit](/w/index.php?title=Kolmogorov_complexity&action=edit&section=6
"Edit section: Basic results")]

In the following discussion, let _K_ ( _s_ ) be the complexity of the string
_s_.

It is not hard to see that the minimal description of a string cannot be too
much larger than the string itself — the program `GenerateFixedString` above
that outputs _s_ is a fixed amount larger than _s_.

**Theorem** : There is a constant _c_ such that

    ∀ _s_. _K_ ( _s_ ) ≤ | _s_ | + _c_.

### Uncomputability of Kolmogorov
complexity[[edit](/w/index.php?title=Kolmogorov_complexity&action=edit&section=7
"Edit section: Uncomputability of Kolmogorov complexity")]

**Theorem** : There exist strings of arbitrarily large Kolmogorov complexity.
Formally: for each _n_ ∈ ℕ, there is a string _s_ with _K_ ( _s_ ) ≥ _n_.[note
1]

**Proof:** Otherwise all of the infinitely many possible finite strings could
be generated by the finitely many[note 2] programs with a complexity below _n_
bits.

**Theorem** : _K_ is not a [computable function](/wiki/Computable_function
"Computable function"). In other words, there is no program which takes a
string _s_ as input and produces the integer _K_ ( _s_ ) as output.

The following [indirect **proof**](/wiki/Indirect_proof "Indirect proof") uses
a simple [Pascal](/wiki/Pascal_\(programming_language\) "Pascal \(programming
language\)")-like language to denote programs; for sake of proof simplicity
assume its description (i.e. an [interpreter](/wiki/Interpreter_\(computing\)
"Interpreter \(computing\)")) to have a length of 1400000 bits. Assume for
contradiction there is a program

    
    
    **function** KolmogorovComplexity( **string** s)
    

which takes as input a string _s_ and returns _K_ ( _s_ ); for sake of proof
simplicity, assume the program's length to be 7000000000 bits. Now, consider
the following program of length 1288 bits:

    
    
    **function** GenerateComplexString()
        **for** i = 1 **to** infinity:
            **for each** string s **of** length exactly i
                **if** KolmogorovComplexity(s) ≥ 8000000000
                    **return** s
    

Using `KolmogorovComplexity` as a subroutine, the program tries every string,
starting with the shortest, until it returns a string with Kolmogorov
complexity at least 8000000000 bits,[note 3] i.e. a string that cannot be
produced by any program shorter than 8000000000 bits. However, the overall
length of the above program that produced _s_ is only 7001401288 bits,[note 4]
which is a contradiction. (If the code of `KolmogorovComplexity` is shorter,
the contradiction remains. If it is longer, the constant used in
`GenerateComplexString` can always be changed appropriately.)[note 5]

The above proof uses a contradiction similar to that of the [Berry
paradox](/wiki/Berry_paradox "Berry paradox"): "1The 2smallest 3positive
4integer 5that 6cannot 7be 8defined 9in 10fewer 11than 12twenty 13English
14words". It is also possible to show the non-computability of _K_ by
reduction from the non-computability of the halting problem _H_ , since _K_
and _H_ are [Turing-equivalent](/wiki/Turing_degree#Turing_equivalence "Turing
degree").[11]

There is a corollary, humorously called the "[full employment
theorem](/wiki/Full_employment_theorem "Full employment theorem")" in the
programming language community, stating that there is no perfect size-
optimizing compiler.

#### A naive attempt at a program to compute _K_
[[edit](/w/index.php?title=Kolmogorov_complexity&action=edit&section=8 "Edit
section: A naive attempt at a program to compute K")]

At first glance it might seem trivial to write a program which can compute _K_
( _s_ ) for any _s_ (thus disproving the above theorem), such as the
following:

    
    
    **function** KolmogorovComplexity( **string** s)
        **for** i = 1 **to** infinity:
            **for each** string p **of** length exactly i
                **if** isValidProgram(p) **and** evaluate(p) == s
                    **return** i
    

This program iterates through all possible programs (by iterating through all
possible strings and only considering those which are valid programs),
starting with the shortest. Each program is executed to find the result
produced by that program, comparing it to the input _s_. If the result matches
the length of the program is returned.

However this will not work because some of the programs _p_ tested will not
terminate, e.g. if they contain infinite loops. There is no way to avoid all
of these programs by testing them in some way before executing them due to the
non-computability of the [halting problem](/wiki/Halting_problem "Halting
problem").

### Chain rule for Kolmogorov
complexity[[edit](/w/index.php?title=Kolmogorov_complexity&action=edit&section=9
"Edit section: Chain rule for Kolmogorov complexity")]

The chain rule[12] for Kolmogorov complexity states that

    _K_ ( _X_ , _Y_ ) ≤ _K_ ( _X_ ) + _K_ ( _Y_ | _X_ ) + _O_ (log( _K_ ( _X_ , _Y_ ))).

It states that the shortest program that reproduces _X_ and _Y_ is [no
more](/wiki/Big-O_notation "Big-O notation") than a logarithmic term larger
than a program to reproduce _X_ and a program to reproduce _Y_ given _X_.
Using this statement, one can define [an analogue of mutual information for
Kolmogorov complexity](/wiki/Mutual_information#Absolute_mutual_information
"Mutual information").

##
Compression[[edit](/w/index.php?title=Kolmogorov_complexity&action=edit&section=10
"Edit section: Compression")]

It is straightforward to compute upper bounds for _K_ ( _s_ ) – simply
[compress](/wiki/Data_compression "Data compression") the string _s_ with some
method, implement the corresponding decompressor in the chosen language,
concatenate the decompressor to the compressed string, and measure the length
of the resulting string – concretely, the size of a [self-extracting
archive](/wiki/Self-extracting_archive "Self-extracting archive") in the given
language.

A string _s_ is compressible by a number _c_ if it has a description whose
length does not exceed | _s_ | − _c_ bits. This is equivalent to saying that
_K_ ( _s_ ) ≤ | _s_ | − _c_. Otherwise, _s_ is incompressible by _c_. A string
incompressible by 1 is said to be simply _incompressible_ – by the [pigeonhole
principle](/wiki/Pigeonhole_principle "Pigeonhole principle"), which applies
because every compressed string maps to only one uncompressed string,
[incompressible strings](/wiki/Incompressible_string "Incompressible string")
must exist, since there are 2 _n_ bit strings of length _n_ , but only 2 _n_ −
1 shorter strings, that is, strings of length less than _n_ , (i.e. with
length 0, 1, ..., _n − 1).[note 6]_

For the same reason, most strings are complex in the sense that they cannot be
significantly compressed – their _K_ ( _s_ ) is not much smaller than | _s_ |,
the length of _s_ in bits. To make this precise, fix a value of _n_. There are
2 _n_ bitstrings of length _n_. The
[uniform](/wiki/Uniform_distribution_\(discrete\) "Uniform distribution
\(discrete\)") [probability](/wiki/Probability "Probability") distribution on
the space of these bitstrings assigns exactly equal weight 2− _n_ to each
string of length _n_.

**Theorem** : With the uniform probability distribution on the space of
bitstrings of length _n_ , the probability that a string is incompressible by
_c_ is at least 1 − 2− _c_ +1 \+ 2− _n_.

To prove the theorem, note that the number of descriptions of length not
exceeding _n_ − _c_ is given by the geometric series:

    1 + 2 + 22 \+ … + 2 _n_ − _c_ = 2 _n_ − _c_ +1 − 1.

There remain at least

    2 _n_ − 2 _n_ − _c_ +1 \+ 1

bitstrings of length _n_ that are incompressible by _c_. To determine the
probability, divide by 2 _n_.

## Chaitin's incompleteness
theorem[[edit](/w/index.php?title=Kolmogorov_complexity&action=edit&section=11
"Edit section: Chaitin's incompleteness theorem")]

[![](//upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Kolmogorov_complexity_and_computable_lower_bounds_svg.svg/600px-
Kolmogorov_complexity_and_computable_lower_bounds_svg.svg.png)](/wiki/File:Kolmogorov_complexity_and_computable_lower_bounds_svg.svg)

Kolmogorov complexity

_K_ ( _s_ )

, and two computable lower bound functions

`prog1(s)`

,

`prog2(s)`

. The horizontal axis (

[logarithmic scale](/wiki/Logarithmic_scale "Logarithmic scale")

) enumerates all

[strings](/wiki/String_\(computer_science\) "String \(computer science\)") _s_

, ordered by length; the vertical axis (

[linear scale](/wiki/Linear_scale "Linear scale")

) measures Kolmogorov complexity in

[bits](/wiki/Bit "Bit")

. Most strings are incompressible, i.e. their Kolmogorov complexity exceeds
their length by a constant amount. 9 compressible strings are shown in the
picture, appearing as almost vertical slopes. Due to Chaitin's incompleteness
theorem (1974), the output of any program computing a lower bound of the
Kolmogorov complexity cannot exceed some fixed limit, which is independent of
the input string

_s_

.

By the above theorem (§ Compression), most strings are complex in the sense
that they cannot be described in any significantly "compressed" way. However,
it turns out that the fact that a specific string is complex cannot be
formally proven, if the complexity of the string is above a certain threshold.
The precise formalization is as follows. First, fix a particular [axiomatic
system](/wiki/Axiomatic_system "Axiomatic system") **S** for the [natural
numbers](/wiki/Natural_number "Natural number"). The axiomatic system has to
be powerful enough so that, to certain assertions **A** about complexity of
strings, one can associate a formula **F** **A** in **S**. This association
must have the following property:

If **F** **A** is provable from the axioms of **S** , then the corresponding
assertion **A** must be true. This "formalization" can be achieved based on a
[Gödel numbering](/wiki/G%C3%B6del_numbering "Gödel numbering").

**Theorem** : There exists a constant _L_ (which only depends on **S** and on
the choice of description language) such that there does not exist a string
_s_ for which the statement

    _K_ ( _s_ ) ≥ _L_ (as formalized in **S** )

can be proven within **S**.[13]:Thm.4.1b

**Proof** : The proof of this result is modeled on a self-referential
construction used in [Berry's paradox](/wiki/Berry%27s_paradox "Berry's
paradox").

We can find an effective enumeration of all the formal proofs in **S** by some
procedure

    
    
    **function** NthProof( **int** _n_ )
    

which takes as input _n_ and outputs some proof. This function enumerates all
proofs. Some of these are proofs for formulas we do not care about here, since
every possible proof in the language of **S** is produced for some _n_. Some
of these are complexity formulas of the form _K_ ( _s_ ) ≥ _n_ where _s_ and
_n_ are constants in the language of **S**. There is a procedure

    
    
    **function** NthProofProvesComplexityFormula( **int** _n_ )
    

which determines whether the _n_ th proof actually proves a complexity formula
_K_ ( _s_ ) ≥ _L_. The strings _s_ , and the integer _L_ in turn, are
computable by procedure:

    
    
    **function** StringNthProof( **int** _n_ )
    
    
    
    **function** ComplexityLowerBoundNthProof( **int** _n_ )
    

Consider the following procedure:

    
    
    **function** GenerateProvablyComplexString( **int** _n_ )
        **for** i = 1 to infinity:
            **if** NthProofProvesComplexityFormula(i) **and** ComplexityLowerBoundNthProof(i) ≥ _n_
                **return** StringNthProof( _i_ )
    

Given an _n_ , this procedure tries every proof until it finds a string and a
proof in the [formal system](/wiki/Formal_system "Formal system") **S** of the
formula _K_ ( _s_ ) ≥ _L_ for some _L_ ≥ _n_ ; if no such proof exists, it
loops forever.

Finally, consider the program consisting of all these procedure definitions,
and a main call:

    
    
    GenerateProvablyComplexString( _n_ 0)
    

where the constant _n_ 0 will be determined later on. The overall program
length can be expressed as _U_ +log2( _n_ 0), where _U_ is some constant and
log2( _n_ 0) represents the length of the integer value _n_ 0, under the
reasonable assumption that it is encoded in binary digits. Now consider the
function _f_ :[[2,∞)](/wiki/Interval_\(mathematics\) "Interval
\(mathematics\)")→[1,∞), defined by _f_ ( _x_ ) = _x_ − log2( _x_ ). It is
[strictly increasing](/wiki/Strictly_increasing "Strictly increasing") on its
domain, and hence has an inverse _f_ -1:[1,∞)→[2,∞).

Define _n_ 0 = _f_ -1( _U_ )+1.

Then no proof of the form " _K_ ( _s_ )≥ _L_ " with _L_ ≥ _n_ 0 can be
obtained in **S** , as can be seen by an [indirect
argument](/wiki/Indirect_argument "Indirect argument"): If
`ComplexityLowerBoundNthProof(i)` could return a value ≥ _n_ 0, then the loop
inside `GenerateProvablyComplexString` would eventually terminate, and that
procedure would return a string _s_ such that

| _K_ ( _s_ )  
---|---  
≥ | _n_ 0 |  | by construction of `GenerateProvablyComplexString`  
> | _U_ +log2( _n_ 0) |  | since _n_ 0 > _f_ -1( _U_ ) implies _n_ 0 − log2(
> _n_ 0) = _f_ ( _n_ 0) > _U_  
≥ | _K_ ( _s_ ) |  | since _s_ was described by the program with that length  
  
This is a contradiction, [Q.E.D.](/wiki/Q.E.D. "Q.E.D.")

As a consequence, the above program, with the chosen value of _n_ 0, must loop
forever.

Similar ideas are used to prove the properties of [Chaitin's
constant](/wiki/Chaitin%27s_constant "Chaitin's constant").

## Minimum message
length[[edit](/w/index.php?title=Kolmogorov_complexity&action=edit&section=12
"Edit section: Minimum message length")]

The minimum message length principle of statistical and inductive inference
and machine learning was developed by [C.S.
Wallace](/wiki/Chris_Wallace_\(computer_scientist\) "Chris Wallace \(computer
scientist\)") and D.M. Boulton in 1968. MML is
[Bayesian](/wiki/Bayesian_probability "Bayesian probability") (i.e. it
incorporates prior beliefs) and information-theoretic. It has the desirable
properties of statistical invariance (i.e. the inference transforms with a re-
parametrisation, such as from polar coordinates to Cartesian coordinates),
statistical consistency (i.e. even for very hard problems, MML will converge
to any underlying model) and efficiency (i.e. the MML model will converge to
any true underlying model about as quickly as is possible). C.S. Wallace and
D.L. Dowe (1999) showed a formal connection between MML and algorithmic
information theory (or Kolmogorov complexity).[14]

## Kolmogorov
randomness[[edit](/w/index.php?title=Kolmogorov_complexity&action=edit&section=13
"Edit section: Kolmogorov randomness")]

_Kolmogorov randomness_ defines a string (usually of [bits](/wiki/Bit "Bit"))
as being [random](/wiki/Randomness "Randomness") if and only if it is shorter
than any [computer program](/wiki/Computer_program "Computer program") that
can produce that string. To make this precise, a [universal
computer](/wiki/Universal_Turing_machine "Universal Turing machine") (or
universal Turing machine) must be specified, so that "program" means a program
for this universal machine. A random string in this sense is "incompressible"
in that it is impossible to "compress" the string into a program whose length
is shorter than the length of the string itself. A [counting
argument](/wiki/Counting_argument "Counting argument") is used to show that,
for any universal computer, there is at least one algorithmically random
string of each length. Whether any particular string is random, however,
depends on the specific universal computer that is chosen.

This definition can be extended to define a notion of randomness for
_infinite_ sequences from a finite alphabet. These [algorithmically random
sequences](/wiki/Algorithmically_random_sequence "Algorithmically random
sequence") can be defined in three equivalent ways. One way uses an effective
analogue of [measure theory](/wiki/Measure_theory "Measure theory"); another
uses effective [martingales](/wiki/Martingale_\(probability_theory\)
"Martingale \(probability theory\)"). The third way defines an infinite
sequence to be random if the prefix-free Kolmogorov complexity of its initial
segments grows quickly enough — there must be a constant _c_ such that the
complexity of an initial segment of length _n_ is always at least _n_ − _c_.
This definition, unlike the definition of randomness for a finite string, is
not affected by which universal machine is used to define prefix-free
Kolmogorov complexity.[15]

## Relation to
entropy[[edit](/w/index.php?title=Kolmogorov_complexity&action=edit&section=14
"Edit section: Relation to entropy")]

For dynamical systems, entropy rate and algorithmic complexity of the
trajectories are related by a theorem of Brudno, that the equality K(x;T) =
h(T) holds for almost all x.[16]

It can be shown[17] that for the output of [Markov information
sources](/wiki/Markov_information_source "Markov information source"),
Kolmogorov complexity is related to the
[entropy](/wiki/Entropy_\(information_theory\) "Entropy \(information
theory\)") of the information source. More precisely, the Kolmogorov
complexity of the output of a Markov information source, normalized by the
length of the output, converges almost surely (as the length of the output
goes to infinity) to the [entropy](/wiki/Entropy_\(information_theory\)
"Entropy \(information theory\)") of the source.

## Conditional
versions[[edit](/w/index.php?title=Kolmogorov_complexity&action=edit&section=15
"Edit section: Conditional versions")]

[![\[icon\]](//upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Wiki_letter_w_cropped.svg/20px-
Wiki_letter_w_cropped.svg.png)](/wiki/File:Wiki_letter_w_cropped.svg)|

This section

**needs expansion**

.

You can help by [adding to
it](https://en.wikipedia.org/w/index.php?title=Kolmogorov_complexity&action=edit&section=).
_( July 2014)_  
  
---|---  
  
The conditional Kolmogorov complexity of two strings  K ( x | y )
{\displaystyle K(x|y)} ![{\\displaystyle
K\(x|y\)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/93d70e70ae35d7640bbc98a6042641e75b49f507)
is, roughly speaking, defined as the Kolmogorov complexity of _x_ given _y_ as
an auxiliary input to the procedure.[18][19]

There is also a length-conditional complexity  K ( x | L ( x ) )
{\displaystyle K(x|L(x))} ![{\\displaystyle
K\(x|L\(x\)\)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/12a0a546f451972d5e5127746d5574de65e1db9b),
which is the complexity of _x_ given the length of _x_ as known/input.[20][21]

## See
also[[edit](/w/index.php?title=Kolmogorov_complexity&action=edit&section=16
"Edit section: See also")]

  1. **^** However, an _s_ with _K_ ( _s_ ) = _n_ need not exist for every _n_. For example, if _n_ is not a multiple of 7 bits, no [ASCII](/wiki/ASCII "ASCII") program can have a length of exactly _n_ bits.
  2. **^** There are 1 + 2 + 22 \+ 23 \+ ... + 2 _n_ = 2 _n_ +1 − 1 different program texts of length up to _n_ bits; cf. [geometric series](/wiki/Geometric_series "Geometric series"). If program lengths are to be multiples of 7 bits, even fewer program texts exist.
  3. **^** By the previous theorem, such a string exists, hence the `for` loop will eventually terminate.
  4. **^** including the language interpreter and the subroutine code for `KolmogorovComplexity`
  5. **^** If `KolmogorovComplexity` has length _n_ bits, the constant _m_ used in `GenerateComplexString` needs to be adapted to satisfy _n_ \+ 1400000 \+ 1218 \+ 7·log10( _m_ ) < _m_ , which is always possible since _m_ grows faster than log10( _m_ ).
  6. **^** As there are _N_ _L_ = 2 _L_ strings of length _L_ , the number of strings of lengths _L_ = 0, 1, …, _n_ − 1 is _N_ 0 \+ _N_ 1 \+ … + _N_ _n_ −1 = 20 \+ 21 \+ … + 2 _n_ −1, which is a finite [geometric series](/wiki/Geometric_series "Geometric series") with sum 20 \+ 21 \+ … + 2 _n_ −1 = 20 × (1 − 2 _n_ ) / (1 − 2) = 2 _n_ − 1

##
References[[edit](/w/index.php?title=Kolmogorov_complexity&action=edit&section=18
"Edit section: References")]

  1. **^** [Kolmogorov, Andrey](/wiki/Andrey_Kolmogorov "Andrey Kolmogorov") (1963). "On Tables of Random Numbers". _Sankhyā Ser. A_. **25** : 369–375. [MR](/wiki/MR_\(identifier\) "MR \(identifier\)") [0178484](//www.ams.org/mathscinet-getitem?mr=0178484).
  2. **^** [Kolmogorov, Andrey](/wiki/Andrey_Kolmogorov "Andrey Kolmogorov") (1998). "On Tables of Random Numbers". _Theoretical Computer Science_. **207** (2): 387–395. [doi](/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1016/S0304-3975(98)00075-9](https://doi.org/10.1016%2FS0304-3975%2898%2900075-9). [MR](/wiki/MR_\(identifier\) "MR \(identifier\)") [1643414](//www.ams.org/mathscinet-getitem?mr=1643414).
  3. **^** [Solomonoff, Ray](/wiki/Ray_Solomonoff "Ray Solomonoff") (February 4, 1960). ["A Preliminary Report on a General Theory of Inductive Inference"](http://world.std.com/~rjs/rayfeb60.pdf) (PDF). _Report V-131_. [revision](http://world.std.com/~rjs/z138.pdf), Nov., 1960.
  4. **^** Solomonoff, Ray (March 1964). ["A Formal Theory of Inductive Inference Part I"](http://world.std.com/~rjs/1964pt1.pdf) (PDF). _Information and Control_. **7** (1): 1–22. [doi](/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1016/S0019-9958(64)90223-2](https://doi.org/10.1016%2FS0019-9958%2864%2990223-2).
  5. **^** Solomonoff, Ray (June 1964). ["A Formal Theory of Inductive Inference Part II"](http://world.std.com/~rjs/1964pt2.pdf) (PDF). _Information and Control_. **7** (2): 224–254. [doi](/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1016/S0019-9958(64)90131-7](https://doi.org/10.1016%2FS0019-9958%2864%2990131-7).
  6. **^** Kolmogorov, A.N. (1965). ["Three Approaches to the Quantitative Definition of Information"](https://web.archive.org/web/20110928032821/http://www.ece.umd.edu/~abarg/ppi/contents/1-65-abstracts.html). _Problems Inform. Transmission_. **1** (1): 1–7. Archived from [the original](http://www.ece.umd.edu/~abarg/ppi/contents/1-65-abstracts.html#1-65.2) on September 28, 2011.
  7. **^** Chaitin, Gregory J. (1969). "On the Simplicity and Speed of Programs for Computing Infinite Sets of Natural Numbers". _Journal of the ACM_. **16** (3): 407–422. [CiteSeerX](/wiki/CiteSeerX_\(identifier\) "CiteSeerX \(identifier\)") [10.1.1.15.3821](//citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.15.3821). [doi](/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1145/321526.321530](https://doi.org/10.1145%2F321526.321530).
  8. **^** Kolmogorov, A. (1968). "Logical basis for information theory and probability theory". _IEEE Transactions on Information Theory_. **14** (5): 662–664. [doi](/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1109/TIT.1968.1054210](https://doi.org/10.1109%2FTIT.1968.1054210).
  9. **^** Li, Ming; Vitányi, Paul (2008). "Preliminaries". [_An Introduction to Kolmogorov Complexity and its Applications_](https://archive.org/details/introductiontoko00limi_695). Texts in Computer Science. pp. [1](https://archive.org/details/introductiontoko00limi_695/page/n23)–99. [doi](/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1007/978-0-387-49820-1_1](https://doi.org/10.1007%2F978-0-387-49820-1_1). [ISBN](/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-0-387-33998-6](/wiki/Special:BookSources/978-0-387-33998-6 "Special:BookSources/978-0-387-33998-6").
  10. **^** Burgin, M. (1982), "Generalized Kolmogorov complexity and duality in theory of computations", _Notices of the Russian Academy of Sciences_ , v.25, No. 3, pp. 19–23.
  11. **^** Stated without proof in: ["Course notes for Data Compression - Kolmogorov complexity"](http://www.daimi.au.dk/~bromille/DC05/Kolmogorov.pdf) [Archived](https://web.archive.org/web/20090909132048/http://www.daimi.au.dk/~bromille/DC05/Kolmogorov.pdf) 2009-09-09 at the [Wayback Machine](/wiki/Wayback_Machine "Wayback Machine"), 2005, P. B. Miltersen, p.7
  12. **^** Zvonkin, A.; L. Levin (1970). ["The complexity of finite objects and the development of the concepts of information and randomness by means of the theory of algorithms"](http://alexander.shen.free.fr/library/Zvonkin_Levin_70.pdf) (PDF). _Russian Mathematical Surveys_. **25** (6). pp. 83–124.
  13. **^** Gregory J. Chaitin (Jul 1974). ["Information-theoretic limitations of formal systems"](http://www.cas.mcmaster.ca/~sancheg/EE_UCU2006_thesis/biblio/Information-theoretic%20limitations%20of%20Formal%20Systems%20\(acm74\).pdf) (PDF). _Journal of the ACM_. **21** (3): 403–434. [doi](/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1145/321832.321839](https://doi.org/10.1145%2F321832.321839).
  14. **^** Wallace, C. S.; Dowe, D. L. (1999). "Minimum Message Length and Kolmogorov Complexity". _Computer Journal_. **42** (4): 270–283. [CiteSeerX](/wiki/CiteSeerX_\(identifier\) "CiteSeerX \(identifier\)") [10.1.1.17.321](//citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.17.321). [doi](/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1093/comjnl/42.4.270](https://doi.org/10.1093%2Fcomjnl%2F42.4.270).
  15. **^** Martin-Löf, Per (1966). "The definition of random sequences". _Information and Control_. **9** (6): 602–619. [doi](/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1016/s0019-9958(66)80018-9](https://doi.org/10.1016%2Fs0019-9958%2866%2980018-9).
  16. **^** Galatolo, Stefano; Hoyrup, Mathieu; Rojas, Cristóbal (2010). ["Effective symbolic dynamics, random points, statistical behavior, complexity and entropy"](http://www.loria.fr/~hoyrup/random_ergodic.pdf) (PDF). _Information and Computation_. **208** : 23–41. [doi](/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1016/j.ic.2009.05.001](https://doi.org/10.1016%2Fj.ic.2009.05.001).
  17. **^** Alexei Kaltchenko (2004). "Algorithms for Estimating Information Distance with Application to Bioinformatics and Linguistics". [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[cs.CC/0404039](//arxiv.org/abs/cs.CC/0404039).
  18. **^** Jorma Rissanen (2007). [_Information and Complexity in Statistical Modeling_](https://archive.org/details/informationcompl00riss_364). Springer S. p. [53](https://archive.org/details/informationcompl00riss_364/page/n59). [ISBN](/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-0-387-68812-1](/wiki/Special:BookSources/978-0-387-68812-1 "Special:BookSources/978-0-387-68812-1").
  19. **^** Ming Li; Paul M.B. Vitányi (2009). [_An Introduction to Kolmogorov Complexity and Its Applications_](https://archive.org/details/introductiontoko00limi_695). Springer. pp. [105](https://archive.org/details/introductiontoko00limi_695/page/n127)–106. [ISBN](/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-0-387-49820-1](/wiki/Special:BookSources/978-0-387-49820-1 "Special:BookSources/978-0-387-49820-1").
  20. **^** Ming Li; Paul M.B. Vitányi (2009). [_An Introduction to Kolmogorov Complexity and Its Applications_](https://archive.org/details/introductiontoko00limi_695). Springer. p. [119](https://archive.org/details/introductiontoko00limi_695/page/n141). [ISBN](/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-0-387-49820-1](/wiki/Special:BookSources/978-0-387-49820-1 "Special:BookSources/978-0-387-49820-1").
  21. **^** Vitányi, Paul M.B. (2013). ["Conditional Kolmogorov complexity and universal probability"](https://ir.cwi.nl/pub/26818). _Theoretical Computer Science_. **501** : 93–100. [arXiv](/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[1206.0983](//arxiv.org/abs/1206.0983). [doi](/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1016/j.tcs.2013.07.009](https://doi.org/10.1016%2Fj.tcs.2013.07.009).

## Further
reading[[edit](/w/index.php?title=Kolmogorov_complexity&action=edit&section=19
"Edit section: Further reading")]

  * [Blum, M.](/wiki/Manuel_Blum "Manuel Blum") (1967). "On the size of machines". _Information and Control_. **11** (3): 257. [doi](/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1016/S0019-9958(67)90546-3](https://doi.org/10.1016%2FS0019-9958%2867%2990546-3).
  * Brudno, A. (1983). "Entropy and the complexity of the trajectories of a dynamical system". _Transactions of the Moscow Mathematical Society_. **2** : 127–151.
  * Cover, Thomas M.; Thomas, Joy A. (2006). _Elements of information theory_ (2nd ed.). Wiley-Interscience. [ISBN](/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [0-471-24195-4](/wiki/Special:BookSources/0-471-24195-4 "Special:BookSources/0-471-24195-4").
  * Lajos, Rónyai; Gábor, Ivanyos; Réka, Szabó (1999). _Algoritmusok_. TypoTeX. [ISBN](/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [963-279-014-6](/wiki/Special:BookSources/963-279-014-6 "Special:BookSources/963-279-014-6").
  * Li, Ming; Vitányi, Paul (1997). _An Introduction to Kolmogorov Complexity and Its Applications_. Springer. [ISBN](/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-0387339986](/wiki/Special:BookSources/978-0387339986 "Special:BookSources/978-0387339986").CS1 maint: ref=harv ([link](/wiki/Category:CS1_maint:_ref%3Dharv "Category:CS1 maint: ref=harv"))
  * Yu, Manin (1977). [_A Course in Mathematical Logic_](https://archive.org/details/courseinmathemat0000bell). Springer-Verlag. [ISBN](/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-0-7204-2844-5](/wiki/Special:BookSources/978-0-7204-2844-5 "Special:BookSources/978-0-7204-2844-5").
  * Sipser, Michael (1997). [_Introduction to the Theory of Computation_](https://archive.org/details/introductiontoth00sips). PWS. [ISBN](/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [0-534-95097-3](/wiki/Special:BookSources/0-534-95097-3 "Special:BookSources/0-534-95097-3").

## External
links[[edit](/w/index.php?title=Kolmogorov_complexity&action=edit&section=20
"Edit section: External links")]

