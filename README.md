```bash
docker run -d -t -i --name haumea \
        -v /data/www/haumea/:/data/www/haumea/ \
        -v /data/static/haumea:/data/static/haumea \
        -v /tmp:/tmp \
        -p 127.0.0.1:8000:8000 haumea

```

```bash
docker run --rm -t -i  \
        -v /data/www/haumea/:/data/www/haumea/ \
        -v /tmp:/tmp \
        haumea /bin/bash
```