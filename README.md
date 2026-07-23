# k0rdent Documentation

The home of the consolidated documentation for k0rdent sponsored by Mirantis.

[k0rdent Docs](https://k0rdent.github.io/docs)

This project utilises Mkdocs with the Material theme and Mermaid for
diagrams. Currently the docs are published using github actions on github pages
from the branch gh-pages.

Development is tracked under [k0rdent](https://github.com/orgs/k0rdent/projects/4) on github.

The k0rdent org is:

- [k0rdent](https://github.com/k0rdent)

The related k0rdent repositories can be found as follows:

- [k0rdent Cluster Manager (kcm)](https://github.com/k0rdent/kcm)
- [k0rdent Observability and FinOps (kof)](https://github.com/k0rdent/kof)
- [k0rdent Documentation Source (docs)](https://github.com/k0rdent/docs)
- [k0rdent Community Documentation](https://github.com/k0rdent/community)



## Project layout

```
mkdocs.yml    # The configuration file.
docs/
    index.md  # The documentation homepage.
    stylesheets  # CSS stylesheets to control look and feel
    assets  # Images and other served material
    ...       # Other markdown pages, images and other files.
```



## Setting up MKdocs and dependancies

1. Setup python Virtual Environment
  ```bash
    python3 -m venv ./mkdocs
    source ./mkdocs/bin/activate
  ```
2. Install MkDocs
  ```bash
    pip install mkdocs
  ```
3. Install plugins
  ```bash
    pip install mkdocs-mermaid2-plugin
    pip install mkdocs-material
    pip install markdown-callouts
  ```



## Run MKdocs for dev

- Start the live-reloading docs server.

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## MKdocs Commands

- `mkdocs new [dir-name]` - Create a new project.
- `mkdocs build` - Build the documentation site.
- `mkdocs -h` - Print help message and exit.



# Documentation Standards

By default, we follow the [Kubernetes documentation style guide](https://kubernetes.io/docs/contribute/style/style-guide/). 

## Header Capitalization

All header text should be capitalized.

## Embedding videos

Videos and large animated gif files should not be stored in the repository. Instead, they should be stored in the [`Mirantis Docs` shared drive](https://drive.google.com/drive/u/0/folders/0ABalyEh44hkqUk9PVA). If you don't have access to this drive, add the asset file to the PR and note it in the description.  To add the video to the page, use this format:

```
<iframe  src="https://drive.google.com/file/d/<FILE_ID>/preview" style="aspect-ratio: <HEIGHT> / <WIDTH>;"      allow="autoplay" allowfullscreen></iframe>
```

You can retrieve the `FILE_ID` of the video or gif by choosing **Share**-->**Copy URL** for the video on Google Drive and extracting it from the URL.  For example, the `FILE_ID` for:

```
https://drive.google.com/file/d/1MrCs07LGN5LPD4stktwC5sv0PB8HclTa/view?usp=sharing
```

is 

```
1MrCs07LGN5LPD4stktwC5sv0PB8HclTa
```

If necessary, you can get the `HEIGHT` and `WIDTH` values by previewing the video and choosing **File**-->**Details**-->**Dimensions**.

## Referencing Kubernetes nested resources

Please use the dot notation.  So in the following:

```
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
```

To refer to the `name` field, please use `.metadata.name` and not `name`.