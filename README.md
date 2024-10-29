# Nice QRcode

## Prerequisites

Install qrcode with **pillow** (PIL) support and pillow modules

```
python3 -m venv venv
source venv/bin/activate

pip install 'qrcode[pil]' pillow
```

## Run the code

Minimal example (URL + logo to insert)

```
python3 niceqrcode.py  https://kibana.zwindler.fr/okiwi-2425-form assets/logo.png
```

Example with output file path

```
python3 niceqrcode.py https://kibana.zwindler.fr/okiwi-2425-form assets/logo.png output.png
```

Example with output file path and footer

```
python3 niceqrcode.py https://kibana.zwindler.fr/okiwi-2425-form assets/logo.png output.png assets/footer.png
```

## Example output

![](assets/example_output.png)