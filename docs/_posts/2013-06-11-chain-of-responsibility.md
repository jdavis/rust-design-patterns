---
layout: default
title: Chain of Responsibility
category: behavioral
description: The Chain of Responsibility design pattern in the Rust programming language with an example.
css:
    - /css/code.css
    - /lib/lightbox/css/lightbox.css
js:
    - //ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js
    - /lib/lightbox/js/lightbox.js
---

{{ page.title }}
================

## Definition

Avoid coupling the sender of a request to its receiver by giving more than one
object a chance to handle the request. Chain the receiving objects and pass the
request along the chain until an object handles it.

## Diagram

<div class="gallery medium">
    <a href="{{ site.url }}/img/chain-of-responsibility-structure.png" rel="lightbox"
    title="Structure of the Chain of Responsibility pattern">
        <img src="{{ site.url }}/img/chain-of-responsibility-structure.png" width="620">
        <span>Structure of the Chain of Responsibility pattern</span>
    </a>
</div>

## Problem

TODO

## Wrong Solution

TODO

## Correct Solution

TODO

## Example

TODO

### Example Diagram

TODO

### Example Code

View [chain_of_responsibility.rs][github] on GitHub

{% highlight rust %}

// TODO

{% endhighlight %}

[github]: https://github.com/jdavis/rust-design-patterns/blob/master/patterns/chain_of_responsibility.rs
