# k0rdent documentation style guide

This page gives style guidance to our Markdown, and makes some general recommendations regarding writing style for docs. It is _not_ a complete style guide. In most cases, Project k0rdent aspires to follow style recommendations adopted by the Kubernetes Project's SIG Docs group. Please see the [Kubernetes Documentation Style Guide](https://kubernetes.io/docs/contribute/style/style-guide/) for details.

If you are looking for technical recommendations about how to contribute to docs, these are found in the [k0rdent Documentation Contributors Guide](k0rdent-documentation-contributors-guide.md).

## Our Markdown style, theme, and extensions

k0rdent docs uses:

* The [MkDocs](https://www.mkdocs.org/) static site generator.
* The [Material theme](https://squidfunk.github.io/mkdocs-material/) for MkDocs.

... plus other extensions and plugins that have less of an effect on how you write documentation. Versions of all components are in the file [`requirements.txt`](https://github.com/k0rdent/docs/blob/main/requirements.txt) at toplevel in k0rdent/docs.

At present, we are mostly utilizing pure CommonMark with certain Material theme extensions (see below), though we are experimenting with other plugins and extensions.

## CommonMark basics

If you don't know Markdown already, [CommonMark](https://commonmark.org) is a strongly-defined specification of Markdown with unambiguous syntax, plus a suite of tests to validate Markdown implementations against the specification. It's used in MkDocs and (with some iffyness around the edges) GitHub, which means our docs are readable when we use MkDocs to render them into static pages for display on the web, and also readable (in most cases) when you surf GitHub and look at the render there.

Comfortingly, the CommonMark spec is very similar to whatever version(s) of Markdown you already know (e.g., GitHub-flavored Markdown) as well as allied structured-text specifications that share DNA with Markdown, like ReStructuredText (.rst), commonly used in open source docs environments.

Some resources you may find useful:

* [CommonMark Markdown Reference](https://commonmark.org/help/)
* [CommonMark Markdown Tutorial](https://commonmark.org/help/tutorial/)

## Admonitions

For the moment, we're coming up to speed with a modern solution for admonitions, but meanwhile are using the OG CommonMark form of 'notes are blockquotes with special headers, rendered prettily by MkDocs. Examples:

```
>NOTE:
>This is a note.
>It can go over several lines as needed, and can contain `code`, **boldface**, _italics_, and other body-copy Markdown elements.

>INFO:
>This is an info box.
>It can go over several lines as needed, and can contain `code`, **boldface**, _italics_, and other body-copy Markdown elements.

>CAUTION:
>This is a cautionary admonishment.
>It can go over several lines as needed, and can contain `code`, **boldface**, _italics_, and other body-copy Markdown elements.

>WARNING:
>This is a warning.
>It can go over several lines as needed, and can contain `code`, **boldface**, _italics_, and other body-copy Markdown elements.
```

>NOTE:
>This is a note.
>It can go over several lines as needed, and can contain `code`, **boldface**, _italics_, and other body-copy Markdown elements.

>INFO:
>This is an info box.
>It can go over several lines as needed, and can contain `code`, **boldface**, _italics_, and other body-copy Markdown elements.

>CAUTION:
>This is a cautionary admonishment.
>It can go over several lines as needed, and can contain `code`, **boldface**, _italics_, and other body-copy Markdown elements.

>WARNING:
>This is a warning.
>It can go over several lines as needed, and can contain `code`, **boldface**, _italics_, and other body-copy Markdown elements.




