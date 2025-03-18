# k0rdent documentation contributors' guide

k0rdent documentation is growing rapidly, and community members are very welcome to contribute by filing pull requests against documents in this repository. Thank you for your interest in k0rdent!

This page gives technical guidance for contributing to k0rdent documentation. The [k0rdent documentation style guide](k0rdent-documentation-style-guide.md) details our markdown style and provides general recommendations for writing style.

## How k0rdent docs are built

k0rdent documentation is built from Markdown (.md) documents using the [MkDocs](https://www.mkdocs.org/) static site generator with the [Material](https://squidfunk.github.io/mkdocs-material/) theme. We use several MkDocs extensions and plugins for rendering glossary items, admonitions (e.g., Note, Tip, Warning, etc.) and other special kinds of content.

Below you'll find [instructions for setting up MkDocs locally](#install-mkdocs-to-view-k0rdent-docs-locally) to dynamically build and serve the k0rdent documentation from your local clone of the docs repository. This is handy for reviewing the rendered look and feel of changes and additions before filing a pull request.

## How k0rdent docs are written

k0rdent documentation is written mostly in [CommonMark](https://commonmark.org/) as adopted by GitHub, with a few CommonMark-compatible markdown enhancements used by MkDocs, the Material theme, and extensions (see below) to enable more-readable rendering of code, glossary items, images, and admonitions (e.g., NOTE:, TIP:, WARNING:, etc.). The [k0rdent documentation style guide](k0rdent-documentation-style-guide.md) details our markdown style, along with those extensions.

## How k0rdent docs is structured

The structure of k0rdent/docs is shown below:

```console
docs                                                # repository containing folder /docs
├── docs                                            # subdirectory for /docs, containing further subdirectories for assets, images, theme, etc.
│   ├── assets                                      # illustrations for docs
│   ├── css                                         # css stylesheets
│   ├── custom_theme                                # Material theme customizations
│   ├── img                                         # site imagery (logos, icons, etc.)
│   ├── stylesheets                                 # extra CSS stylesheets
│   ├── index.md                                    # default homepage of the docs site
│   ├── LICENSE                                     # k0rdent docs license (CC-BY-4.0)
│   ├── (documentation-files.md)                    # actual docs pages (markdown documents)
├── mkdocs.yml                                      # main configuration file for mkdocs, specifies site navigation and table of contents
├── requirements.txt                                # mkdocs requirements (for installation with pip for building docs locally - see below)
├── Dockerfile                                      # Dockerfile for building a container to serve docs interactively
├── .gitignore                                      # Things to ignore when people push
└── .github                                         # Special GitHub features, including allowed-patterns.yml for placeholders replacing secrets
```

   > NOTE:
   > The k0rdent documentation repository is called `docs` and cloning the repo will create a containing directory called `docs`.
   > This directory itself contains a subdirectory `/docs` which contains Markdown (.md) doc files and related subdirectories like
   > /assets, /img, etc. Do not confuse toplevel docs with subdirectory /docs.

## Raising issues

If you find issues (errors, omissions, etc.) with k0rdent documentation, we would be very grateful if you would notify us by [creating an issue](https://github.com/k0rdent/docs/issues).

## Contributing to k0rdent docs - simplest way: use GitHub's webUI

For making small corrections to k0rdent docs, the simplest tool is GitHub's website. You will need a personal (free) or business GitHub account.

1. Familiarize yourself with the [structure of the `k0rdent/docs` repo](#how-k0rdent-docs-is-structured).
2. Figure out where the doc you want to update lives, or where a new doc you create might need to live.
3. Visit the k0rdent/docs repo itself. Search for `k0rdent/docs` or click the following link: ([https://github.com/k0rdent/docs](https://github.com/k0rdent/docs))
4. To propose changes to existing docs: On k0rdent/docs, edit the doc you want to change, using the pencil icon (Edit) button in the upper right of GitHub's webUI. This will create a fork of k0rdent/docs in your own account's workspace (if you don't already have your own fork) and create a new feature branch, from which your proposed update will be submitted to k0rdent/docs as a pull request (PR).
5. To create new docs (or propose changes to existing docs): Create a fork of k0rdent/docs in your own account workspace using the Fork button in the upper right of k0rdent/docs. Navigate to the directory in which you want to create your new doc (or go to the directory in which the doc you want to edit lives). Click Add File>Create New File to add a new blank doc, upload an image or other file, or find and edit the doc you want to change.
6. When your edit(s) are complete, click Commit Changes in the upper right.
7. Write a descriptive commit message so project k0rdent docs maintainers understand your proposed addition or change.
8. Click Propose Change.
9. On the next screen, compare your change with content originally there.
10. Click Create Pull Request.

Maintainers will see your pull request and may request discussion or suggest further changes, or they may merge your change. You'll be notified via GitHub either way.

## Making regular contributions - use Git on the desktop

For making regular or at-scale contributions to k0rdent documentation, we recommend using a standard open source workflow as follows:

1. Create a fork of k0rdent/docs in your own GitHub workspace.
2. Clone your fork to your desktop using git.
3. Set origin remotes (fetch, push) to your fork.
4. Set upstream remotes (fetch, push) to k0rdent/docs (main)

Then, when getting ready to work:

5. Update your local main from upstream and update main on your fork on GitHub:

```shell  
git checkout main && git fetch upstream && git pull upstream main && git push origin main
```

6. Create a new feature branch for each intended commit, to isolate your changes:

```shell
git checkout -b my-feature-branch main
```

7. As needed, particularly if you work on a change for a long time, periodically update your feature branch from upstream main to avoid later conflicts:
   
```shell
git checkout my-feature-branch && git pull --rebase upstream main
```

8. When finished editing, add and commit changes:

```shell
git add . && git commit -m "My changes"
```

9. Pre-emptively update once more before pushing:

```shell
git fetch upstream && git rebase upstream/main
```

10. Push your feature branch to your fork on GitHub:

```shell
git push origin my-feature-branch
```

This will cause Git to display a confirmation message containing a link you can follow to submit a pull request on GitHub, from your feature branch to k0rdent/docs (main).

11. Follow the link. Compare changes. Write an informative pull request title and extended description. And submit your Pull Request. Thank you in advance!

## Install MkDocs to view k0rdent docs locally

When making docs contributions or edits, it can be very helpful to run MkDocs on your desktop, so you can see your additions and changes as they will be rendered online.

MkDocs can be run on almost any contemporary Linux environment, desktop or server, inside a container, or on MacOS, Windows, or WSL. It requires recent (in k0rdent's case, 3.9+) versions of Python and pip. So this should work in whatever desktop environment you use: alongside Git and your Markdown editor or IDE.

   > NOTE:
   > k0rdent's MkDocs environment requires Python 3.9+ and a corresponding version of pip. 

Assuming you have a machine (desktop, laptop, VM) for editing with recent (Python 3.9+) versions of Python and pip:

1. Begin by creating a fork of k0rdent/docs on GitHub, and clone your fork to your machine. See [Making regular contributions - use Git on the desktop](#making-regular-contributions-use-git-on-the-desktop)

2. Switch into the cloned project directory on your machine:
   
```shell
cd docs
```

3. Create a venv into which to install MkDocs and dependencies, saved in the /docs repo in a file called `requirements.txt`.

```shell
python3 -m venv venv
source venv/bin/activate
```

   Your terminal should now show `(venv)` in the prompt. This will create a local /venv folder in your copy of the repo, which the
   .gitignore already in your clone will instruct GitHub to ignore when you make commits and file pull requests. 

4. Install MkDocs and dependencies in the venv, using `requirements.txt`.

    > NOTE:
    > The file `requirements.txt` is in the toplevel containing folder (called `docs`) &mdash; not in the `/docs` subfolder
    > within the toplevel directory.
   
```shell
pip install -r requirements.txt 
```

Once you've done this, you can execute MkDocs to dynamically build and serve docs locally on localhost (`http://127.0.0.1:8000`):

```shell
python3 mkdocs serve
```

Then just visit localhost (`http://127.0.0.1:8000`) in a browser to view and navigate the docs.

## Run MkDocs in a container to view k0rdent docs locally

If you prefer, you can also run MkDocs in a container on your machine to view k0rdent docs locally. This is another way of keeping the MkDocs environment isolated and easily removable.

We've put a Dockerfile in the toplevel directory of the repo to help with this. Here's what's in that Dockerfile:

```shell
# Use the official MkDocs Material image
FROM squidfunk/mkdocs-material:latest

# Set the working directory
WORKDIR /docs

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy MkDocs files
COPY mkdocs.yml .

# Expose the MkDocs server port
EXPOSE 8000
```

As you can see, we're using the official MkDocs Material base image. The Dockerfile creates a working directory called /docs, installs requirements.txt with pip, copies in the mkdocs.yml configuration file, and exposes port 8000 so the container can be accessed as localhost on your machine.

1. You'll need Docker installed on your machine. Follow instructions [here](https://docs.docker.com/engine/install/)
2. Go to the toplevel directory of the repo, where the Dockerfile and mkdocs.yml reside.
3. Build the container, tagging it with the name `mk-local`.

```shell
docker build -f Dockerfile -t mk-local
```

4. Then use git to (optionally create and/or) checkout the branch you'll be working in, since this is the branch you want MkDocs to render from.

```shell
git checkout -b my-working-branch       # create and checkout new working branch, or ...
git checkout my-working-branch          # checkout existing working branch
```

5. Open a new terminal (so you can stop the container within this terminal window by pressing CTRL-C later), then run the container like this:

```shell
docker run --rm -it -p 8000:8000 -v ${PWD}:/docs mk-local
```

This ensures that the container is removed when you're finished with it, that it launches as interactive and with a TTY, that the container's port 8000 is mapped to port 8000 on your local machine (enabling you to view the container on localhost - `http://127.0.0.1:8000`), and it mounts your current directory (the toplevel of the repo) as /docs inside the container. This lets MkDocs see your local copy of the repo to render and serve it to the browser, and refreshes each time you make a change.

Just visit the container on `http://127.0.0.1:8000` to view the docs.

6. When you want to stop the container, press CTRL+C inside the terminal window used to start it. Alternatively, you can stop the container from any terminal as follows:

```shell
docker ps                       # find the container ID, then ...
docker stop <container-id>      # stop the container
```

Because we started the container with the --rm flag, it will be removed from Docker Engine when it stops. Restart by once again entering:

```shell
docker run --rm -it -p 8000:8000 -v ${PWD}:/docs mk-local
```

