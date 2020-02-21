# Sample setup on using ssl with postgres

Includes client cert verification!

## Quickstart

```
docker-compose up -d
```

Then see that all the requests from test-ssl.py works using

```
docker-compose logs -f
```

Tweak the settings to understand the moving parts!

## Notes

For this sample, `docker-compose up -d` will change the owner of the keys, so if you want to work with git you'll have to change the owners back.

```
sudo chown $USER *
```
