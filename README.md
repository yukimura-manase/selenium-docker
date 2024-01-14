# Selenium を Docker で動かす Sample

## Selenium の概要(Summary)

- Selenium は、主に Web アプリケーションのブラウザ操作を自動化するためのテストフレームワークです。
- ブラウザでの操作を自動化するスクリプトを作成することができるため、テスト自動化だけでなく、Web スクレイピングにも使用されます。
- Selenium の主な特徴とメリット、デメリットは、次のとおりです。

### 特徴

1. オープンソース: Selenium はオープンソースのテストフレームワークで、無償で利用することができます。

2. ブラウザの操作自動化: Web ブラウザの操作を自動化し、ユーザーのアクションをシミュレートすることが可能です。

3. 多言語対応: Python の他にも、Java、C#、Ruby など複数のプログラミング言語でスクリプトを記述できます。

4. クロスブラウザテスト: 複数のブラウザでテストを実行することが可能です。

## 環境構築

- 注意事項、M1 Mac など ARM で動作する環境かどうかで、使用するイメージが変わります。

- ARM 対応の Selenium Docker Image を使わないと M1 Mac などでは動きません。

  - 詳細は、[system spec が通らなくなった問題を SeleniARM で解決！](https://zenn.dev/lovegraph/articles/26109f0bc2f4c5)をご参照ください。

  - ちなみに、ARM 対応の Image 名は、docker-selenium ではなく、 docker-seleniarm になっている。。。芸が細かい。。。

- 環境に応じて、`docker-compose.yml`の`selenium`のコメントアウト箇所の編集をお願いします。

```yml: docker-compose.yml
version: "3"
services:
  # Selenium サーバを起動するコンテナ
  selenium:
    container_name: selenium-chrome
    # 通常の環境では、以下のイメージを使います。
    # image: selenium/standalone-chrome
    # M1 Mac など ARM で動作する環境では、以下のイメージを使います。
    image: seleniarm/standalone-chromium
    ports:
      # Selenium サーバに接続するポート
      - "4444:4444"
      # VNC で接続するポート
      - "5900:5900"
      # Selenium サーバのログを出力するポート
      - "7900:7900"
    # コンテナが使用するメモリの上限を設定
    shm_size: "2gb"
  # Web スクレイピングを実行するコンテナ
  scraping-app:
    container_name: app
    build: ./app
    volumes:
      - ./app:/opt/app
    tty: true
```

- Image の Build と Container の立ち上げを実施します。

```bash
docker compose up --build
```

- テストスクリプト実行環境のコンテナに入ります。

```bash
docker exec -it scraping-app /bin/bash
```

- テストスクリプトを実行します。

```bash
python ./src/company_judge.py
```

## [ 参考・引用 ]

1. [docker-selenium で E2E テスト環境構築 【Python】](https://tech-lab.sios.jp/archives/28840)

2. [Python Selenium について](https://zenn.dev/manase/scraps/28fe7b34824e79)

3. [system spec が通らなくなった問題を SeleniARM で解決！](https://zenn.dev/lovegraph/articles/26109f0bc2f4c5)

4. [Docker Seleniarm](https://github.com/seleniumhq-community/docker-seleniarm)
