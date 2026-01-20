To generate docs/reference/crd/index.md call:

KCM_REF=v<vernum> make -C crdgen api-docs

from to repo root.

Once the file is generated, use regex to replace:

<td\b[^>]*>\s*<b\b[^>]*>\s*<a\b[^>]*href="#[^"]+"[^>]*>(.*?)</a>\s*</b>\s*</td>

with 

<td><b>$1</b></td>

and remove:

<sup\b[^>]*>\s*<sup\b[^>]*>\s*\[\s*↩\s*Parent\s*\]\(([^)]+)\)\s*</sup>\s*</sup>

altogether.

Also remove all valpha1 content.
