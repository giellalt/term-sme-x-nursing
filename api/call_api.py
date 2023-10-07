#!/usr/bin/env python3
"""Query the tartunlp api, nor-sme, with text from an input file.
Multiple requests will be sent if the file is not small enough to be sent in
one request. The file is split up so that each request is under 10000 bytes
long (well, hopefully, at least. see comment in code)."""

import argparse
import json
import sys
from urllib.request import urlopen, Request
import urllib.error

URL = "https://api.tartunlp.ai/translation/v2"

# kinda hard to make sure that the encoded data is always under 10000 bytes,
# due to encoding and such.. so just to be safe: take only this many characters
# from the text in each chunk (remember, one character can be encoded as
# multiple bytes)
N_CHARS = 7500


def make_payloads(text):
    assert isinstance(text, str)
    for n in range(0, len(text), N_CHARS):
        chunk, text = text[n:n+N_CHARS], text[n+N_CHARS:]
        if not chunk:
            break
        chunk = chunk.replace("¶", ".")

        payload = json.dumps({
          "text": chunk,
          "src": "nor",
          "tgt": "sme",
          "domain": "general",
          "application": "Documentation UI"
        })

        yield payload.encode("utf-8")


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "file",
        nargs="?",
        type=argparse.FileType("r", encoding="utf-8"),
        default=sys.stdin,
        help="The file with the text. Read from stdin if no file is given"
    )

    return parser.parse_args()


def main():
    args = parse_args()

    text = args.file.read()
    headers = {"content-type": "application/json"}

    return_chunks = []
    payloads = list(make_payloads(text))
    total_payload_len = sum(len(payload) for payload in payloads)

    n_bytes_remaining = total_payload_len
    for i, payload in enumerate(payloads, start=1):
        n_bytes_remaining -= len(payload)
        print(f"Sending request {i} of {len(payloads)} ({len(payload)} bytes, "
              f"{n_bytes_remaining} bytes left to send)",
              file=sys.stderr)
        if len(payload) >= 10000:
            print("error: a chunk was 10000 bytes or longer, adjust N_CHARS",
                  file=sys.stderr)
            break

        try:
            request = Request(URL, data=payload, headers=headers, method="POST")
            response = urlopen(request)
        except urllib.error.HTTPError as e:
            print(e)
            response_data = e.file.read().decode("utf-8")
            try:
                errmsg = json.loads(response_data)["detail"]
            except json.decoder.JSONDecodeError as e:
                print("error decoding response error payload:", e)
                print("raw data:", response_data)
            else:
                print(errmsg)
            finally:
                break
        else:
            returned_text = json.loads(response.read().decode("utf-8"))["result"]
            return_chunks.append(returned_text)

    for chunk in return_chunks:
        print(chunk)


if __name__ == "__main__":
    raise SystemExit(main())