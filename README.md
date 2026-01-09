# deeplearning-20251-demo

For HUST's 20251 Deep Learning course.

This repository hosts the demonstration for our segmentation and inpainting Pytorch models. The models are run separately.

## Project Structure
```
deeplearning-20251-demo/
├── .venv/
├── app/
│   ├── assets/
│   ├── src/
│   ├── static/
│   └── templates/
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt
```
## Prerequisites
- Docker (if running with docker)
- Python w/ the various libraries in requirements.txt (if running locally; and preferrably, we use a Python virtual environment)
## Installation & Setup
### With Docker
__Pull image (warning: big)__:
```bash
docker pull espimkii/deeplearning-20251-demo:2.0
```
__Create a container from the image__:
```bash
docker run \
    --name deeplearning-demo \
    -p 5000:5000 \
    --restart unless-stopped \
    espimkii/deeplearning-20251-demo:2.0
```

### Running Locally
__Clone this repository:__
```bash
git clone https://github.com/EspiMKII/deeplearning-20251-demo.git
cd deeplearning-20251-demo
```

__Create a virtual environment and install the required libraries:__
```bash
python3 -m venv .venv
source .venv/bin/<activate-script>
pip install -r requirements.txt
```
Depending on what command line shell you use, activate-script needs to be different:
- PowerShell (Windows): Activate.ps1
- bash / zsh shell (Linux): activate
- fish shell (Linux): activate.fish

__Warning__: installing all the libraries may take... many seconds....

__Install model files__
```bash
cd app
mkdir assets/lightning_logs
mkdir assets/seg_models
```
For inpainting models, download the zip file from [this link](https://husteduvn-my.sharepoint.com/personal/chau_nb235481_sis_hust_edu_vn/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fchau%5Fnb235481%5Fsis%5Fhust%5Fedu%5Fvn%2FDocuments%2FSend%2F%5BDL%5DProject%5FSegmentation%5Fn%5FInpainting&ga=1) and extract the model_v2.ckpt file into assets/lightning_logs.

For segmentation models, download the .pth files from [this link](https://drive.google.com/drive/folders/1v5pOVZz3GwuBFYGYF83P2xc1J66zD9XR) and put them into assets/seg_models.

__Run the webapp__
```bash
cd ..
python3 app/src/base.py
```
Then, go to your local browser and connect to the domain `localhost:5000`
## Usage

## About
