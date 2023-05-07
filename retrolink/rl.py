import re
from datetime import datetime
from urllib.parse import urljoin, urlparse

from dateutil.parser import isoparse

# we don't need to handle non-ascii domain names separately
# ref: https://www.charset.org/punycode
url_pattern = re.compile(r"(?<=(?:href=(?:\"|')))(.+?)(?=(?:\"|'))", re.IGNORECASE)
relative_url_pattern = re.compile(r"(?<=(?:href=(?:\"|')))(/.+?)(?=(?:\"|'))|(?<=(?:src=(?:\"|')))(/.+?)(?=(?:\"|'))", re.IGNORECASE)

# ref: https://stackoverflow.com/questions/3143070/regex-to-match-an-iso-8601-datetime-string/58878432
iso_date_pattern = re.compile(r"(\d{4}-[01]\d-[0-3]\dT[0-2]\d:[0-5]\d:[0-5]\d\.\d+([+-][0-2]\d:[0-5]\d|Z))|(\d{4}-[01]\d-[0-3]\dT[0-2]\d:[0-5]\d:[0-5]\d([+-][0-2]\d:[0-5]\d|Z))|(\d{4}-[01]\d-[0-3]\dT[0-2]\d:[0-5]\d([+-][0-2]\d:[0-5]\d|Z))")

html_body_pattern = re.compile("<body[^>]*>((.|[\n\r])*)<\/body>", re.IGNORECASE)


def fix_html(content: str, url: str = "") -> str:
    result = html_body_pattern.sub(
        lambda match: fix_links(match.group(1), when=guess_publish_date(content), base_url=url),
        content,
    )
    result = relative_url_pattern.sub(
        lambda match: make_absolute(match.group(1) or match.group(2), base=url),
        result,
    )
    return result


def fix_generic(content: str, url: str = "") -> str:
    return fix_links(content, when=guess_publish_date(content), base_url=url)


def guess_publish_date(content: str) -> datetime:
    """
    Use regex to get the first date-like string in content
    If not found, fallback to today.

    This will likely return the date in a meta tag for
    `article:published_time`, but I'm too lazy to go through
    that exercise.
    """
    maybe_date = iso_date_pattern.search(content)
    if maybe_date:
        return isoparse(maybe_date.group(0))
    else:
        return datetime.now()


def fix_links(content: str, when: datetime, base_url: str = "") -> str:
    def replace(match):
        return get_memento(make_absolute(match.group(1), base=base_url), when)
    return url_pattern.sub(replace, content)


def get_memento(url: str, when: datetime) -> str:
    timestamp = when.strftime("%Y%m%d%H%M%S")
    qs = urlparse(url).query
    return f"https://web.archive.org/web/{timestamp}/{url.removesuffix(qs)}"


def make_absolute(url: str, base: str) -> str:
    return urljoin(base, url)
