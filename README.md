# retrolink

retrolink restores external links in old web sites (such as blogs). It
will find all links in a web page, and convert all links to archive.org
links that point to the closest time to when the post was written.

This should be used when wayback machine doesn't already have a snapshot
of your webpage at the intended time.

## Usage

retrolink can be used as a CLI (for fixing links as makers) or as a
webapp (for viewing webpages with broken/stale links).

Clone this repository and install retrolink with pip.
This has been tested with Python 3.10.

```
$ git clone https://github.com/nikochiko/retrolink
...
$ cd retrolink
$ python3 setup.py develop
$ rl version
0.1.0
```

### CLI

```
$ cat my-old-writing.md | rl --strategy=meta.publish_date > my-old-writing-with-robust-links.md
```

### Webapp

```
$ rl web
```

In the UI, enter URL and intended date (will default to `meta.publish_date`).

### LICENSE

MIT License. See [LICENSE](./LICENSE)
