# Python header parser microservice

This is a Python/[Flask](https://flask.palletsprojects.com/en/1.1.x/) port of my [Node.js header parser microservice project](https://ty-headerparser.glitch.me/), which was originally built to fulfill the following user stories:

1.  I can get the IP address, preferred languages (from header `Accept-Language`) and system infos (from header `User-Agent`) for my device.
    - Example usage:
      - `[base url]/api/whoami`
    - Example output:
      - `{"ipaddress": "::ffff:159.20.14.100", "language": "en-US,en;q=0.5", "software": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0"}`
