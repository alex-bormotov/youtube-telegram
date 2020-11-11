# The bot sends thending Youtube videos to Telegram channel

![](https://github.com/alex-bormotov/youtube-telegram/workflows/Github-CICD/badge.svg)

## Install (Ubuntu + Docker)

```bash
git clone https://github.com/alex-bormotov/youtube-telegram
```

```bash
cd youtube-telegram
```

```bash
cp config/config.json.sample config/config.json
```

> Edit config/config.json

```bash
sudo chmod +x docker_ubuntu_install.sh && sudo ./docker_ubuntu_install.sh
```

```bash
sudo docker run -d --rm --mount src=`pwd`/config,target=/youtube-telegram/config,type=bind skilfulll1/youtube-telegram:latest
```
