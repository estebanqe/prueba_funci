cd //wsl.localhost/Ubuntu-22.04/home/esteban/vscode/prueba_func
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
reflex init
API_URL=pruebafunci-production.up.railway.app reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
deactivate