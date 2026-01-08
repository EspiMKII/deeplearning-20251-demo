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
- Docker
- Python w/ the various libraries in requirements.txt (preferrably, we set up a virtual environment for this)
## Installation & Setup
### With Docker

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
