import os
import sys
import subprocess
import venv
import platform

def run(cmd):
    print(f"🔧 Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def create_venv(venv_dir="venv"):
    if not os.path.exists(venv_dir):
        print("🐍 Creating virtual environment...")
        venv.EnvBuilder(with_pip=True).create(venv_dir)
    else:
        print("✅ Virtual environment already exists.")

def get_python_exec(venv_dir="venv"):
    if platform.system() == "Windows":
        return os.path.join(venv_dir, "Scripts", "python.exe")
    else:
        return os.path.join(venv_dir, "bin", "python")

def install_editable(python_exec, path):
    run(f'"{python_exec}" -m pip install -e "{path}"')

def install_dependencies(python_exec):
    run(f'"{python_exec}" -m pip install --upgrade pip setuptools')

def install_requirements(python_exec, filename="requirements.txt"):
    if os.path.exists(filename):
        print(f"📦 Installing requirements from {filename}...")
        run(f'"{python_exec}" -m pip install -r "{filename}"')
    else:
        print(f"⚠️ No {filename} found – skipping.")

def setup_all():
    venv_dir = "venv"
    create_venv(venv_dir)
    python_exec = get_python_exec(venv_dir)

    install_dependencies(python_exec)

    install_requirements(python_exec)

    # Install editable packages
    install_editable(python_exec, "src/dynamixel-port")
    install_editable(python_exec, "src/linear-interpolation")

    # Add SDK manually by setting PYTHONPATH-style hack via .pth file
    sdk_path = os.path.abspath("src/DynamixelSDK/python/src")
    site_packages_path = subprocess.check_output(
        [python_exec, "-c", "import site; print(site.getsitepackages()[0])"],
        text=True
    ).strip()
    pth_file = os.path.join(site_packages_path, "dynamixel_sdk.pth")

    print(f"🔗 Linking SDK via .pth file at: {pth_file}")
    with open(pth_file, "w") as f:
        f.write(sdk_path)

    print("🎉 Setup complete! Activate the environment with:")
    if platform.system() == "Windows":
        print(r"venv\Scripts\activate")
    else:
        print("source venv/bin/activate")
    print("Then run your scripts as usual.")

if __name__ == "__main__":
    setup_all()